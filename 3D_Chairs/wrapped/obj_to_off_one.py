import os
import trimesh

filename = 'chair_001_191363'

try:
    mesh = trimesh.load(f'{filename}.obj')
    mesh.export(f'{filename}.off')
    print(f'Done converting {filename}.')
except:
    print('Could not finish the operation.')