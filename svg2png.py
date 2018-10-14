import cairosvg

import os

root_dir = os.path.dirname(__file__)
src_dir_name = 'INSTRUMENTS'
src_dir_path = os.path.join(root_dir, src_dir_name)
target_dir_name = '__files'
target_dir_path = os.path.join(root_dir, target_dir_name, src_dir_name)

if not os.path.exists(target_dir_path):
    os.makedirs(target_dir_path)

for f in os.listdir(src_dir_path):
    if not f.endswith('.svg'): continue
    print('Process: - %s' % f)
    cairosvg.svg2png(
        url=os.path.join(src_dir_path, f),
        write_to=os.path.join(root_dir, target_dir_name, src_dir_name, '%s.png' % f),
        d=1000
    )
