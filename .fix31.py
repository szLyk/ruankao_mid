# -*- coding: utf-8 -*-
import io
t = io.open('.add31ex.py', encoding='utf-8').read()
old = """a5 = '</section>\\n\\n<section id="s-kgmap">'"""
assert old in t, [l for l in t.split('\n') if 'a5 =' in l]
new = """a5 = '</section>\\n\\n<!-- ============ \U0001f578 知识图谱 ============ -->\\n<section id="s-kgmap">'"""
t = t.replace(old, new, 1)
old2 = """t = t.replace(a5, dp_card + '</section>\\n\\n<section id="s-kgmap">', 1)"""
assert old2 in t, [l for l in t.split('\n') if 'dp_card +' in l]
new2 = """t = t.replace(a5, dp_card + '</section>\\n\\n<!-- ============ \U0001f578 知识图谱 ============ -->\\n<section id="s-kgmap">', 1)"""
t = t.replace(old2, new2, 1)
io.open('.add31ex.py', 'w', encoding='utf-8', newline='').write(t)
print('OK')
