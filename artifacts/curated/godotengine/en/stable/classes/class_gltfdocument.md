# GLTFDocument

Inherits: Resource < RefCounted < Object

Inherited By: FBXDocument

Class for importing and exporting glTF files in and out of Godot.

## Description

GLTFDocument supports reading data from a glTF file, buffer, or Godot scene.
This data can then be written to the filesystem, buffer, or used to create a
Godot scene.

All of the data in a glTF scene is stored in the GLTFState class. GLTFDocument
processes state objects, but does not contain any scene data itself.
GLTFDocument has member variables to store export configuration settings such
as the image format, but is otherwise stateless. Multiple scenes can be
processed with the same settings using the same GLTFDocument object and
different GLTFState objects.

GLTFDocument can be extended with arbitrary functionality by extending the
GLTFDocumentExtension class and registering it with GLTFDocument via
register_gltf_document_extension(). This allows for custom data to be imported
and exported.

## Tutorials

  * Runtime file loading and saving

  * glTF 'What the duck?' guide

  * Khronos glTF specification

## Properties

String | image_format | `"PNG"`  
---|---|---  
float | lossy_quality | `0.75`  
RootNodeMode | root_node_mode | `0`  
  
## Methods

Error | append_from_buffer(bytes: PackedByteArray, base_path: String, state: GLTFState, flags: int = 0)  
---|---  
Error | append_from_file(path: String, state: GLTFState, flags: int = 0, base_path: String = "")  
Error | append_from_scene(node: Node, state: GLTFState, flags: int = 0)  
GLTFObjectModelProperty | export_object_model_property(state: GLTFState, node_path: NodePath, godot_node: Node, gltf_node_index: int) static  
PackedByteArray | generate_buffer(state: GLTFState)  
Node | generate_scene(state: GLTFState, bake_fps: float = 30, trimming: bool = false, remove_immutable_tracks: bool = true)  
PackedStringArray | get_supported_gltf_extensions() static  
GLTFObjectModelProperty | import_object_model_property(state: GLTFState, json_pointer: String) static  
void | register_gltf_document_extension(extension: GLTFDocumentExtension, first_priority: bool = false) static  
void | unregister_gltf_document_extension(extension: GLTFDocumentExtension) static  
Error | write_to_filesystem(state: GLTFState, path: String)  
  
## Enumerations

enum RootNodeMode:

RootNodeMode ROOT_NODE_MODE_SINGLE_ROOT = `0`

Treat the Godot scene's root node as the root node of the glTF file, and mark
it as the single root node via the `GODOT_single_root` glTF extension. This
will be parsed the same as ROOT_NODE_MODE_KEEP_ROOT if the implementation does
not support `GODOT_single_root`.

RootNodeMode ROOT_NODE_MODE_KEEP_ROOT = `1`

Treat the Godot scene's root node as the root node of the glTF file, but do
not mark it as anything special. An extra root node will be generated when
importing into Godot. This uses only vanilla glTF features. This is equivalent
to the behavior in Godot 4.1 and earlier.

RootNodeMode ROOT_NODE_MODE_MULTI_ROOT = `2`

Treat the Godot scene's root node as the name of the glTF scene, and add all
of its children as root nodes of the glTF file. This uses only vanilla glTF
features. This avoids an extra root node, but only the name of the Godot
scene's root node will be preserved, as it will not be saved as a node.

## Property Descriptions

String image_format = `"PNG"`

  * void set_image_format(value: String)

  * String get_image_format()

The user-friendly name of the export image format. This is used when exporting
the glTF file, including writing to a file and writing to a byte array.

By default, Godot allows the following options: "None", "PNG", "JPEG",
"Lossless WebP", and "Lossy WebP". Support for more image formats can be added
in GLTFDocumentExtension classes.

float lossy_quality = `0.75`

  * void set_lossy_quality(value: float)

  * float get_lossy_quality()

