# SoftBody3D

Inherits: MeshInstance3D < GeometryInstance3D < VisualInstance3D < Node3D <
Node < Object

A deformable 3D physics mesh.

## Description

A deformable 3D physics mesh. Used to create elastic or deformable objects
such as cloth, rubber, or other flexible materials.

Additionally, SoftBody3D is subject to wind forces defined in Area3D (see
Area3D.wind_source_path, Area3D.wind_force_magnitude, and
Area3D.wind_attenuation_factor).

Note: There are many known bugs in SoftBody3D. Therefore, it's not recommended
to use them for things that can affect gameplay (such as trampolines).

## Tutorials

  * SoftBody

## Properties

int | collision_layer | `1`  
---|---|---  
int | collision_mask | `1`  
float | damping_coefficient | `0.01`  
DisableMode | disable_mode | `0`  
float | drag_coefficient | `0.0`  
float | linear_stiffness | `0.5`  
NodePath | parent_collision_ignore | `NodePath("")`  
float | pressure_coefficient | `0.0`  
bool | ray_pickable | `true`  
int | simulation_precision | `5`  
float | total_mass | `1.0`  
  
## Methods

void | add_collision_exception_with(body: Node)  
---|---  
Array[PhysicsBody3D] | get_collision_exceptions()  
bool | get_collision_layer_value(layer_number: int) const  
bool | get_collision_mask_value(layer_number: int) const  
RID | get_physics_rid() const  
Vector3 | get_point_transform(point_index: int)  
bool | is_point_pinned(point_index: int) const  
void | remove_collision_exception_with(body: Node)  
void | set_collision_layer_value(layer_number: int, value: bool)  
void | set_collision_mask_value(layer_number: int, value: bool)  
void | set_point_pinned(point_index: int, pinned: bool, attachment_path: NodePath = NodePath(""), insert_at: int = -1)  
  
## Enumerations

enum DisableMode:

DisableMode DISABLE_MODE_REMOVE = `0`

When Node.process_mode is set to Node.PROCESS_MODE_DISABLED, remove from the
physics simulation to stop all physics interactions with this SoftBody3D.

Automatically re-added to the physics simulation when the Node is processed
again.

DisableMode DISABLE_MODE_KEEP_ACTIVE = `1`

When Node.process_mode is set to Node.PROCESS_MODE_DISABLED, do not affect the
physics simulation.

## Property Descriptions

int collision_layer = `1`

  * void set_collision_layer(value: int)

  * int get_collision_layer()

The physics layers this SoftBody3D is in. Collision objects can exist in one
or more of 32 different layers. See also collision_mask.

Note: Object A can detect a contact with object B only if object B is in any
of the layers that object A scans. See Collision layers and masks in the
documentation for more information.

int collision_mask = `1`

  * void set_collision_mask(value: int)

  * int get_collision_mask()

The physics layers this SoftBody3D scans. Collision objects can scan one or
more of 32 different layers. See also collision_layer.

Note: Object A can detect a contact with object B only if object B is in any
of the layers that object A scans. See Collision layers and masks in the
documentation for more information.

float damping_coefficient = `0.01`

  * void set_damping_coefficient(value: float)

  * float get_damping_coefficient()

The body's damping coefficient. Higher values will slow down the body more
noticeably when forces are applied.

DisableMode disable_mode = `0`

  * void set_disable_mode(value: DisableMode)

  * DisableMode get_disable_mode()

Defines the behavior in physics when Node.process_mode is set to
Node.PROCESS_MODE_DISABLED. See DisableMode for more details about the
different modes.

float drag_coefficient = `0.0`

  * void set_drag_coefficient(value: float)

  * float get_drag_coefficient()

The body's drag coefficient. Higher values increase this body's air
resistance.

Note: This value is currently unused by Godot's default physics
implementation.

float linear_stiffness = `0.5`

  * void set_linear_stiffness(value: float)

  * float get_linear_stiffness()

Higher values will result in a stiffer body, while lower values will increase
the body's ability to bend. The value can be between `0.0` and `1.0`
(inclusive).

NodePath parent_collision_ignore = `NodePath("")`

  * void set_parent_collision_ignore(value: NodePath)

  * NodePath get_parent_collision_ignore()

NodePath to a CollisionObject3D this SoftBody3D should avoid clipping.

float pressure_coefficient = `0.0`

  * void set_pressure_coefficient(value: float)

  * float get_pressure_coefficient()

The pressure coefficient of this soft body. Simulate pressure build-up from
inside this body. Higher values increase the strength of this effect.

bool ray_pickable = `true`

  * void set_ray_pickable(value: bool)

  * bool is_ray_pickable()

If `true`, the SoftBody3D will respond to RayCast3Ds.

int simulation_precision = `5`

  * void set_simulation_precision(value: int)

  * int get_simulation_precision()

Increasing this value will improve the resulting simulation, but can affect
performance. Use with care.

float total_mass = `1.0`

  * void set_total_mass(value: float)

  * float get_total_mass()

The SoftBody3D's mass.

## Method Descriptions

void add_collision_exception_with(body: Node)

Adds a body to the list of bodies that this body can't collide with.

Array[PhysicsBody3D] get_collision_exceptions()

Returns an array of nodes that were added as collision exceptions for this
body.

bool get_collision_layer_value(layer_number: int) const

Returns whether or not the specified layer of the collision_layer is enabled,
given a `layer_number` between 1 and 32.

bool get_collision_mask_value(layer_number: int) const

Returns whether or not the specified layer of the collision_mask is enabled,
given a `layer_number` between 1 and 32.

RID get_physics_rid() const

Returns the internal RID used by the PhysicsServer3D for this body.

Vector3 get_point_transform(point_index: int)

Returns local translation of a vertex in the surface array.

bool is_point_pinned(point_index: int) const

Returns `true` if vertex is set to pinned.

void remove_collision_exception_with(body: Node)

Removes a body from the list of bodies that this body can't collide with.

void set_collision_layer_value(layer_number: int, value: bool)

Based on `value`, enables or disables the specified layer in the
collision_layer, given a `layer_number` between 1 and 32.

void set_collision_mask_value(layer_number: int, value: bool)

Based on `value`, enables or disables the specified layer in the
collision_mask, given a `layer_number` between 1 and 32.

void set_point_pinned(point_index: int, pinned: bool, attachment_path:
NodePath = NodePath(""), insert_at: int = -1)

Sets the pinned state of a surface vertex. When set to `true`, the optional
`attachment_path` can define a Node3D the pinned vertex will be attached to.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

