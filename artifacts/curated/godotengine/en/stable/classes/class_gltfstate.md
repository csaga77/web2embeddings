# GLTFState

Inherits: Resource < RefCounted < Object

Inherited By: FBXState

Represents all data of a glTF file.

## Description

Contains all nodes and resources of a glTF file. This is used by GLTFDocument
as data storage, which allows GLTFDocument and all GLTFDocumentExtension
classes to remain stateless.

GLTFState can be populated by GLTFDocument reading a file or by converting a
Godot scene. Then the data can either be used to create a Godot scene or save
to a glTF file. The code that converts to/from a Godot scene can be
intercepted at arbitrary points by GLTFDocumentExtension classes. This allows
for custom data to be stored in the glTF file or for custom data to be
converted to/from Godot nodes.

## Tutorials

  * Runtime file loading and saving

  * glTF asset header schema

## Properties

float | bake_fps | `30.0`  
---|---|---  
String | base_path | `""`  
Array[PackedByteArray] | buffers | `[]`  
String | copyright | `""`  
bool | create_animations | `true`  
String | filename | `""`  
PackedByteArray | glb_data | `PackedByteArray()`  
bool | import_as_skeleton_bones | `false`  
Dictionary | json | `{}`  
int | major_version | `0`  
int | minor_version | `0`  
PackedInt32Array | root_nodes | `PackedInt32Array()`  
String | scene_name | `""`  
bool | use_named_skin_binds | `false`  
  
## Methods

void | add_used_extension(extension_name: String, required: bool)  
---|---  
int | append_data_to_buffers(data: PackedByteArray, deduplication: bool)  
int | append_gltf_node(gltf_node: GLTFNode, godot_scene_node: Node, parent_node_index: int)  
Array[GLTFAccessor] | get_accessors()  
Variant | get_additional_data(extension_name: StringName)  
AnimationPlayer | get_animation_player(idx: int)  
int | get_animation_players_count(idx: int)  
Array[GLTFAnimation] | get_animations()  
Array[GLTFBufferView] | get_buffer_views()  
Array[GLTFCamera] | get_cameras()  
int | get_handle_binary_image()  
Array[Texture2D] | get_images()  
Array[GLTFLight] | get_lights()  
Array[Material] | get_materials()  
Array[GLTFMesh] | get_meshes()  
int | get_node_index(scene_node: Node)  
Array[GLTFNode] | get_nodes()  
Node | get_scene_node(idx: int)  
Array[GLTFSkeleton] | get_skeletons()  
Array[GLTFSkin] | get_skins()  
Array[GLTFTextureSampler] | get_texture_samplers()  
Array[GLTFTexture] | get_textures()  
Array[String] | get_unique_animation_names()  
Array[String] | get_unique_names()  
void | set_accessors(accessors: Array[GLTFAccessor])  
void | set_additional_data(extension_name: StringName, additional_data: Variant)  
void | set_animations(animations: Array[GLTFAnimation])  
void | set_buffer_views(buffer_views: Array[GLTFBufferView])  
void | set_cameras(cameras: Array[GLTFCamera])  
void | set_handle_binary_image(method: int)  
void | set_images(images: Array[Texture2D])  
void | set_lights(lights: Array[GLTFLight])  
void | set_materials(materials: Array[Material])  
void | set_meshes(meshes: Array[GLTFMesh])  
void | set_nodes(nodes: Array[GLTFNode])  
void | set_skeletons(skeletons: Array[GLTFSkeleton])  
void | set_skins(skins: Array[GLTFSkin])  
void | set_texture_samplers(texture_samplers: Array[GLTFTextureSampler])  
void | set_textures(textures: Array[GLTFTexture])  
void | set_unique_animation_names(unique_animation_names: Array[String])  
void | set_unique_names(unique_names: Array[String])  
  
## Constants

HANDLE_BINARY_DISCARD_TEXTURES = `0`

