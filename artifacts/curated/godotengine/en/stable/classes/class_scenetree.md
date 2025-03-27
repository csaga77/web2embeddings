# SceneTree

Inherits: MainLoop < Object

Manages the game loop via a hierarchy of nodes.

## Description

As one of the most important classes, the SceneTree manages the hierarchy of
nodes in a scene, as well as scenes themselves. Nodes can be added, fetched
and removed. The whole scene tree (and thus the current scene) can be paused.
Scenes can be loaded, switched and reloaded.

You can also use the SceneTree to organize your nodes into groups: every node
can be added to as many groups as you want to create, e.g. an "enemy" group.
You can then iterate these groups or even call methods and set properties on
all the nodes belonging to any given group.

SceneTree is the default MainLoop implementation used by the engine, and is
thus in charge of the game loop.

## Tutorials

  * SceneTree

  * Multiple resolutions

## Properties

bool | auto_accept_quit | `true`  
---|---|---  
Node | current_scene  
bool | debug_collisions_hint | `false`  
bool | debug_navigation_hint | `false`  
bool | debug_paths_hint | `false`  
Node | edited_scene_root  
bool | multiplayer_poll | `true`  
bool | paused | `false`  
bool | physics_interpolation | `false`  
bool | quit_on_go_back | `true`  
Window | root  
  
## Methods

void | call_group(group: StringName, method: StringName, ...) vararg  
---|---  
void | call_group_flags(flags: int, group: StringName, method: StringName, ...) vararg  
Error | change_scene_to_file(path: String)  
Error | change_scene_to_packed(packed_scene: PackedScene)  
SceneTreeTimer | create_timer(time_sec: float, process_always: bool = true, process_in_physics: bool = false, ignore_time_scale: bool = false)  
Tween | create_tween()  
Node | get_first_node_in_group(group: StringName)  
int | get_frame() const  
MultiplayerAPI | get_multiplayer(for_path: NodePath = NodePath("")) const  
int | get_node_count() const  
int | get_node_count_in_group(group: StringName) const  
Array[Node] | get_nodes_in_group(group: StringName)  
Array[Tween] | get_processed_tweens()  
bool | has_group(name: StringName) const  
void | notify_group(group: StringName, notification: int)  
void | notify_group_flags(call_flags: int, group: StringName, notification: int)  
void | queue_delete(obj: Object)  
void | quit(exit_code: int = 0)  
Error | reload_current_scene()  
void | set_group(group: StringName, property: String, value: Variant)  
void | set_group_flags(call_flags: int, group: StringName, property: String, value: Variant)  
void | set_multiplayer(multiplayer: MultiplayerAPI, root_path: NodePath = NodePath(""))  
void | unload_current_scene()  
  
## Signals

node_added(node: Node)

Emitted when the `node` enters this tree.

node_configuration_warning_changed(node: Node)

Emitted when the `node`'s Node.update_configuration_warnings() is called. Only
emitted in the editor.

node_removed(node: Node)

Emitted when the `node` exits this tree.

node_renamed(node: Node)

Emitted when the `node`'s Node.name is changed.

physics_frame()

Emitted immediately before Node._physics_process() is called on every node in
this tree.

process_frame()

Emitted immediately before Node._process() is called on every node in this
tree.

tree_changed()

Emitted any time the tree's hierarchy changes (nodes being moved, renamed,
etc.).

tree_process_mode_changed()

Emitted when the Node.process_mode of any node inside the tree is changed.
Only emitted in the editor, to update the visibility of disabled nodes.

## Enumerations

enum GroupCallFlags:

GroupCallFlags GROUP_CALL_DEFAULT = `0`

Call nodes within a group with no special behavior (default).

GroupCallFlags GROUP_CALL_REVERSE = `1`

Call nodes within a group in reverse tree hierarchy order (all nested children
are called before their respective parent nodes).

GroupCallFlags GROUP_CALL_DEFERRED = `2`

Call nodes within a group at the end of the current frame (can be either
process or physics frame), similar to Object.call_deferred().

GroupCallFlags GROUP_CALL_UNIQUE = `4`

