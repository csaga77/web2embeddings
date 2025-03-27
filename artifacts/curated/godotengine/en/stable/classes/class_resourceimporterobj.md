# ResourceImporterOBJ

Inherits: ResourceImporter < RefCounted < Object

Imports an OBJ 3D model as an independent Mesh or scene.

## Description

Unlike ResourceImporterScene, ResourceImporterOBJ will import a single Mesh
resource by default instead of importing a PackedScene. This makes it easier
to use the Mesh resource in nodes that expect direct Mesh resources, such as
GridMap, GPUParticles3D or CPUParticles3D. Note that it is still possible to
save mesh resources from 3D scenes using the Advanced Import Settings dialog,
regardless of the source format.

See also ResourceImporterScene, which is used for more advanced 3D formats
such as glTF.

## Tutorials

  * Importing 3D scenes

## Properties

bool | force_disable_mesh_compression | `false`  
---|---|---  
bool | generate_lightmap_uv2 | `false`  
float | generate_lightmap_uv2_texel_size | `0.2`  
bool | generate_lods | `true`  
bool | generate_shadow_mesh | `true`  
bool | generate_tangents | `true`  
Vector3 | offset_mesh | `Vector3(0, 0, 0)`  
Vector3 | scale_mesh | `Vector3(1, 1, 1)`  
  
## Property Descriptions

bool force_disable_mesh_compression = `false`

If `true`, mesh compression will not be used. Consider enabling if you notice
blocky artifacts in your mesh normals or UVs, or if you have meshes that are
larger than a few thousand meters in each direction.

bool generate_lightmap_uv2 = `false`

If `true`, generates UV2 on import for LightmapGI baking.

float generate_lightmap_uv2_texel_size = `0.2`

Controls the size of each texel on the baked lightmap. A smaller value results
in more precise lightmaps, at the cost of larger lightmap sizes and longer
bake times.

Note: Only effective if generate_lightmap_uv2 is `true`.

bool generate_lods = `true`

If `true`, generates lower detail variants of the mesh which will be displayed
in the distance to improve rendering performance. Not all meshes benefit from
LOD, especially if they are never rendered from far away. Disabling this can
reduce output file size and speed up importing. See Mesh level of detail (LOD)
for more information.

bool generate_shadow_mesh = `true`

If `true`, enables the generation of shadow meshes on import. This optimizes
shadow rendering without reducing quality by welding vertices together when
possible. This in turn reduces the memory bandwidth required to render
shadows. Shadow mesh generation currently doesn't support using a lower detail
level than the source mesh (but shadow rendering will make use of LODs when
relevant).

bool generate_tangents = `true`

If `true`, generate vertex tangents using Mikktspace if the source mesh
doesn't have tangent data. When possible, it's recommended to let the 3D
modeling software generate tangents on export instead on relying on this
option. Tangents are required for correct display of normal and height maps,
along with any material/shader features that require tangents.

If you don't need material features that require tangents, disabling this can
reduce output file size and speed up importing if the source 3D file doesn't
contain tangents.

Vector3 offset_mesh = `Vector3(0, 0, 0)`

Offsets the mesh's data by the specified value. This can be used to work
around misaligned meshes without having to modify the source file.

Vector3 scale_mesh = `Vector3(1, 1, 1)`

Scales the mesh's data by the specified value. This can be used to work around
misscaled meshes without having to modify the source file.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