Discards all embedded textures and uses untextured materials.

HANDLE_BINARY_EXTRACT_TEXTURES = `1`

Extracts embedded textures to be reimported and compressed. Editor only. Acts
as uncompressed at runtime.

HANDLE_BINARY_EMBED_AS_BASISU = `2`

Embeds textures VRAM compressed with Basis Universal into the generated scene.

HANDLE_BINARY_EMBED_AS_UNCOMPRESSED = `3`

Embeds textures compressed losslessly into the generated scene, matching old
behavior.

## Property Descriptions

float bake_fps = `30.0`

  * void set_bake_fps(value: float)

  * float get_bake_fps()

The baking fps of the animation for either import or export.

String base_path = `""`

  * void set_base_path(value: String)

  * String get_base_path()

The folder path associated with this glTF data. This is used to find other
files the glTF file references, like images or binary buffers. This will be
set during import when appending from a file, and will be set during export
when writing to a file.

Array[PackedByteArray] buffers = `[]`

  * void set_buffers(value: Array[PackedByteArray])

  * Array[PackedByteArray] get_buffers()

There is currently no description for this property. Please help us by
contributing one!

String copyright = `""`

  * void set_copyright(value: String)

  * String get_copyright()

The copyright string in the asset header of the glTF file. This is set during
import if present and export if non-empty. See the glTF asset header
documentation for more information.

bool create_animations = `true`

  * void set_create_animations(value: bool)

  * bool get_create_animations()

There is currently no description for this property. Please help us by
contributing one!

String filename = `""`

  * void set_filename(value: String)

  * String get_filename()

The file name associated with this glTF data. If it ends with `.gltf`, this is
text-based glTF, otherwise this is binary GLB. This will be set during import
when appending from a file, and will be set during export when writing to a
file. If writing to a buffer, this will be an empty string.

PackedByteArray glb_data = `PackedByteArray()`

  * void set_glb_data(value: PackedByteArray)

  * PackedByteArray get_glb_data()

The binary buffer attached to a .glb file.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

bool import_as_skeleton_bones = `false`

  * void set_import_as_skeleton_bones(value: bool)

  * bool get_import_as_skeleton_bones()

If `true`, forces all GLTFNodes in the document to be bones of a single
Skeleton3D Godot node.

Dictionary json = `{}`

  * void set_json(value: Dictionary)

  * Dictionary get_json()

The original raw JSON document corresponding to this GLTFState.

int major_version = `0`

  * void set_major_version(value: int)

  * int get_major_version()

There is currently no description for this property. Please help us by
contributing one!

int minor_version = `0`

  * void set_minor_version(value: int)

  * int get_minor_version()

There is currently no description for this property. Please help us by
contributing one!

PackedInt32Array root_nodes = `PackedInt32Array()`

  * void set_root_nodes(value: PackedInt32Array)

  * PackedInt32Array get_root_nodes()

The root nodes of the glTF file. Typically, a glTF file will only have one
scene, and therefore one root node. However, a glTF file may have multiple
scenes and therefore multiple root nodes, which will be generated as siblings
of each other and as children of the root node of the generated Godot scene.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedInt32Array for more details.

String scene_name = `""`

  * void set_scene_name(value: String)

  * String get_scene_name()

The name of the scene. When importing, if not specified, this will be the file
name. When exporting, if specified, the scene name will be saved to the glTF
file.

bool use_named_skin_binds = `false`

  * void set_use_named_skin_binds(value: bool)

  * bool get_use_named_skin_binds()

There is currently no description for this property. Please help us by
contributing one!

## Method Descriptions

void add_used_extension(extension_name: String, required: bool)

Appends an extension to the list of extensions used by this glTF file during
serialization. If `required` is `true`, the extension will also be added to
the list of required extensions. Do not run this in
GLTFDocumentExtension._export_post(), as that stage is too late to add
extensions. The final list is sorted alphabetically.