Call nodes within a group only once, even if the call is executed many times
in the same frame. Must be combined with GROUP_CALL_DEFERRED to work.

Note: Different arguments are not taken into account. Therefore, when the same
call is executed with different arguments, only the first call will be
performed.

## Property Descriptions

bool auto_accept_quit = `true`

  * void set_auto_accept_quit(value: bool)

  * bool is_auto_accept_quit()

If `true`, the application automatically accepts quitting requests.

For mobile platforms, see quit_on_go_back.

Node current_scene

  * void set_current_scene(value: Node)

  * Node get_current_scene()

The root node of the currently loaded main scene, usually as a direct child of
root. See also change_scene_to_file(), change_scene_to_packed(), and
reload_current_scene().

Warning: Setting this property directly may not work as expected, as it does
not add or remove any nodes from this tree.

bool debug_collisions_hint = `false`

  * void set_debug_collisions_hint(value: bool)

  * bool is_debugging_collisions_hint()

If `true`, collision shapes will be visible when running the game from the
editor for debugging purposes.

Note: This property is not designed to be changed at run-time. Changing the
value of debug_collisions_hint while the project is running will not have the
desired effect.

bool debug_navigation_hint = `false`

  * void set_debug_navigation_hint(value: bool)

  * bool is_debugging_navigation_hint()

If `true`, navigation polygons will be visible when running the game from the
editor for debugging purposes.

Note: This property is not designed to be changed at run-time. Changing the
value of debug_navigation_hint while the project is running will not have the
desired effect.

bool debug_paths_hint = `false`

  * void set_debug_paths_hint(value: bool)

  * bool is_debugging_paths_hint()

If `true`, curves from Path2D and Path3D nodes will be visible when running
the game from the editor for debugging purposes.

Note: This property is not designed to be changed at run-time. Changing the
value of debug_paths_hint while the project is running will not have the
desired effect.

Node edited_scene_root

  * void set_edited_scene_root(value: Node)

  * Node get_edited_scene_root()

The root of the scene currently being edited in the editor. This is usually a
direct child of root.

Note: This property does nothing in release builds.

bool multiplayer_poll = `true`

  * void set_multiplayer_poll_enabled(value: bool)

  * bool is_multiplayer_poll_enabled()

If `true` (default value), enables automatic polling of the MultiplayerAPI for
this SceneTree during process_frame.

If `false`, you need to manually call MultiplayerAPI.poll() to process network
packets and deliver RPCs. This allows running RPCs in a different loop (e.g.
physics, thread, specific time step) and for manual Mutex protection when
accessing the MultiplayerAPI from threads.

bool paused = `false`

  * void set_pause(value: bool)

  * bool is_paused()

If `true`, the scene tree is considered paused. This causes the following
behavior:

  * 2D and 3D physics will be stopped, as well as collision detection and related signals.

  * Depending on each node's Node.process_mode, their Node._process(), Node._physics_process() and Node._input() callback methods may not called anymore.

bool physics_interpolation = `false`

  * void set_physics_interpolation_enabled(value: bool)

  * bool is_physics_interpolation_enabled()

If `true`, the renderer will interpolate the transforms of physics objects
between the last two transforms, so that smooth motion is seen even when
physics ticks do not coincide with rendered frames.

The default value of this property is controlled by
ProjectSettings.physics/common/physics_interpolation.

bool quit_on_go_back = `true`

  * void set_quit_on_go_back(value: bool)

  * bool is_quit_on_go_back()

If `true`, the application quits automatically when navigating back (e.g.
using the system "Back" button on Android).

To handle 'Go Back' button when this option is disabled, use
DisplayServer.WINDOW_EVENT_GO_BACK_REQUEST.

Window root

  * Window get_root()

The tree's root Window. This is top-most Node of the scene tree, and is always
present. An absolute NodePath always starts from this node. Children of the
root node may include the loaded current_scene, as well as any AutoLoad
configured in the Project Settings.

Warning: Do not delete this node. This will result in unstable behavior,
followed by a crash.

## Method Descriptions

void call_group(group: StringName, method: StringName, ...) vararg

