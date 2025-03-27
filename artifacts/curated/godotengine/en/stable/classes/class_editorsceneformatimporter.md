# EditorSceneFormatImporter

Inherits: RefCounted < Object

Inherited By: EditorSceneFormatImporterBlend,
EditorSceneFormatImporterFBX2GLTF, EditorSceneFormatImporterGLTF,
EditorSceneFormatImporterUFBX

Imports scenes from third-parties' 3D files.

## Description

EditorSceneFormatImporter allows to define an importer script for a third-
party 3D format.

To use EditorSceneFormatImporter, register it using the
EditorPlugin.add_scene_format_importer_plugin() method first.

## Methods

PackedStringArray | _get_extensions() virtual const  
---|---  
void | _get_import_options(path: String) virtual  
Variant | _get_option_visibility(path: String, for_animation: bool, option: String) virtual const  
Object | _import_scene(path: String, flags: int, options: Dictionary) virtual  
void | add_import_option(name: String, value: Variant)  
void | add_import_option_advanced(type: Variant.Type, name: String, default_value: Variant, hint: PropertyHint = 0, hint_string: String = "", usage_flags: int = 6)  
  
## Constants

IMPORT_SCENE = `1`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_ANIMATION = `2`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_FAIL_ON_MISSING_DEPENDENCIES = `4`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_GENERATE_TANGENT_ARRAYS = `8`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_USE_NAMED_SKIN_BINDS = `16`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_DISCARD_MESHES_AND_MATERIALS = `32`

There is currently no description for this constant. Please help us by
contributing one!

IMPORT_FORCE_DISABLE_MESH_COMPRESSION = `64`

There is currently no description for this constant. Please help us by
contributing one!

## Method Descriptions

PackedStringArray _get_extensions() virtual const

Return supported file extensions for this scene importer.

void _get_import_options(path: String) virtual

Override to add general import options. These will appear in the main import
dock on the editor. Add options via add_import_option() and
add_import_option_advanced().

Note: All EditorSceneFormatImporter and EditorScenePostImportPlugin instances
will add options for all files. It is good practice to check the file
extension when `path` is non-empty.

When the user is editing project settings, `path` will be empty. It is
recommended to add all options when `path` is empty to allow the user to
customize Import Defaults.

Variant _get_option_visibility(path: String, for_animation: bool, option:
String) virtual const

Should return `true` to show the given option, `false` to hide the given
option, or `null` to ignore.

Object _import_scene(path: String, flags: int, options: Dictionary) virtual

Perform the bulk of the scene import logic here, for example using
GLTFDocument or FBXDocument.

void add_import_option(name: String, value: Variant)

Add a specific import option (name and default value only). This function can
only be called from _get_import_options().

void add_import_option_advanced(type: Variant.Type, name: String,
default_value: Variant, hint: PropertyHint = 0, hint_string: String = "",
usage_flags: int = 6)

Add a specific import option. This function can only be called from
_get_import_options().

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