int append_data_to_buffers(data: PackedByteArray, deduplication: bool)

Appends the given byte array data to the buffers and creates a GLTFBufferView
for it. The index of the destination GLTFBufferView is returned. If
`deduplication` is `true`, the buffers will first be searched for duplicate
data, otherwise new bytes will always be appended.

int append_gltf_node(gltf_node: GLTFNode, godot_scene_node: Node,
parent_node_index: int)

Append the given GLTFNode to the state, and return its new index. This can be
used to export one Godot node as multiple glTF nodes, or inject new glTF nodes
at import time. On import, this must be called before
GLTFDocumentExtension._generate_scene_node() finishes for the parent node. On
export, this must be called before GLTFDocumentExtension._export_node() runs
for the parent node.

The `godot_scene_node` parameter is the Godot scene node that corresponds to
this glTF node. This is highly recommended to be set to a valid node, but may
be `null` if there is no corresponding Godot scene node. One Godot scene node
may be used for multiple glTF nodes, so if exporting multiple glTF nodes for
one Godot scene node, use the same Godot scene node for each.

The `parent_node_index` parameter is the index of the parent GLTFNode in the
state. If `-1`, the node will be a root node, otherwise the new node will be
added to the parent's list of children. The index will also be written to the
GLTFNode.parent property of the new node.

Array[GLTFAccessor] get_accessors()

There is currently no description for this method. Please help us by
contributing one!

Variant get_additional_data(extension_name: StringName)

Gets additional arbitrary data in this GLTFState instance. This can be used to
keep per-file state data in GLTFDocumentExtension classes, which is important
because they are stateless.

The argument should be the GLTFDocumentExtension name (does not have to match
the extension name in the glTF file), and the return value can be anything you
set. If nothing was set, the return value is `null`.

AnimationPlayer get_animation_player(idx: int)

Returns the AnimationPlayer node with the given index. These nodes are only
used during the export process when converting Godot AnimationPlayer nodes to
glTF animations.

int get_animation_players_count(idx: int)

Returns the number of AnimationPlayer nodes in this GLTFState. These nodes are
only used during the export process when converting Godot AnimationPlayer
nodes to glTF animations.

Array[GLTFAnimation] get_animations()

Returns an array of all GLTFAnimations in the glTF file. When importing, these
will be generated as animations in an AnimationPlayer node. When exporting,
these will be generated from Godot AnimationPlayer nodes.

Array[GLTFBufferView] get_buffer_views()

There is currently no description for this method. Please help us by
contributing one!

Array[GLTFCamera] get_cameras()

Returns an array of all GLTFCameras in the glTF file. These are the cameras
that the GLTFNode.camera index refers to.

int get_handle_binary_image()

There is currently no description for this method. Please help us by
contributing one!

Array[Texture2D] get_images()

Gets the images of the glTF file as an array of Texture2Ds. These are the
images that the GLTFTexture.src_image index refers to.

Array[GLTFLight] get_lights()

Returns an array of all GLTFLights in the glTF file. These are the lights that
the GLTFNode.light index refers to.

Array[Material] get_materials()

There is currently no description for this method. Please help us by
contributing one!

Array[GLTFMesh] get_meshes()

Returns an array of all GLTFMeshes in the glTF file. These are the meshes that
the GLTFNode.mesh index refers to.

int get_node_index(scene_node: Node)

Returns the index of the GLTFNode corresponding to this Godot scene node. This
is the inverse of get_scene_node(). Useful during the export process.

Note: Not every Godot scene node will have a corresponding GLTFNode, and not
every GLTFNode will have a scene node generated. If there is no GLTFNode index
for this scene node, `-1` is returned.

Array[GLTFNode] get_nodes()

Returns an array of all GLTFNodes in the glTF file. These are the nodes that
GLTFNode.children and root_nodes refer to. This includes nodes that may not be
generated in the Godot scene, or nodes that may generate multiple Godot scene
nodes.

