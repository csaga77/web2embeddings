# Node3D

Inherits: Node < Object

Inherited By: AudioListener3D, AudioStreamPlayer3D, BoneAttachment3D,
Camera3D, CollisionObject3D, CollisionPolygon3D, CollisionShape3D, GridMap,
ImporterMeshInstance3D, Joint3D, LightmapProbe, Marker3D, NavigationLink3D,
NavigationObstacle3D, NavigationRegion3D, OpenXRCompositionLayer, OpenXRHand,
Path3D, PathFollow3D, RayCast3D, RemoteTransform3D, ShapeCast3D, Skeleton3D,
SkeletonModifier3D, SpringArm3D, SpringBoneCollision3D, VehicleWheel3D,
VisualInstance3D, XRFaceModifier3D, XRNode3D, XROrigin3D

Most basic 3D game object, parent of all 3D-related nodes.

## Description

Most basic 3D game object, with a Transform3D and visibility settings. All
other 3D game objects inherit from Node3D. Use Node3D as a parent node to
move, scale, rotate and show/hide children in a 3D project.

Affine operations (rotate, scale, translate) happen in parent's local
coordinate system, unless the Node3D object is set as top-level. Affine
operations in this coordinate system correspond to direct affine operations on
the Node3D's transform. The word local below refers to this coordinate system.
The coordinate system that is attached to the Node3D object itself is referred
to as object-local coordinate system.

Note: Unless otherwise specified, all methods that have angle parameters must
have angles specified as radians. To convert degrees to radians, use
@GlobalScope.deg_to_rad().

Note: Be aware that "Spatial" nodes are now called "Node3D" starting with
Godot 4. Any Godot 3.x references to "Spatial" nodes refer to "Node3D" in
Godot 4.

## Tutorials

  * Introduction to 3D

  * All 3D Demos

## Properties

