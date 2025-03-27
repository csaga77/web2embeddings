# Resource

Inherits: RefCounted < Object

Inherited By: Animation, AnimationLibrary, AnimationNode,
AnimationNodeStateMachinePlayback, AnimationNodeStateMachineTransition,
AudioBusLayout, AudioEffect, AudioStream, BitMap, BoneMap, ButtonGroup,
CameraAttributes, ColorPalette, Compositor, CompositorEffect, CryptoKey,
Curve, Curve2D, Curve3D, EditorNode3DGizmoPlugin, EditorSettings, Environment,
Font, GDExtension, GLTFAccessor, GLTFAnimation, GLTFBufferView, GLTFCamera,
GLTFDocument, GLTFDocumentExtension, GLTFLight, GLTFMesh, GLTFNode,
GLTFPhysicsBody, GLTFPhysicsShape, GLTFSkeleton, GLTFSkin, GLTFSpecGloss,
GLTFState, GLTFTexture, GLTFTextureSampler, Gradient, Image, ImporterMesh,
InputEvent, JSON, LabelSettings, LightmapGIData, Material, Mesh, MeshLibrary,
MissingResource, MultiMesh, NavigationMesh,
NavigationMeshSourceGeometryData2D, NavigationMeshSourceGeometryData3D,
NavigationPolygon, Noise, Occluder3D, OccluderPolygon2D, OggPacketSequence,
OpenXRAction, OpenXRActionMap, OpenXRActionSet, OpenXRBindingModifier,
OpenXRHapticBase, OpenXRInteractionProfile, OpenXRIPBinding,
PackedDataContainer, PackedScene, PhysicsMaterial, PolygonPathFinder,
RDShaderFile, RDShaderSPIRV, RichTextEffect, SceneReplicationConfig, Script,
Shader, ShaderInclude, Shape2D, Shape3D, Shortcut, SkeletonModification2D,
SkeletonModificationStack2D, SkeletonProfile, Skin, Sky, SpriteFrames,
StyleBox, SyntaxHighlighter, Texture, Theme, TileMapPattern, TileSet,
TileSetSource, Translation, VideoStream, VideoStreamPlayback,
VisualShaderNode, VoxelGIData, World2D, World3D, X509Certificate

Base class for serializable objects.

## Description

Resource is the base class for all Godot-specific resource types, serving
primarily as data containers. Since they inherit from RefCounted, resources
are reference-counted and freed when no longer in use. They can also be nested
within other resources, and saved on disk. PackedScene, one of the most common
Objects in a Godot project, is also a resource, uniquely capable of storing
and instantiating the Nodes it contains as many times as desired.

In GDScript, resources can loaded from disk by their resource_path using
@GDScript.load() or @GDScript.preload().

The engine keeps a global cache of all loaded resources, referenced by paths
(see ResourceLoader.has_cached()). A resource will be cached when loaded for
the first time and removed from cache once all references are released. When a
resource is cached, subsequent loads using its path will return the cached
reference.

Note: In C#, resources will not be freed instantly after they are no longer in
use. Instead, garbage collection will run periodically and will free resources
that are no longer in use. This means that unused resources will remain in
memory for a while before being removed.

## Tutorials

  * Resources

  * When and how to avoid using nodes for everything

## Properties

bool | resource_local_to_scene | `false`  
---|---|---  
String | resource_name | `""`  
String | resource_path | `""`  
String | resource_scene_unique_id  
  
## Methods

RID | _get_rid() virtual const  
---|---  
void | _reset_state() virtual  
void | _set_path_cache(path: String) virtual const  
void | _setup_local_to_scene() virtual  
Resource | duplicate(subresources: bool = false) const  
void | emit_changed()  
String | generate_scene_unique_id() static  
String | get_id_for_path(path: String) const  
Node | get_local_scene() const  
RID | get_rid() const  
bool | is_built_in() const  
void | reset_state()  
void | set_id_for_path(path: String, id: String)  
void | set_path_cache(path: String)  
void | setup_local_to_scene()  
void | take_over_path(path: String)  
  
## Signals

changed()

Emitted when the resource changes, usually when one of its properties is
modified. See also emit_changed().

Note: This signal is not emitted automatically for properties of custom
resources. If necessary, a setter needs to be created to emit the signal.

setup_local_to_scene_requested()

Deprecated: This signal is only emitted when the resource is created. Override
_setup_local_to_scene() instead.

Emitted by a newly duplicated resource with resource_local_to_scene set to
`true`.

## Property Descriptions

bool resource_local_to_scene = `false`

  * void set_local_to_scene(value: bool)

  * bool is_local_to_scene()

If `true`, the resource is duplicated for each instance of all scenes using
it. At run-time, the resource can be modified in one scene without affecting
other instances (see PackedScene.instantiate()).

Note: Changing this property at run-time has no effect on already created
duplicate resources.

String resource_name = `""`

  * void set_name(value: String)

  * String get_name()

An optional name for this resource. When defined, its value is displayed to
represent the resource in the Inspector dock. For built-in scripts, the name
is displayed as part of the tab name in the script editor.