If image_format is a lossy image format, this determines the lossy quality of
the image. On a range of `0.0` to `1.0`, where `0.0` is the lowest quality and
`1.0` is the highest quality. A lossy quality of `1.0` is not the same as
lossless.

RootNodeMode root_node_mode = `0`

  * void set_root_node_mode(value: RootNodeMode)

  * RootNodeMode get_root_node_mode()

How to process the root node during export. See RootNodeMode for details. The
default and recommended value is ROOT_NODE_MODE_SINGLE_ROOT.

Note: Regardless of how the glTF file is exported, when importing, the root
node type and name can be overridden in the scene import settings tab.

## Method Descriptions

Error append_from_buffer(bytes: PackedByteArray, base_path: String, state:
GLTFState, flags: int = 0)

Takes a PackedByteArray defining a glTF and imports the data to the given
GLTFState object through the `state` parameter.

Note: The `base_path` tells append_from_buffer() where to find dependencies
and can be empty.

Error append_from_file(path: String, state: GLTFState, flags: int = 0,
base_path: String = "")

Takes a path to a glTF file and imports the data at that file path to the
given GLTFState object through the `state` parameter.

Note: The `base_path` tells append_from_file() where to find dependencies and
can be empty.

Error append_from_scene(node: Node, state: GLTFState, flags: int = 0)

Takes a Godot Engine scene node and exports it and its descendants to the
given GLTFState object through the `state` parameter.

GLTFObjectModelProperty export_object_model_property(state: GLTFState,
node_path: NodePath, godot_node: Node, gltf_node_index: int) static

Determines a mapping between the given Godot `node_path` and the corresponding
glTF Object Model JSON pointer(s) in the generated glTF file. The details of
this mapping are returned in a GLTFObjectModelProperty object. Additional
mappings can be supplied via the
GLTFDocumentExtension._import_object_model_property() callback method.

PackedByteArray generate_buffer(state: GLTFState)

Takes a GLTFState object through the `state` parameter and returns a glTF
PackedByteArray.

Node generate_scene(state: GLTFState, bake_fps: float = 30, trimming: bool =
false, remove_immutable_tracks: bool = true)

Takes a GLTFState object through the `state` parameter and returns a Godot
Engine scene node.

The `bake_fps` parameter overrides the bake_fps in `state`.

PackedStringArray get_supported_gltf_extensions() static

Returns a list of all support glTF extensions, including extensions supported
directly by the engine, and extensions supported by user plugins registering
GLTFDocumentExtension classes.

Note: If this method is run before a GLTFDocumentExtension is registered, its
extensions won't be included in the list. Be sure to only run this method
after all extensions are registered. If you run this when the engine starts,
consider waiting a frame before calling this method to ensure all extensions
are registered.

GLTFObjectModelProperty import_object_model_property(state: GLTFState,
json_pointer: String) static

Determines a mapping between the given glTF Object Model `json_pointer` and
the corresponding Godot node path(s) in the generated Godot scene. The details
of this mapping are returned in a GLTFObjectModelProperty object. Additional
mappings can be supplied via the
GLTFDocumentExtension._export_object_model_property() callback method.

void register_gltf_document_extension(extension: GLTFDocumentExtension,
first_priority: bool = false) static

Registers the given GLTFDocumentExtension instance with GLTFDocument. If
`first_priority` is `true`, this extension will be run first. Otherwise, it
will be run last.

Note: Like GLTFDocument itself, all GLTFDocumentExtension classes must be
stateless in order to function properly. If you need to store data, use the
`set_additional_data` and `get_additional_data` methods in GLTFState or
GLTFNode.

void unregister_gltf_document_extension(extension: GLTFDocumentExtension)
static

Unregisters the given GLTFDocumentExtension instance.

Error write_to_filesystem(state: GLTFState, path: String)

Takes a GLTFState object through the `state` parameter and writes a glTF file
to the filesystem.

Note: The extension of the glTF file determines if it is a .glb binary file or
a .gltf text file.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.
  *[void]: No return value.