Basis | basis  
---|---  
Basis | global_basis  
Vector3 | global_position  
Vector3 | global_rotation  
Vector3 | global_rotation_degrees  
Transform3D | global_transform  
Vector3 | position | `Vector3(0, 0, 0)`  
Quaternion | quaternion  
Vector3 | rotation | `Vector3(0, 0, 0)`  
Vector3 | rotation_degrees  
RotationEditMode | rotation_edit_mode | `0`  
EulerOrder | rotation_order | `2`  
Vector3 | scale | `Vector3(1, 1, 1)`  
bool | top_level | `false`  
Transform3D | transform | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`  
NodePath | visibility_parent | `NodePath("")`  
bool | visible | `true`  
  
## Methods

void | add_gizmo(gizmo: Node3DGizmo)  
---|---  
void | clear_gizmos()  
void | clear_subgizmo_selection()  
void | force_update_transform()  
Array[Node3DGizmo] | get_gizmos() const  
Transform3D | get_global_transform_interpolated()  
Node3D | get_parent_node_3d() const  
World3D | get_world_3d() const  
void | global_rotate(axis: Vector3, angle: float)  
void | global_scale(scale: Vector3)  
void | global_translate(offset: Vector3)  
void | hide()  
bool | is_local_transform_notification_enabled() const  
bool | is_scale_disabled() const  
bool | is_transform_notification_enabled() const  
bool | is_visible_in_tree() const  
void | look_at(target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false)  
void | look_at_from_position(position: Vector3, target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front: bool = false)  
void | orthonormalize()  
void | rotate(axis: Vector3, angle: float)  
void | rotate_object_local(axis: Vector3, angle: float)  
void | rotate_x(angle: float)  
void | rotate_y(angle: float)  
void | rotate_z(angle: float)  
void | scale_object_local(scale: Vector3)  
void | set_disable_scale(disable: bool)  
void | set_identity()  
void | set_ignore_transform_notification(enabled: bool)  
void | set_notify_local_transform(enable: bool)  
void | set_notify_transform(enable: bool)  
void | set_subgizmo_selection(gizmo: Node3DGizmo, id: int, transform: Transform3D)  
void | show()  
Vector3 | to_global(local_point: Vector3) const  
Vector3 | to_local(global_point: Vector3) const  
void | translate(offset: Vector3)  
void | translate_object_local(offset: Vector3)  
void | update_gizmos()  
  
## Signals

visibility_changed()

Emitted when node visibility changes.

## Enumerations

enum RotationEditMode:

RotationEditMode ROTATION_EDIT_MODE_EULER = `0`

The rotation is edited using Vector3 Euler angles.

RotationEditMode ROTATION_EDIT_MODE_QUATERNION = `1`

The rotation is edited using a Quaternion.

RotationEditMode ROTATION_EDIT_MODE_BASIS = `2`

The rotation is edited using a Basis. In this mode, scale can't be edited
separately.

## Constants

NOTIFICATION_TRANSFORM_CHANGED = `2000`

Node3D nodes receive this notification when their global transform changes.
This means that either the current or a parent node changed its transform.

In order for NOTIFICATION_TRANSFORM_CHANGED to work, users first need to ask
for it, with set_notify_transform(). The notification is also sent if the node
is in the editor context and it has at least one valid gizmo.

NOTIFICATION_ENTER_WORLD = `41`

Node3D nodes receive this notification when they are registered to new World3D
resource.

NOTIFICATION_EXIT_WORLD = `42`

Node3D nodes receive this notification when they are unregistered from current
World3D resource.

NOTIFICATION_VISIBILITY_CHANGED = `43`

Node3D nodes receive this notification when their visibility changes.

NOTIFICATION_LOCAL_TRANSFORM_CHANGED = `44`

Node3D nodes receive this notification when their local transform changes.
This is not received when the transform of a parent node is changed.

In order for NOTIFICATION_LOCAL_TRANSFORM_CHANGED to work, users first need to
ask for it, with set_notify_local_transform().

## Property Descriptions

Basis basis

  * void set_basis(value: Basis)

  * Basis get_basis()

Basis of the transform property. Represents the rotation, scale, and shear of
this node.

Basis global_basis

  * void set_global_basis(value: Basis)

  * Basis get_global_basis()

Global basis of this node. This is equivalent to `global_transform.basis`.

Vector3 global_position

  * void set_global_position(value: Vector3)

  * Vector3 get_global_position()

Global position of this node. This is equivalent to `global_transform.origin`.

Vector3 global_rotation

  * void set_global_rotation(value: Vector3)

  * Vector3 get_global_rotation()

Rotation part of the global transformation in radians, specified in terms of
YXZ-Euler angles in the format (X angle, Y angle, Z angle).

Note: In the mathematical sense, rotation is a matrix and not a vector. The
three Euler angles, which are the three independent parameters of the Euler-
angle parametrization of the rotation matrix, are stored in a Vector3 data
structure not because the rotation is a vector, but only because Vector3
exists as a convenient data-structure to store 3 floating-point numbers.
Therefore, applying affine operations on the rotation "vector" is not
meaningful.

Vector3 global_rotation_degrees

  * void set_global_rotation_degrees(value: Vector3)

  * Vector3 get_global_rotation_degrees()

Helper property to access global_rotation in degrees instead of radians.

Transform3D global_transform

  * void set_global_transform(value: Transform3D)

  * Transform3D get_global_transform()

World3D space (global) Transform3D of this node.

Vector3 position = `Vector3(0, 0, 0)`

  * void set_position(value: Vector3)

  * Vector3 get_position()

Local position or translation of this node relative to the parent. This is
equivalent to `transform.origin`.

Quaternion quaternion

  * void set_quaternion(value: Quaternion)

  * Quaternion get_quaternion()

Access to the node rotation as a Quaternion. This property is ideal for
tweening complex rotations.

Vector3 rotation = `Vector3(0, 0, 0)`

  * void set_rotation(value: Vector3)

  * Vector3 get_rotation()

Rotation part of the local transformation in radians, specified in terms of
Euler angles. The angles construct a rotation in the order specified by the
rotation_order property.

Note: In the mathematical sense, rotation is a matrix and not a vector. The
three Euler angles, which are the three independent parameters of the Euler-
angle parametrization of the rotation matrix, are stored in a Vector3 data
structure not because the rotation is a vector, but only because Vector3
exists as a convenient data-structure to store 3 floating-point numbers.
Therefore, applying affine operations on the rotation "vector" is not
meaningful.

Note: This property is edited in the inspector in degrees. If you want to use
degrees in a script, use rotation_degrees.

Vector3 rotation_degrees

  * void set_rotation_degrees(value: Vector3)

  * Vector3 get_rotation_degrees()

Helper property to access rotation in degrees instead of radians.

RotationEditMode rotation_edit_mode = `0`

  * void set_rotation_edit_mode(value: RotationEditMode)

  * RotationEditMode get_rotation_edit_mode()

Specify how rotation (and scale) will be presented in the editor.

EulerOrder rotation_order = `2`

  * void set_rotation_order(value: EulerOrder)

  * EulerOrder get_rotation_order()

Specify the axis rotation order of the rotation property. The final
orientation is constructed by rotating the Euler angles in the order specified
by this property.

Vector3 scale = `Vector3(1, 1, 1)`

  * void set_scale(value: Vector3)

  * Vector3 get_scale()

Scale part of the local transformation.

Note: Mixed negative scales in 3D are not decomposable from the transformation
matrix. Due to the way scale is represented with transformation matrices in
Godot, the scale values will either be all positive or all negative.

Note: Not all nodes are visually scaled by the scale property. For example,
Light3Ds are not visually affected by scale.

bool top_level = `false`

  * void set_as_top_level(value: bool)

  * bool is_set_as_top_level()

If `true`, the node will not inherit its transformations from its parent. Node
transformations are only in global space.

Transform3D transform = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

  * void set_transform(value: Transform3D)

  * Transform3D get_transform()

Local space Transform3D of this node, with respect to the parent node.

NodePath visibility_parent = `NodePath("")`

  * void set_visibility_parent(value: NodePath)

  * NodePath get_visibility_parent()

Defines the visibility range parent for this node and its subtree. The
visibility parent must be a GeometryInstance3D. Any visual instance will only
be visible if the visibility parent (and all of its visibility ancestors) is
hidden by being closer to the camera than its own
GeometryInstance3D.visibility_range_begin. Nodes hidden via the visible
property are essentially removed from the visibility dependency tree, so
dependent instances will not take the hidden node or its ancestors into
account.

bool visible = `true`

  * void set_visible(value: bool)

  * bool is_visible()

If `true`, this node is drawn. The node is only visible if all of its
ancestors are visible as well (in other words, is_visible_in_tree() must
return `true`).

## Method Descriptions

void add_gizmo(gizmo: Node3DGizmo)

Attach an editor gizmo to this Node3D.

Note: The gizmo object would typically be an instance of EditorNode3DGizmo,
but the argument type is kept generic to avoid creating a dependency on editor
classes in Node3D.

void clear_gizmos()

Clear all gizmos attached to this Node3D.

void clear_subgizmo_selection()

Clears subgizmo selection for this node in the editor. Useful when subgizmo
IDs become invalid after a property change.

void force_update_transform()

Forces the transform to update. Transform changes in physics are not instant
for performance reasons. Transforms are accumulated and then set. Use this if
you need an up-to-date transform when doing physics operations.

Array[Node3DGizmo] get_gizmos() const

Returns all the gizmos attached to this Node3D.

Transform3D get_global_transform_interpolated()

When using physics interpolation, there will be circumstances in which you
want to know the interpolated (displayed) transform of a node rather than the
standard transform (which may only be accurate to the most recent physics
tick).

This is particularly important for frame-based operations that take place in
Node._process(), rather than Node._physics_process(). Examples include
Camera3Ds focusing on a node, or finding where to fire lasers from on a frame
rather than physics tick.

Note: This function creates an interpolation pump on the Node3D the first time
it is called, which can respond to physics interpolation resets. If you get
problems with "streaking" when initially following a Node3D, be sure to call
get_global_transform_interpolated() at least once before resetting the Node3D
physics interpolation.

Node3D get_parent_node_3d() const

Returns the parent Node3D, or `null` if no parent exists, the parent is not of
type Node3D, or top_level is `true`.

Note: Calling this method is not equivalent to `get_parent() as Node3D`, which
does not take top_level into account.

World3D get_world_3d() const

Returns the current World3D resource this Node3D node is registered to.

void global_rotate(axis: Vector3, angle: float)

Rotates the global (world) transformation around axis, a unit Vector3, by
specified angle in radians. The rotation axis is in global coordinate system.

void global_scale(scale: Vector3)

Scales the global (world) transformation by the given Vector3 scale factors.

void global_translate(offset: Vector3)

Moves the global (world) transformation by Vector3 offset. The offset is in
global coordinate system.

void hide()

Disables rendering of this node. Changes visible to `false`.

bool is_local_transform_notification_enabled() const

Returns whether node notifies about its local transformation changes. Node3D
will not propagate this by default.

bool is_scale_disabled() const

Returns whether this node uses a scale of `(1, 1, 1)` or its local
transformation scale.

bool is_transform_notification_enabled() const

Returns whether the node notifies about its global and local transformation
changes. Node3D will not propagate this by default.

bool is_visible_in_tree() const

Returns `true` if the node is present in the SceneTree, its visible property
is `true` and all its ancestors are also visible. If any ancestor is hidden,
this node will not be visible in the scene tree.

Visibility is checked only in parent nodes that inherit from Node3D. If the
parent is of any other type (such as Node, AnimationPlayer, or Node2D), it is
assumed to be visible.

Note: This method does not take VisualInstance3D.layers into account, so even
if this method returns `true`, the node might end up not being rendered.

void look_at(target: Vector3, up: Vector3 = Vector3(0, 1, 0), use_model_front:
bool = false)

Rotates the node so that the local forward axis (-Z, Vector3.FORWARD) points
toward the `target` position.

The local up axis (+Y) points as close to the `up` vector as possible while
staying perpendicular to the local forward axis. The resulting transform is
orthogonal, and the scale is preserved. Non-uniform scaling may not work
correctly.

The `target` position cannot be the same as the node's position, the `up`
vector cannot be zero.

The `target` and the `up` cannot be Vector3.ZERO, and shouldn't be colinear to
avoid unintended rotation around local Z axis.

Operations take place in global space, which means that the node must be in
the scene tree.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as
forward (implies +X is left) and points toward the `target` position. By
default, the -Z axis (camera forward) is treated as forward (implies +X is
right).

void look_at_from_position(position: Vector3, target: Vector3, up: Vector3 =
Vector3(0, 1, 0), use_model_front: bool = false)

Moves the node to the specified `position`, and then rotates the node to point
toward the `target` as per look_at(). Operations take place in global space.

void orthonormalize()

Resets this node's transformations (like scale, skew and taper) preserving its
rotation and translation by performing Gram-Schmidt orthonormalization on this
node's Transform3D.

void rotate(axis: Vector3, angle: float)

Rotates the local transformation around axis, a unit Vector3, by specified
angle in radians.

void rotate_object_local(axis: Vector3, angle: float)

Rotates the local transformation around axis, a unit Vector3, by specified
angle in radians. The rotation axis is in object-local coordinate system.

void rotate_x(angle: float)

Rotates the local transformation around the X axis by angle in radians.

void rotate_y(angle: float)

Rotates the local transformation around the Y axis by angle in radians.

void rotate_z(angle: float)

Rotates the local transformation around the Z axis by angle in radians.

void scale_object_local(scale: Vector3)

Scales the local transformation by given 3D scale factors in object-local
coordinate system.

void set_disable_scale(disable: bool)

Sets whether the node uses a scale of `(1, 1, 1)` or its local transformation
scale. Changes to the local transformation scale are preserved.

void set_identity()

Reset all transformations for this node (sets its Transform3D to the identity
matrix).

void set_ignore_transform_notification(enabled: bool)

Sets whether the node ignores notification that its transformation (global or
local) changed.

void set_notify_local_transform(enable: bool)

Sets whether the node notifies about its local transformation changes. Node3D
will not propagate this by default.

void set_notify_transform(enable: bool)

Sets whether the node notifies about its global and local transformation
changes. Node3D will not propagate this by default, unless it is in the editor
context and it has a valid gizmo.

void set_subgizmo_selection(gizmo: Node3DGizmo, id: int, transform:
Transform3D)

Set subgizmo selection for this node in the editor.

Note: The gizmo object would typically be an instance of EditorNode3DGizmo,
but the argument type is kept generic to avoid creating a dependency on editor
classes in Node3D.

void show()

Enables rendering of this node. Changes visible to `true`.

Vector3 to_global(local_point: Vector3) const

Transforms `local_point` from this node's local space to world space.

Vector3 to_local(global_point: Vector3) const

Transforms `global_point` from world space to this node's local space.

void translate(offset: Vector3)

Changes the node's position by the given offset Vector3.

Note that the translation `offset` is affected by the node's scale, so if
scaled by e.g. `(10, 1, 1)`, a translation by an offset of `(2, 0, 0)` would
actually add 20 (`2 * 10`) to the X coordinate.

void translate_object_local(offset: Vector3)

Changes the node's position by the given offset Vector3 in local space.

void update_gizmos()

Updates all the Node3D gizmos attached to this node.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

