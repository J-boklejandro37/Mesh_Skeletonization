import os
import trimesh

from pathlib import Path

'''
# files = list(Path(input_folder).glob('**/*.obj'))
# -> [Path("models/model1.obj"), Path("textures/bump/model2.obj"), Path("model3.obj")]

# Get only filename (without folder)
# filenames = [file_path.name for file_path in files]
# -> ["model1.obj", "model2.obj", "model3.obj"]

# Get only filename (without folder and extension)
# filenames_no_ext = [file_path.stem for file_path in files]
# ->["model1", "model2", "model3"]
'''

def batch(folder, ext_old, ext_new):
    file_paths = list(Path(folder).glob(f'*.{ext_old}'))
    for file_path in file_paths:
        # print(f'{folder}{file_path.name}')
        # print(f'{folder}{file_path.stem}.{ext_new}')
        mesh = trimesh.load(f'{folder}{file_path.name}')
        mesh.export(f'{folder}{file_path.stem}.{ext_new}')
        print(f'Done converting {file_path.stem}.{ext_old} to {file_path.stem}.{ext_new}.')

if __name__ == '__main__':
    batch('../wrapped/', 'obj', 'off')