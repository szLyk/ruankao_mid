# 从 Chrome localStorage leveldb 提取 rk_practice_v1（支持跨块大值）
import os, glob, json, struct

LEV = r'C:\Users\luoyikai\AppData\Roaming\ZCode\session\Partitions\zcode-embedded-browser\Local Storage\leveldb'
TARGET = b'rk_practice_v1'

def snappy_decompress(data):
    i, out = 0, bytearray()
    ln, shift = 0, 0
    while True:
        c = data[i]; i += 1
        ln |= (c & 0x7F) << shift
        if not (c & 0x80): break
        shift += 7
    while len(out) < ln:
        tag = data[i]; i += 1
        t = tag & 3
        if t == 0:
            l = (tag >> 2) + 1
            if l > 60:
                extra = l - 60
                l = int.from_bytes(data[i:i+extra], 'little') + 1
                i += extra
            out += data[i:i+l]; i += l
        else:
            if t == 1:
                l = ((tag >> 2) & 7) + 4
                off = ((tag >> 5) << 8) | data[i]; i += 1
            elif t == 2:
                l = (tag >> 2) + 1
                off = int.from_bytes(data[i:i+2], 'little'); i += 2
            else:
                l = (tag >> 2) + 1
                off = int.from_bytes(data[i:i+4], 'little'); i += 4
            for _ in range(l):
                out.append(out[-off])
    return bytes(out)

def uvarint(b, i):
    r, s = 0, 0
    while True:
        c = b[i]; i += 1
        r |= (c & 0x7F) << s
        if not (c & 0x80): return r, i
        s += 7

def block_entries(b):
    if not b: return []
    n = int.from_bytes(b[-4:], 'little')
    end = len(b) - 4 - 4 * n - 1
    i, key, out = 0, b'', []
    while i < end:
        sh, i = uvarint(b, i); ns, i = uvarint(b, i); vl, i = uvarint(b, i)
        key = key[:sh] + b[i:i+ns]; i += ns
        out.append((key, b[i:i+vl]))          # 值字节（跨块大值在此块内被截断）
        i += vl
    return out

def ldb_blocks(raw):
    if len(raw) < 48 or struct.unpack('<Q', raw[-8:])[0] != 0xdb4775248b80fb57: return
    def load(off, size):
        chunk = raw[off:off+size+1]
        return snappy_decompress(chunk) if raw[off+size] == 1 else chunk[:size]
    footer = raw[-48:]
    _, i = uvarint(footer, 0); _, i = uvarint(footer, i)
    idx_off, i = uvarint(footer, i); idx_sz, i = uvarint(footer, i)
    idx = load(idx_off, idx_sz)
    blks = []
    for k, v in block_entries(idx):
        off, i2 = uvarint(v, 0); size, i2 = uvarint(v, i2)
        try: blks.append((off, load(off, size)))
        except Exception: pass
    blks.sort()
    return blks

def extract_values(path):
    """返回 [(value_bytes, 来源描述)]：枚举所有含 TARGET 的条目，大值跨块拼装"""
    raw = open(path, 'rb').read()
    blks = ldb_blocks(raw)
    if not blks: return []
    out = []
    for bi, (off, b) in enumerate(blks):
        entries = block_entries(b)
    for j, (key, _vb) in enumerate(entries):
        if TARGET not in key: continue
        # 回放该块条目，拿到此条目 value 的完整长度与块内起始偏移
        n = int.from_bytes(b[-4:], 'little')
        end = len(b) - 4 - 4 * n - 1
        i, key2, pos_of_val, full_vlen = 0, b'', 0, 0
        for jj in range(j + 1):
            sh, i = uvarint(b, i); ns, i = uvarint(b, i); vl, i = uvarint(b, i)
            key2 = key2[:sh] + b[i:i+ns]; i += ns
            if jj == j: pos_of_val = i; full_vlen = vl
            i += vl
        val = bytearray(b[pos_of_val:])
        src = f'{os.path.basename(path)}#blk{bi}#e{j}'
        if len(val) >= full_vlen:
            out.append((bytes(val[:full_vlen]), src)); continue
        # 大值：拼接后续块
        bi2 = bi
        for bi2 in range(bi + 1, len(blks)):
            val += blks[bi2][1]
            if len(val) >= full_vlen: break
        out.append((bytes(val[:full_vlen]), src + f'(+{bi2-bi}块)'))
    return out

def read_log(path):
    """WriteBatch 日志：crc(4)+len(2)+type(1) 分帧，32KB 块；载荷=seq(8)+count(4)+条目"""
    results = []
    raw = open(path, 'rb').read()
    pos, buf = 0, b''
    while pos + 7 <= len(raw):
        ln = int.from_bytes(raw[pos+4:pos+6], 'little')
        typ = raw[pos+6]
        if ln > 40000: break
        rec = raw[pos+7:pos+7+ln]
        pos += 7 + ln
        if typ == 1 or typ == 2: buf = rec          # full / first
        elif typ == 3 or typ == 4: buf += rec       # middle / last
        else: continue
        if typ not in (1, 4): continue              # 未拼完不解析
        i = 12
        try:
            while i < len(buf):
                t = buf[i]; i += 1
                if t != 1: break
                klen, i = uvarint(buf, i)
                key = buf[i:i+klen]; i += klen
                vlen, i = uvarint(buf, i)
                val = buf[i:i+vlen]; i += vlen
                if TARGET in key:
                    results.append(val)
        except Exception:
            pass
    return results

versions = []
for f in sorted(glob.glob(os.path.join(LEV, '*.ldb')), key=os.path.getmtime, reverse=True):
    try:
        for v, src in extract_values(f):
            versions.append((src, v))
    except Exception as e:
        print('跳过', f, e)
for f in glob.glob(os.path.join(LEV, '*.log')):
    print('log:', os.path.basename(f), os.path.getsize(f), '字节')
    for v in read_log(f):
        versions.append(('log:' + os.path.basename(f), v))

print('版本数:', len(versions))
best = None
for src, v in versions:
    if v[:1] == b'\x01': v = v[1:]                  # localStorage 值首字节是编码标记
    try:
        obj = json.loads(v.decode('utf-8'))
        n = len(obj.get('answers', {})); lu = obj.get('lastUpdated', '')
        print(f'  {src}: 作答{n} lastUpdated={lu} 长度{len(v)}')
        if best is None or (n, lu) > (len(best.get('answers', {})), best.get('lastUpdated', '')):
            best = obj
    except Exception as e:
        print(f'  {src}: 解析失败({len(v)}字节) {str(e)[:60]} 头40: {v[:40]!r}')
if best:
    json.dump(best, open(r'D:\Project requirements\软考\.chrome_rec.json', 'w', encoding='utf-8'), ensure_ascii=False)
    print('✅ 最优: 作答', len(best['answers']), '| lastUpdated', best.get('lastUpdated'), '→ .chrome_rec.json')
