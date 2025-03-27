# SpringBoneSimulator3D

Inherits: SkeletonModifier3D < Node3D < Node < Object

A SkeletonModifier3D to apply inertial wavering to bone chains.

## Description

This SkeletonModifier3D can be used to wiggle hair, cloth, and tails. This
modifier behaves differently from PhysicalBoneSimulator3D as it attempts to
return the original pose after modification.

If you setup set_root_bone() and set_end_bone(), it is treated as one bone
chain. Note that it does not support a branched chain like Y-shaped chains.

When a bone chain is created, an array is generated from the bones that exist
in between and listed in the joint list.

Several properties can be applied to each joint, such as
set_joint_stiffness(), set_joint_drag(), and set_joint_gravity().

For simplicity, you can set values to all joints at the same time by using a
Curve. If you want to specify detailed values individually, set
set_individual_config() to `true`.

For physical simulation, SpringBoneSimulator3D can have children as self-
standing collisions that are not related to PhysicsServer3D, see also
SpringBoneCollision3D.

Warning: A scaled SpringBoneSimulator3D will likely not behave as expected.
Make sure that the parent Skeleton3D and its bones are not scaled.

## Properties

int | setting_count | `0`  
---|---|---  
  
## Methods

bool | are_all_child_collisions_enabled(index: int) const  
---|---  
void | clear_collisions(index: int)  
void | clear_exclude_collisions(index: int)  
void | clear_settings()  
int | get_center_bone(index: int) const  
String | get_center_bone_name(index: int) const  
CenterFrom | get_center_from(index: int) const  
NodePath | get_center_node(index: int) const  
int | get_collision_count(index: int) const  
NodePath | get_collision_path(index: int, collision: int) const  
float | get_drag(index: int) const  
Curve | get_drag_damping_curve(index: int) const  
int | get_end_bone(index: int) const  
BoneDirection | get_end_bone_direction(index: int) const  
float | get_end_bone_length(index: int) const  
String | get_end_bone_name(index: int) const  
int | get_exclude_collision_count(index: int) const  
NodePath | get_exclude_collision_path(index: int, collision: int) const  
float | get_gravity(index: int) const  
Curve | get_gravity_damping_curve(index: int) const  
Vector3 | get_gravity_direction(index: int) const  
int | get_joint_bone(index: int, joint: int) const  
String | get_joint_bone_name(index: int, joint: int) const  
int | get_joint_count(index: int) const  
float | get_joint_drag(index: int, joint: int) const  
float | get_joint_gravity(index: int, joint: int) const  
Vector3 | get_joint_gravity_direction(index: int, joint: int) const  
float | get_joint_radius(index: int, joint: int) const  
RotationAxis | get_joint_rotation_axis(index: int, joint: int) const  
float | get_joint_stiffness(index: int, joint: int) const  
float | get_radius(index: int) const  
Curve | get_radius_damping_curve(index: int) const  
int | get_root_bone(index: int) const  
String | get_root_bone_name(index: int) const  
RotationAxis | get_rotation_axis(index: int) const  
float | get_stiffness(index: int) const  
Curve | get_stiffness_damping_curve(index: int) const  
bool | is_config_individual(index: int) const  
bool | is_end_bone_extended(index: int) const  
void | reset()  
void | set_center_bone(index: int, bone: int)  
void | set_center_bone_name(index: int, bone_name: String)  
void | set_center_from(index: int, center_from: CenterFrom)  
void | set_center_node(index: int, node_path: NodePath)  
void | set_collision_count(index: int, count: int)  
void | set_collision_path(index: int, collision: int, node_path: NodePath)  
void | set_drag(index: int, drag: float)  
void | set_drag_damping_curve(index: int, curve: Curve)  
void | set_enable_all_child_collisions(index: int, enabled: bool)  
void | set_end_bone(index: int, bone: int)  
void | set_end_bone_direction(index: int, bone_direction: BoneDirection)  
void | set_end_bone_length(index: int, length: float)  
void | set_end_bone_name(index: int, bone_name: String)  
void | set_exclude_collision_count(index: int, count: int)  
void | set_exclude_collision_path(index: int, collision: int, node_path: NodePath)  
void | set_extend_end_bone(index: int, enabled: bool)  
void | set_gravity(index: int, gravity: float)  
void | set_gravity_damping_curve(index: int, curve: Curve)  
void | set_gravity_direction(index: int, gravity_direction: Vector3)  
void | set_individual_config(index: int, enabled: bool)  
void | set_joint_drag(index: int, joint: int, drag: float)  
void | set_joint_gravity(index: int, joint: int, gravity: float)  
void | set_joint_gravity_direction(index: int, joint: int, gravity_direction: Vector3)  
void | set_joint_radius(index: int, joint: int, radius: float)  
void | set_joint_rotation_axis(index: int, joint: int, axis: RotationAxis)  
void | set_joint_stiffness(index: int, joint: int, stiffness: float)  
void | set_radius(index: int, radius: float)  
void | set_radius_damping_curve(index: int, curve: Curve)  
void | set_root_bone(index: int, bone: int)  
void | set_root_bone_name(index: int, bone_name: String)  
void | set_rotation_axis(index: int, axis: RotationAxis)  
void | set_stiffness(index: int, stiffness: float)  
void | set_stiffness_damping_curve(index: int, curve: Curve)  
  