Calls `method` on each node inside this tree added to the given `group`. You
can pass arguments to `method` by specifying them at the end of this method
call. Nodes that cannot call `method` (either because the method doesn't exist
or the arguments do not match) are ignored. See also set_group() and
notify_group().

Note: This method acts immediately on all selected nodes at once, which may
cause stuttering in some performance-intensive situations.

Note: In C#, `method` must be in snake_case when referring to built-in Godot
methods. Prefer using the names exposed in the `MethodName` class to avoid
allocating a new StringName on each call.

void call_group_flags(flags: int, group: StringName, method: StringName, ...)
vararg

Calls the given `method` on each node inside this tree added to the given
`group`. Use `flags` to customize this method's behavior (see GroupCallFlags).
Additional arguments for `method` can be passed at the end of this method.
Nodes that cannot call `method` (either because the method doesn't exist or
the arguments do not match) are ignored.

    
    
    # Calls "hide" to all nodes of the "enemies" group, at the end of the frame and in reverse tree order.
    get_tree().call_group_flags(
            SceneTree.GROUP_CALL_DEFERRED | SceneTree.GROUP_CALL_REVERSE,
            "enemies", "hide")
    

Note: In C#, `method` must be in snake_case when referring to built-in Godot
methods. Prefer using the names exposed in the `MethodName` class to avoid
allocating a new StringName on each call.

Error change_scene_to_file(path: String)

Changes the running scene to the one at the given `path`, after loading it
into a PackedScene and creating a new instance.

Returns @GlobalScope.OK on success, @GlobalScope.ERR_CANT_OPEN if the `path`
cannot be loaded into a PackedScene, or @GlobalScope.ERR_CANT_CREATE if that
scene cannot be instantiated.

Note: See change_scene_to_packed() for details on the order of operations.

Error change_scene_to_packed(packed_scene: PackedScene)

Changes the running scene to a new instance of the given PackedScene (which
must be valid).

Returns @GlobalScope.OK on success, @GlobalScope.ERR_CANT_CREATE if the scene
cannot be instantiated, or @GlobalScope.ERR_INVALID_PARAMETER if the scene is
invalid.

Note: Operations happen in the following order when change_scene_to_packed()
is called:

  1. The current scene node is immediately removed from the tree. From that point, Node.get_tree() called on the current (outgoing) scene will return `null`. current_scene will be `null`, too, because the new scene is not available yet.

  2. At the end of the frame, the formerly current scene, already removed from the tree, will be deleted (freed from memory) and then the new scene will be instantiated and added to the tree. Node.get_tree() and current_scene will be back to working as usual.

This ensures that both scenes aren't running at the same time, while still
freeing the previous scene in a safe way similar to Node.queue_free().

SceneTreeTimer create_timer(time_sec: float, process_always: bool = true,
process_in_physics: bool = false, ignore_time_scale: bool = false)

Returns a new SceneTreeTimer. After `time_sec` in seconds have passed, the
timer will emit SceneTreeTimer.timeout and will be automatically freed.

If `process_always` is `false`, the timer will be paused when setting paused
to `true`.

If `process_in_physics` is `true`, the timer will update at the end of the
physics frame, instead of the process frame.

If `ignore_time_scale` is `true`, the timer will ignore Engine.time_scale and
update with the real, elapsed time.

This method is commonly used to create a one-shot delay timer, as in the
following example:

GDScriptC#

    
    
    func some_function():
        print("start")
        await get_tree().create_timer(1.0).timeout
        print("end")
    
    
    
    public async Task SomeFunction()
    {
        GD.Print("start");
        await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
        GD.Print("end");
    }
    

Note: The timer is always updated after all of the nodes in the tree. A node's
Node._process() method would be called before the timer updates (or
Node._physics_process() if `process_in_physics` is set to `true`).

Tween create_tween()

Creates and returns a new Tween processed in this tree. The Tween will start
automatically on the next process frame or physics frame (depending on its
TweenProcessMode).

Note: A Tween created using this method is not bound to any Node. It may keep
working until there is nothing left to animate. If you want the Tween to be
automatically killed when the Node is freed, use Node.create_tween() or
Tween.bind_node().

Node get_first_node_in_group(group: StringName)

