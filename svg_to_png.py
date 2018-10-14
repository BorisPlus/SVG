import cairosvg

import os

root_dir = os.path.dirname(__file__)
src_dir_name = 'INSTRUMENTS'
src_dir_path = os.path.join(root_dir, src_dir_name)
target_dir_name = 'gitignore/png'
target_dir_path = os.path.join(root_dir, target_dir_name)
for f in os.listdir(src_dir_path):
    print(f)
    if not f.endswith('.svg'): continue
    cairosvg.svg2png(
        url=os.path.join(src_dir_path, f),
        write_to=os.path.join(target_dir_path, '%s.png' % f),
        d=1000
    )
