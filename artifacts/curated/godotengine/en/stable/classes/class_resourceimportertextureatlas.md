# ResourceImporterTextureAtlas

Inherits: ResourceImporter < RefCounted < Object

Imports a collection of textures from a PNG image into an optimized
AtlasTexture for 2D rendering.

## Description

This imports a collection of textures from a PNG image into an AtlasTexture or
2D ArrayMesh. This can be used to save memory when importing 2D animations
from spritesheets. Texture atlases are only supported in 2D rendering, not 3D.
See also ResourceImporterTexture and ResourceImporterLayeredTexture.

Note: ResourceImporterTextureAtlas does not handle importing
TileSetAtlasSource, which is created using the TileSet editor instead.

## Properties

String | atlas_file | `""`  
---|---|---  
bool | crop_to_region | `false`  
int | import_mode | `0`  
bool | trim_alpha_border_from_region | `true`  
  
## Property Descriptions

String atlas_file = `""`

Path to the atlas spritesheet. This must be set to valid path to a PNG image.
Otherwise, the atlas will fail to import.

bool crop_to_region = `false`

If `true`, discards empty areas from the atlas. This only affects final sprite
positioning, not storage. See also trim_alpha_border_from_region.

Note: Only effective if import_mode is Region.

int import_mode = `0`

Region: Imports the atlas in an AtlasTexture resource, which is rendered as a
rectangle. This is fast to render, but transparent areas still have to be
rendered if they can't be trimmed effectively by
trim_alpha_border_from_region. This can reduce performance when rendering
large sprites on screen.

Mesh: Imports the atlas as an ArrayMesh resource, keeping the original bitmap
visible (but rendered as a polygon). This can be used to reduce fill rate when
rendering large transparent sprites, at the cost of slower rendering if there
are little to no transparent areas in the sprite.

bool trim_alpha_border_from_region = `true`

If `true`, trims the region to exclude fully transparent pixels using a
clipping rectangle (which is never rotated). This can be used to save memory.
See also crop_to_region.

Note: Only effective if import_mode is Region.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

