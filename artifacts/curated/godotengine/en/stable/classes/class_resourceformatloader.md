# ResourceFormatLoader

Inherits: RefCounted < Object

Loads a specific resource type from a file.

## Description

Godot loads resources in the editor or in exported games using
ResourceFormatLoaders. They are queried automatically via the ResourceLoader
singleton, or when a resource with internal dependencies is loaded. Each file
type may load as a different resource type, so multiple ResourceFormatLoaders
are registered in the engine.

Extending this class allows you to define your own loader. Be sure to respect
the documented return types and values. You should give it a global class name
with `class_name` for it to be registered. Like built-in
ResourceFormatLoaders, it will be called automatically when loading resources
of its handled type(s). You may also implement a ResourceFormatSaver.

Note: You can also extend EditorImportPlugin if the resource type you need
exists but Godot is unable to load its format. Choosing one way over another
depends on if the format is suitable or not for the final exported game. For
example, it's better to import `.png` textures as `.ctex`
(CompressedTexture2D) first, so they can be loaded with better efficiency on
the graphics card.

## Methods

bool | _exists(path: String) virtual const  
---|---  
PackedStringArray | _get_classes_used(path: String) virtual const  
PackedStringArray | _get_dependencies(path: String, add_types: bool) virtual const  
PackedStringArray | _get_recognized_extensions() virtual const  
String | _get_resource_script_class(path: String) virtual const  
String | _get_resource_type(path: String) virtual const  
int | _get_resource_uid(path: String) virtual const  
bool | _handles_type(type: StringName) virtual const  
Variant | _load(path: String, original_path: String, use_sub_threads: bool, cache_mode: int) virtual const  
bool | _recognize_path(path: String, type: StringName) virtual const  
Error | _rename_dependencies(path: String, renames: Dictionary) virtual const  
  
## Enumerations

enum CacheMode:

CacheMode CACHE_MODE_IGNORE = `0`

Neither the main resource (the one requested to be loaded) nor any of its
subresources are retrieved from cache nor stored into it. Dependencies
(external resources) are loaded with CACHE_MODE_REUSE.

CacheMode CACHE_MODE_REUSE = `1`

The main resource (the one requested to be loaded), its subresources, and its
dependencies (external resources) are retrieved from cache if present, instead
of loaded. Those not cached are loaded and then stored into the cache. The
same rules are propagated recursively down the tree of dependencies (external
resources).

CacheMode CACHE_MODE_REPLACE = `2`

Like CACHE_MODE_REUSE, but the cache is checked for the main resource (the one
requested to be loaded) as well as for each of its subresources. Those already
in the cache, as long as the loaded and cached types match, have their data
refreshed from storage into the already existing instances. Otherwise, they
are recreated as completely new objects.

CacheMode CACHE_MODE_IGNORE_DEEP = `3`

Like CACHE_MODE_IGNORE, but propagated recursively down the tree of
dependencies (external resources).

CacheMode CACHE_MODE_REPLACE_DEEP = `4`

Like CACHE_MODE_REPLACE, but propagated recursively down the tree of
dependencies (external resources).

## Method Descriptions

bool _exists(path: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_classes_used(path: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_dependencies(path: String, add_types: bool) virtual
const

If implemented, gets the dependencies of a given resource. If `add_types` is
`true`, paths should be appended `::TypeName`, where `TypeName` is the class
name of the dependency.

Note: Custom resource types defined by scripts aren't known by the ClassDB, so
you might just return `"Resource"` for them.

PackedStringArray _get_recognized_extensions() virtual const

Gets the list of extensions for files this loader is able to read.

String _get_resource_script_class(path: String) virtual const

Returns the script class name associated with the Resource under the given
`path`. If the resource has no script or the script isn't a named class, it
should return `""`.

String _get_resource_type(path: String) virtual const

Gets the class name of the resource associated with the given path. If the
loader cannot handle it, it should return `""`.

Note: Custom resource types defined by scripts aren't known by the ClassDB, so
you might just return `"Resource"` for them.

int _get_resource_uid(path: String) virtual const

Should return the unique ID for the resource associated with the given path.
If this method is not overridden, a `.uid` file is generated along with the
resource file, containing the unique ID.

bool _handles_type(type: StringName) virtual const

Tells which resource class this loader can load.

Note: Custom resource types defined by scripts aren't known by the ClassDB, so
you might just handle `"Resource"` for them.

Variant _load(path: String, original_path: String, use_sub_threads: bool,
cache_mode: int) virtual const

Loads a resource when the engine finds this loader to be compatible. If the
loaded resource is the result of an import, `original_path` will target the
source file. Returns a Resource object on success, or an Error constant in
case of failure.

The `cache_mode` property defines whether and how the cache should be used or
updated when loading the resource. See CacheMode for details.

bool _recognize_path(path: String, type: StringName) virtual const

Tells whether or not this loader should load a resource from its resource path
for a given type.

If it is not implemented, the default behavior returns whether the path's
extension is within the ones provided by _get_recognized_extensions(), and if
the type is within the ones provided by _get_resource_type().

Error _rename_dependencies(path: String, renames: Dictionary) virtual const

If implemented, renames dependencies within the given resource and saves it.
`renames` is a dictionary `{ String => String }` mapping old dependency paths
to new paths.

Returns @GlobalScope.OK on success, or an Error constant in case of failure.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

