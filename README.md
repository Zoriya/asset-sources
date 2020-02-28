# Asset sources

Files for generating assets for Zoriya

## Assets generation

Script `ExportToGltf.py` automatically exports all assets in glTF to corresponding folders. It optionally accepts path to the project (by default `../zoriya` will be used).

**Example:**

```bash
blender --background --python ExportToGltf.py -- /path/to/zoriya/
```