Note: Some resource formats do not support resource names. You can still set
the name in the editor or via code, but it will be lost when the resource is
reloaded. For example, only built-in scripts can have a resource name, while
scripts stored in separate files cannot.

String resource_path = `""`

  * void set_path(value: String)

  * String get_path()

The unique path to this resource. If it has been saved to disk, the value will
be its filepath. If the resource is exclusively contained within a scene, the
value will be the PackedScene's filepath, followed by a unique identifier.

Note: Setting this property manually may fail if a resource with the same path
has already been previously loaded. If necessary, use take_over_path().

String resource_scene_unique_id

  * void set_scene_unique_id(value: String)

  * String get_scene_unique_id()

An unique identifier relative to the this resource's scene. If left empty, the
ID is automatically generated when this resource is saved inside a
PackedScene. If the resource is not inside a scene, this property is empty by
default.

Note: When the PackedScene is saved, if multiple resources in the same scene
use the same ID, only the earliest resource in the scene hierarchy keeps the
original ID. The other resources are assigned new IDs from
generate_scene_unique_id().

Note: Setting this property does not emit the changed signal.

Warning: When setting, the ID must only consist of letters, numbers, and
underscores. Otherwise, it will fail and default to a randomly generated ID.

## Method Descriptions

RID _get_rid() virtual const

Override this method to return a custom RID when get_rid() is called.

void _reset_state() virtual

For resources that use a variable number of properties, either via
Object._validate_property() or Object._get_property_list(), this method should
be implemented to correctly clear the resource's state.

void _set_path_cache(path: String) virtual const

Sets the resource's path to `path` without involving the resource cache.

void _setup_local_to_scene() virtual

Override this method to customize the newly duplicated resource created from
PackedScene.instantiate(), if the original's resource_local_to_scene is set to
`true`.

Example: Set a random `damage` value to every local resource from an
instantiated scene:

    
    
    extends Resource
    
    var damage = 0
    
    func _setup_local_to_scene():
        damage = randi_range(10, 40)
    

Resource duplicate(subresources: bool = false) const

Duplicates this resource, returning a new resource with its `export`ed or
@GlobalScope.PROPERTY_USAGE_STORAGE properties copied from the original.

If `subresources` is `false`, a shallow copy is returned; nested resources
within subresources are not duplicated and are shared with the original
resource (with one exception; see below). If `subresources` is `true`, a deep
copy is returned; nested subresources will be duplicated and are not shared
(with two exceptions; see below).

`subresources` is usually respected, with the following exceptions:

  * Subresource properties with the @GlobalScope.PROPERTY_USAGE_ALWAYS_DUPLICATE flag are always duplicated.

  * Subresource properties with the @GlobalScope.PROPERTY_USAGE_NEVER_DUPLICATE flag are never duplicated.

  * Subresources inside Array and Dictionary properties are never duplicated.

Note: For custom resources, this method will fail if Object._init() has been
defined with required parameters.

void emit_changed()

Emits the changed signal. This method is called automatically for some built-
in resources.

Note: For custom resources, it's recommended to call this method whenever a
meaningful change occurs, such as a modified property. This ensures that
custom Objects depending on the resource are properly updated.

    
    
    var damage:
        set(new_value):
            if damage != new_value:
                damage = new_value
                emit_changed()
    

String generate_scene_unique_id() static

Generates a unique identifier for a resource to be contained inside a
PackedScene, based on the current date, time, and a random value. The returned
string is only composed of letters (`a` to `y`) and numbers (`0` to `8`). See
also resource_scene_unique_id.

String get_id_for_path(path: String) const

Returns the unique identifier for the resource with the given `path` from the
resource cache. If the resource is not loaded and cached, an empty string is
returned.

Note: This method is only implemented when running in an editor context. At
runtime, it returns an empty string.

Node get_local_scene() const

If resource_local_to_scene is set to `true` and the resource has been loaded
from a PackedScene instantiation, returns the root Node of the scene where
this resource is used. Otherwise, returns `null`.

RID get_rid() const

Returns the RID of this resource (or an empty RID). Many resources (such as
Texture2D, Mesh, and so on) are high-level abstractions of resources stored in
a specialized server (DisplayServer, RenderingServer, etc.), so this function
will return the original RID.

bool is_built_in() const

Returns `true` if the resource is built-in (from the engine) or `false` if it
is user-defined.

void reset_state()

For resources that use a variable number of properties, either via
Object._validate_property() or Object._get_property_list(), override
_reset_state() to correctly clear the resource's state.

void set_id_for_path(path: String, id: String)

Sets the unique identifier to `id` for the resource with the given `path` in
the resource cache. If the unique identifier is empty, the cache entry using
`path` is removed if it exists.

Note: This method is only implemented when running in an editor context.

void set_path_cache(path: String)

Sets the resource's path to `path` without involving the resource cache.

void setup_local_to_scene()

Deprecated: This method should only be called internally.

Calls _setup_local_to_scene(). If resource_local_to_scene is set to `true`,
this method is automatically called from PackedScene.instantiate() by the
newly duplicated resource within the scene instance.

void take_over_path(path: String)

Sets the resource_path to `path`, potentially overriding an existing cache
entry for this path. Further attempts to load an overridden resource by path
will instead return this resource.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.
  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.