## Enumerations

enum BoneDirection:

BoneDirection BONE_DIRECTION_PLUS_X = `0`

Enumerated value for the +X axis.

BoneDirection BONE_DIRECTION_MINUS_X = `1`

Enumerated value for the -X axis.

BoneDirection BONE_DIRECTION_PLUS_Y = `2`

Enumerated value for the +Y axis.

BoneDirection BONE_DIRECTION_MINUS_Y = `3`

Enumerated value for the -Y axis.

BoneDirection BONE_DIRECTION_PLUS_Z = `4`

Enumerated value for the +Z axis.

BoneDirection BONE_DIRECTION_MINUS_Z = `5`

Enumerated value for the -Z axis.

BoneDirection BONE_DIRECTION_FROM_PARENT = `6`

Enumerated value for the axis from a parent bone to the child bone.

enum CenterFrom:

CenterFrom CENTER_FROM_WORLD_ORIGIN = `0`

The world origin is defined as center.

CenterFrom CENTER_FROM_NODE = `1`

The Node3D specified by set_center_node() is defined as center.

If Node3D is not found, the parent Skeleton3D is treated as center.

CenterFrom CENTER_FROM_BONE = `2`

The bone pose origin of the parent Skeleton3D specified by set_center_bone()
is defined as center.

If Node3D is not found, the parent Skeleton3D is treated as center.

enum RotationAxis:

RotationAxis ROTATION_AXIS_X = `0`

Enumerated value for the rotation of the X axis.

RotationAxis ROTATION_AXIS_Y = `1`

Enumerated value for the rotation of the Y axis.

RotationAxis ROTATION_AXIS_Z = `2`

Enumerated value for the rotation of the Z axis.

RotationAxis ROTATION_AXIS_ALL = `3`

Enumerated value for the unconstrained rotation.

## Property Descriptions

int setting_count = `0`

  * void set_setting_count(value: int)

  * int get_setting_count()

The number of settings.

## Method Descriptions

bool are_all_child_collisions_enabled(index: int) const

Returns `true` if the all child SpringBoneCollision3Ds are contained in the
collision list at `index` in the settings.

void clear_collisions(index: int)

Clears all collisions from the collision list at `index` in the settings when
are_all_child_collisions_enabled() is `false`.

void clear_exclude_collisions(index: int)

Clears all exclude collisions from the collision list at `index` in the
settings when are_all_child_collisions_enabled() is `true`.

void clear_settings()

Clears all settings.

int get_center_bone(index: int) const

Returns the center bone index of the bone chain.

String get_center_bone_name(index: int) const

Returns the center bone name of the bone chain.

CenterFrom get_center_from(index: int) const

Returns what the center originates from in the bone chain.

NodePath get_center_node(index: int) const

Returns the center node path of the bone chain.

int get_collision_count(index: int) const

Returns the collision count of the bone chain's collision list when
are_all_child_collisions_enabled() is `false`.

NodePath get_collision_path(index: int, collision: int) const

Returns the node path of the SpringBoneCollision3D at `collision` in the bone
chain's collision list when are_all_child_collisions_enabled() is `false`.

float get_drag(index: int) const

Returns the drag force damping curve of the bone chain.

Curve get_drag_damping_curve(index: int) const

Returns the drag force damping curve of the bone chain.

int get_end_bone(index: int) const

Returns the end bone index of the bone chain.

BoneDirection get_end_bone_direction(index: int) const

