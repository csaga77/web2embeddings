# Upgrading from Godot 4.3 to Godot 4.4

For most games and apps made with 4.3 it should be relatively safe to migrate
to 4.4. This page intends to cover everything you need to pay attention to
when migrating your project.

## Breaking changes

If you are migrating from 4.3 to 4.4, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and
whether the C# breaking change is binary compatible or source compatible:

  * Binary compatible \- Existing binaries will load and execute successfully without recompilation, and the run-time behavior won't change.

  * Source compatible \- Source code will compile successfully without changes when upgrading Godot.

### Core

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
FileAccess  
Method `open_encrypted` adds a new `iv` optional parameter |  |  |  | GH-98918  
Method `store_8` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_16` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_32` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_64` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_buffer` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_csv_line` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_double` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_float` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_half` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_line` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_pascal_string` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_real` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_string` changes return type from `void` to `bool` |  |  |  | GH-78289  
Method `store_var` changes return type from `void` to `bool` |  |  |  | GH-78289  
OS  
Method `execute_with_pipe` adds a new `blocking` optional parameter |  |  |  | GH-94434  
Method `read_string_from_stdin` adds a new `buffer_size` optional parameter |  |  |  | GH-91201  
RegEx  
Method `compile` adds a new `show_error` optional parameter |  |  |  | GH-95212  
Method `create_from_string` adds a new `show_error` optional parameter |  |  |  | GH-95212  
Semaphore  
Method `post` adds a new `count` optional parameter |  |  |  | GH-93605  
TranslationServer  
Method `standardize_locale` adds a new `add_defaults` optional parameter |  |  |  | GH-98972  
  
### GUI nodes

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
RichTextLabel  
Method `push_meta` adds a new `tooltip` optional parameter |  |  |  | GH-99481  
Method `set_table_column_expand` adds a new `shrink` optional parameter |  |  |  | GH-101482  
GraphEdit  
Method `connect_node` adds a new `keep_alive` optional parameter |  |  |  | GH-97449  
Signal `frame_rect_changed` changes `new_rect` parameter type from `Vector2` to `Rect2` |  |  |  | GH-102796  
  
### Physics

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
SoftBody3D  
Method `set_point_pinned` adds a new `insert_at` optional parameter |  |  |  | GH-94684  
  
### Rendering

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
CPUParticles2D  
Method `restart` adds a new `keep_seed` optional parameter |  |  |  | GH-92089  
CPUParticles3D  
Method `restart` adds a new `keep_seed` optional parameter |  |  |  | GH-92089  
GPUParticles2D  
Method `restart` adds a new `keep_seed` optional parameter |  |  |  | GH-92089  
GPUParticles3D  
Method `restart` adds a new `keep_seed` optional parameter |  |  |  | GH-92089  
RenderingDevice  
Method `draw_list_begin` adds a new `breadcrumb` optional parameter |  |  |  | GH-90993  
Method `draw_list_begin` removes many parameters |  |  |  | GH-98670  
Method `index_buffer_create` adds a new `enable_device_address` optional parameter |  |  |  | GH-100062  
Method `uniform_buffer_create` adds a new `enable_device_address` optional parameter |  |  |  | GH-100062  
Method `vertex_buffer_create` adds a new `enable_device_address` optional parameter |  |  |  | GH-100062  
RenderingServer  
Method `multimesh_allocate_data` adds a new `use_indirect` optional parameter |  |  |  | GH-99455  
Shader  
Method `get_default_texture_parameter` changes return type from `Texture2D` to `Texture` |  |  |  | GH-95126  
Method `set_default_texture_parameter` changes `texture` parameter type from `Texture2D` to `Texture` |  |  |  | GH-95126  
VisualShaderNodeCubemap  
Property `cube_map` changes type from `Cubemap` to `TextureLayered` |  |  |  | GH-95126  
VisualShaderNodeTexture2DArray  
Property `texture_array` changes type from `Texture2DArray` to `TextureLayered` |  |  |  | GH-95126  
  
Note

In C#, the enum `RenderingDevice.StorageBufferUsage` breaks compatibility
because of the way the bindings generator detects the enum prefix. New members
where added in GH-100062 to the enum that caused the enum members to be
renamed.

### Navigation

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
NavigationServer2D  
Method `query_path` adds a new `callback` optional parameter |  |  |  | GH-100129  
NavigationServer3D  
Method `query_path` adds a new `callback` optional parameter |  |  |  | GH-100129  
  
### Editor plugins

Change | GDScript Compatible | C# Binary Compatible | C# Source Compatible | Introduced  
---|---|---|---|---  
EditorInterface  
Method `open_scene_from_path` adds a new `set_inherited` optional parameter |  |  |  | GH-90057  
Method `popup_node_selector` adds a new `current_value` optional parameter |  |  |  | GH-94323  
Method `popup_property_selector` adds a new `current_value` optional parameter |  |  |  | GH-94323  
EditorSceneFormatImporter  
Method `_get_import_flags` removed |  |  |  | GH-101531  
EditorTranslationParserPlugin  
Method `_parse_file` changes return type to `Array` and removes `msgids` and `msgids_context_plural` parameters |  |  |  | GH-99297  
  
Note

The method `_get_import_flags` was never used by the engine. It was removed
despite the compatibility breakage as there's no way for users to rely on this
affecting engine behavior.

## Behavior changes

### Core

Note

The `Curve` resource now enforces its value range, so `min_value` and
`max_value` need to be changed if any of the points fall outside of the
default `[0, 1]` range.

### Rendering

Note

The `VisualShaderNodeVec4Constant` shader node had its input type changed to
`Vector4`. Users need to recreate the values in their constants.

### CSG

Note

The CSG implementation now uses Emmett Lalish's Manifold library (GH-94321).
The new implementation is more consistent with manifold definitions and fixes
a number of bugs and stability issues. As a result, non-manifold meshes are no
longer supported. You can use `MeshInstance3D` for rendering non-manifold
geometry, such as quads or planes.

### Android

Note

Android sensor events are no longer enabled by default (GH-94799). Projects
that use sensor events can enable them as needed in Project Settings under
Input Devices > Sensors.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