Node get_scene_node(idx: int)

Returns the Godot scene node that corresponds to the same index as the
GLTFNode it was generated from. This is the inverse of get_node_index().
Useful during the import process.

Note: Not every GLTFNode will have a scene node generated, and not every
generated scene node will have a corresponding GLTFNode. If there is no scene
node for this GLTFNode index, `null` is returned.

Array[GLTFSkeleton] get_skeletons()

Returns an array of all GLTFSkeletons in the glTF file. These are the
skeletons that the GLTFNode.skeleton index refers to.

Array[GLTFSkin] get_skins()

Returns an array of all GLTFSkins in the glTF file. These are the skins that
the GLTFNode.skin index refers to.

Array[GLTFTextureSampler] get_texture_samplers()

Retrieves the array of texture samplers that are used by the textures
contained in the glTF.

Array[GLTFTexture] get_textures()

There is currently no description for this method. Please help us by
contributing one!

Array[String] get_unique_animation_names()

Returns an array of unique animation names. This is only used during the
import process.

Array[String] get_unique_names()

Returns an array of unique node names. This is used in both the import process
and export process.

void set_accessors(accessors: Array[GLTFAccessor])

There is currently no description for this method. Please help us by
contributing one!

void set_additional_data(extension_name: StringName, additional_data: Variant)

Sets additional arbitrary data in this GLTFState instance. This can be used to
keep per-file state data in GLTFDocumentExtension classes, which is important
because they are stateless.

The first argument should be the GLTFDocumentExtension name (does not have to
match the extension name in the glTF file), and the second argument can be
anything you want.

void set_animations(animations: Array[GLTFAnimation])

Sets the GLTFAnimations in the state. When importing, these will be generated
as animations in an AnimationPlayer node. When exporting, these will be
generated from Godot AnimationPlayer nodes.

void set_buffer_views(buffer_views: Array[GLTFBufferView])

There is currently no description for this method. Please help us by
contributing one!

void set_cameras(cameras: Array[GLTFCamera])

Sets the GLTFCameras in the state. These are the cameras that the
GLTFNode.camera index refers to.

void set_handle_binary_image(method: int)

There is currently no description for this method. Please help us by
contributing one!

void set_images(images: Array[Texture2D])

Sets the images in the state stored as an array of Texture2Ds. This can be
used during export. These are the images that the GLTFTexture.src_image index
refers to.

void set_lights(lights: Array[GLTFLight])

Sets the GLTFLights in the state. These are the lights that the GLTFNode.light
index refers to.

void set_materials(materials: Array[Material])

There is currently no description for this method. Please help us by
contributing one!

void set_meshes(meshes: Array[GLTFMesh])

Sets the GLTFMeshes in the state. These are the meshes that the GLTFNode.mesh
index refers to.

void set_nodes(nodes: Array[GLTFNode])

Sets the GLTFNodes in the state. These are the nodes that GLTFNode.children
and root_nodes refer to. Some of the nodes set here may not be generated in
the Godot scene, or may generate multiple Godot scene nodes.

void set_skeletons(skeletons: Array[GLTFSkeleton])

Sets the GLTFSkeletons in the state. These are the skeletons that the
GLTFNode.skeleton index refers to.

void set_skins(skins: Array[GLTFSkin])

Sets the GLTFSkins in the state. These are the skins that the GLTFNode.skin
index refers to.

void set_texture_samplers(texture_samplers: Array[GLTFTextureSampler])

Sets the array of texture samplers that are used by the textures contained in
the glTF.

void set_textures(textures: Array[GLTFTexture])

There is currently no description for this method. Please help us by
contributing one!

void set_unique_animation_names(unique_animation_names: Array[String])

Sets the unique animation names in the state. This is only used during the
import process.

void set_unique_names(unique_names: Array[String])

Sets the unique node names in the state. This is used in both the import
process and export process.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