Returns the end bone's tail direction of the bone chain when
is_end_bone_extended() is `true`.

float get_end_bone_length(index: int) const

Returns the end bone's tail length of the bone chain when
is_end_bone_extended() is `true`.

String get_end_bone_name(index: int) const

Returns the end bone name of the bone chain.

int get_exclude_collision_count(index: int) const

Returns the exclude collision count of the bone chain's exclude collision list
when are_all_child_collisions_enabled() is `true`.

NodePath get_exclude_collision_path(index: int, collision: int) const

Returns the node path of the SpringBoneCollision3D at `collision` in the bone
chain's exclude collision list when are_all_child_collisions_enabled() is
`true`.

float get_gravity(index: int) const

Returns the gravity amount of the bone chain.

Curve get_gravity_damping_curve(index: int) const

Returns the gravity amount damping curve of the bone chain.

Vector3 get_gravity_direction(index: int) const

Returns the gravity direction of the bone chain.

int get_joint_bone(index: int, joint: int) const

Returns the bone index at `joint` in the bone chain's joint list.

String get_joint_bone_name(index: int, joint: int) const

Returns the bone name at `joint` in the bone chain's joint list.

int get_joint_count(index: int) const

Returns the joint count of the bone chain's joint list.

float get_joint_drag(index: int, joint: int) const

Returns the drag force at `joint` in the bone chain's joint list.

float get_joint_gravity(index: int, joint: int) const

Returns the gravity amount at `joint` in the bone chain's joint list.

Vector3 get_joint_gravity_direction(index: int, joint: int) const

Returns the gravity direction at `joint` in the bone chain's joint list.

float get_joint_radius(index: int, joint: int) const

Returns the radius at `joint` in the bone chain's joint list.

RotationAxis get_joint_rotation_axis(index: int, joint: int) const

Returns the rotation axis at `joint` in the bone chain's joint list.

float get_joint_stiffness(index: int, joint: int) const

Returns the stiffness force at `joint` in the bone chain's joint list.

float get_radius(index: int) const

Returns the joint radius of the bone chain.

Curve get_radius_damping_curve(index: int) const

Returns the joint radius damping curve of the bone chain.

int get_root_bone(index: int) const

Returns the root bone index of the bone chain.

String get_root_bone_name(index: int) const

Returns the root bone name of the bone chain.

RotationAxis get_rotation_axis(index: int) const

Returns the rotation axis of the bone chain.

float get_stiffness(index: int) const

Returns the stiffness force of the bone chain.

Curve get_stiffness_damping_curve(index: int) const

Returns the stiffness force damping curve of the bone chain.

bool is_config_individual(index: int) const

Returns `true` if the config can be edited individually for each joint.

bool is_end_bone_extended(index: int) const

Returns `true` if the end bone is extended to have the tail.

void reset()

Resets a simulating state with respect to the current bone pose.

It is useful to prevent the simulation result getting violent. For example,
calling this immediately after a call to AnimationPlayer.play() without a
fading, or within the previous SkeletonModifier3D.modification_processed
signal if it's condition changes significantly.

void set_center_bone(index: int, bone: int)

Sets the center bone index of the bone chain.

void set_center_bone_name(index: int, bone_name: String)

Sets the center bone name of the bone chain.

void set_center_from(index: int, center_from: CenterFrom)

Sets what the center originates from in the bone chain.

Bone movement is calculated based on the difference in relative distance
between center and bone in the previous and next frames.

For example, if the parent Skeleton3D is used as the center, the bones are
considered to have not moved if the Skeleton3D moves in the world.

In this case, only a change in the bone pose is considered to be a bone
movement.

void set_center_node(index: int, node_path: NodePath)

Sets the center node path of the bone chain.

void set_collision_count(index: int, count: int)

Sets the number of collisions in the collision list at `index` in the settings
when are_all_child_collisions_enabled() is `false`.

void set_collision_path(index: int, collision: int, node_path: NodePath)

Sets the node path of the SpringBoneCollision3D at `collision` in the bone
chain's collision list when are_all_child_collisions_enabled() is `false`.

void set_drag(index: int, drag: float)

Sets the drag force of the bone chain. The greater the value, the more
suppressed the wiggling.

The value is scaled by set_drag_damping_curve() and cached in each joint
setting in the joint list.

void set_drag_damping_curve(index: int, curve: Curve)

Sets the drag force damping curve of the bone chain.