Returns the first Node found inside the tree, that has been added to the given
`group`, in scene hierarchy order. Returns `null` if no match is found. See
also get_nodes_in_group().

int get_frame() const

Returns how many frames have been processed, since the application started.
This is not a measurement of elapsed time.

MultiplayerAPI get_multiplayer(for_path: NodePath = NodePath("")) const

Searches for the MultiplayerAPI configured for the given path, if one does not
exist it searches the parent paths until one is found. If the path is empty,
or none is found, the default one is returned. See set_multiplayer().

int get_node_count() const

Returns the number of nodes inside this tree.

int get_node_count_in_group(group: StringName) const

Returns the number of nodes assigned to the given group.

Array[Node] get_nodes_in_group(group: StringName)

Returns an Array containing all nodes inside this tree, that have been added
to the given `group`, in scene hierarchy order.

Array[Tween] get_processed_tweens()

Returns an Array of currently existing Tweens in the tree, including paused
tweens.

bool has_group(name: StringName) const

Returns `true` if a node added to the given group `name` exists in the tree.

void notify_group(group: StringName, notification: int)

Calls Object.notification() with the given `notification` to all nodes inside
this tree added to the `group`. See also Godot notifications and call_group()
and set_group().

Note: This method acts immediately on all selected nodes at once, which may
cause stuttering in some performance-intensive situations.

void notify_group_flags(call_flags: int, group: StringName, notification: int)

Calls Object.notification() with the given `notification` to all nodes inside
this tree added to the `group`. Use `call_flags` to customize this method's
behavior (see GroupCallFlags).

void queue_delete(obj: Object)

Queues the given `obj` to be deleted, calling its Object.free() at the end of
the current frame. This method is similar to Node.queue_free().

void quit(exit_code: int = 0)

Quits the application at the end of the current iteration, with the given
`exit_code`.

By convention, an exit code of `0` indicates success, whereas any other exit
code indicates an error. For portability reasons, it should be between `0` and
`125` (inclusive).

Note: On iOS this method doesn't work. Instead, as recommended by the iOS
Human Interface Guidelines, the user is expected to close apps via the Home
button.

Error reload_current_scene()

Reloads the currently active scene, replacing current_scene with a new
instance of its original PackedScene.

Returns @GlobalScope.OK on success, @GlobalScope.ERR_UNCONFIGURED if no
current_scene is defined, @GlobalScope.ERR_CANT_OPEN if current_scene cannot
be loaded into a PackedScene, or @GlobalScope.ERR_CANT_CREATE if the scene
cannot be instantiated.

void set_group(group: StringName, property: String, value: Variant)

Sets the given `property` to `value` on all nodes inside this tree added to
the given `group`. Nodes that do not have the `property` are ignored. See also
call_group() and notify_group().

Note: This method acts immediately on all selected nodes at once, which may
cause stuttering in some performance-intensive situations.

Note: In C#, `property` must be in snake_case when referring to built-in Godot
properties. Prefer using the names exposed in the `PropertyName` class to
avoid allocating a new StringName on each call.

void set_group_flags(call_flags: int, group: StringName, property: String,
value: Variant)

Sets the given `property` to `value` on all nodes inside this tree added to
the given `group`. Nodes that do not have the `property` are ignored. Use
`call_flags` to customize this method's behavior (see GroupCallFlags).

Note: In C#, `property` must be in snake_case when referring to built-in Godot
properties. Prefer using the names exposed in the `PropertyName` class to
avoid allocating a new StringName on each call.

void set_multiplayer(multiplayer: MultiplayerAPI, root_path: NodePath =
NodePath(""))

Sets a custom MultiplayerAPI with the given `root_path` (controlling also the
relative subpaths), or override the default one if `root_path` is empty.

Note: No MultiplayerAPI must be configured for the subpath containing
`root_path`, nested custom multiplayers are not allowed. I.e. if one is
configured for `"/root/Foo"` setting one for `"/root/Foo/Bar"` will cause an
error.

void unload_current_scene()

If a current scene is loaded, calling this method will unload it.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[vararg]: This method accepts any number of arguments after the ones described here.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

