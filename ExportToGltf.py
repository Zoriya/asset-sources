import bpy
import sys
from pathlib import Path


def export_file(filename, output_path):
    bpy.ops.wm.open_mainfile(filepath=str(filename))
    Path(output_path / filename.parent).mkdir(parents=True, exist_ok=True)
    output_filename = str(output_path / filename.with_suffix('.glb'))
    bpy.ops.export_scene.gltf(filepath=output_filename,
                              export_materials=False,
                              export_apply=True)


def zorya_path():
    if '--' in sys.argv:
        return Path(sys.argv[sys.argv.index('--') + 1])
    else:
        return Path('../zoriya')


output_path = zorya_path()
for pattern in ('Environment/Camp/*.blend', 'Items/Potions/*.blend'):
    for filename in Path('.').glob(pattern):
        export_file(filename, output_path)