void set_enable_all_child_collisions(index: int, enabled: bool)

If sets `enabled` to `true`, the all child SpringBoneCollision3Ds are collided
and set_exclude_collision_path() is enabled as an exclusion list at `index` in
the settings.

If sets `enabled` to `false`, you need to manually register all valid
collisions with set_collision_path().

void set_end_bone(index: int, bone: int)

Sets the end bone index of the bone chain.

void set_end_bone_direction(index: int, bone_direction: BoneDirection)

Sets the end bone tail direction of the bone chain when is_end_bone_extended()
is `true`.

void set_end_bone_length(index: int, length: float)

Sets the end bone tail length of the bone chain when is_end_bone_extended() is
`true`.

void set_end_bone_name(index: int, bone_name: String)

Sets the end bone name of the bone chain.

Note: End bone must be the root bone or a child of the root bone. If they are
the same, the tail must be extended by set_extend_end_bone() to jiggle the
bone.

void set_exclude_collision_count(index: int, count: int)

Sets the number of exclude collisions in the exclude collision list at `index`
in the settings when are_all_child_collisions_enabled() is `true`.

void set_exclude_collision_path(index: int, collision: int, node_path:
NodePath)

Sets the node path of the SpringBoneCollision3D at `collision` in the bone
chain's exclude collision list when are_all_child_collisions_enabled() is
`true`.

void set_extend_end_bone(index: int, enabled: bool)

If `enabled` is `true`, the end bone is extended to have the tail.

The extended tail config is allocated to the last element in the joint list.

In other words, if you set `enabled` is `false`, the config of last element in
the joint list has no effect in the simulated result.

void set_gravity(index: int, gravity: float)

Sets the gravity amount of the bone chain. This value is not an acceleration,
but a constant velocity of movement in set_gravity_direction().

If `gravity` is not `0`, the modified pose will not return to the original
pose since it is always affected by gravity.

The value is scaled by set_gravity_damping_curve() and cached in each joint
setting in the joint list.

void set_gravity_damping_curve(index: int, curve: Curve)

Sets the gravity amount damping curve of the bone chain.

void set_gravity_direction(index: int, gravity_direction: Vector3)

Sets the gravity direction of the bone chain. This value is internally
normalized and then multiplied by set_gravity().

The value is cached in each joint setting in the joint list.

void set_individual_config(index: int, enabled: bool)

If `enabled` is `true`, the config can be edited individually for each joint.

void set_joint_drag(index: int, joint: int, drag: float)

Sets the drag force at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_joint_gravity(index: int, joint: int, gravity: float)

Sets the gravity amount at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_joint_gravity_direction(index: int, joint: int, gravity_direction:
Vector3)

Sets the gravity direction at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_joint_radius(index: int, joint: int, radius: float)

Sets the joint radius at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_joint_rotation_axis(index: int, joint: int, axis: RotationAxis)

Sets the rotation axis at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_joint_stiffness(index: int, joint: int, stiffness: float)

Sets the stiffness force at `joint` in the bone chain's joint list when
is_config_individual() is `true`.

void set_radius(index: int, radius: float)

Sets the joint radius of the bone chain. It is used to move and slide with the
SpringBoneCollision3D in the collision list.

The value is scaled by set_radius_damping_curve() and cached in each joint
setting in the joint list.

void set_radius_damping_curve(index: int, curve: Curve)

Sets the joint radius damping curve of the bone chain.

void set_root_bone(index: int, bone: int)

Sets the root bone index of the bone chain.

void set_root_bone_name(index: int, bone_name: String)

Sets the root bone name of the bone chain.

void set_rotation_axis(index: int, axis: RotationAxis)

Sets the rotation axis of the bone chain. If sets a specific axis, it acts
like a hinge joint.

The value is cached in each joint setting in the joint list.

Note: The rotation axis and the forward vector shouldn't be colinear to avoid
unintended rotation since SpringBoneSimulator3D does not factor in twisting
forces.

void set_stiffness(index: int, stiffness: float)

Sets the stiffness force of the bone chain. The greater the value, the faster
it recovers to its initial pose.

If `stiffness` is `0`, the modified pose will not return to the original pose.

The value is scaled by set_stiffness_damping_curve() and cached in each joint
setting in the joint list.

void set_stiffness_damping_curve(index: int, curve: Curve)

Sets the stiffness force damping curve of the bone chain.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

