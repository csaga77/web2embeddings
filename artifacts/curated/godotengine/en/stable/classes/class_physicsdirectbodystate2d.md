# PhysicsDirectBodyState2D

Inherits: Object

Inherited By: PhysicsDirectBodyState2DExtension

Provides direct access to a physics body in the PhysicsServer2D.

## Description

Provides direct access to a physics body in the PhysicsServer2D, allowing safe
changes to physics properties. This object is passed via the direct state
callback of RigidBody2D, and is intended for changing the direct state of that
body. See RigidBody2D._integrate_forces().

## Tutorials

  * Physics introduction

  * Ray-casting

## Properties

float | angular_velocity  
---|---  
Vector2 | center_of_mass  
Vector2 | center_of_mass_local  
float | inverse_inertia  
float | inverse_mass  
Vector2 | linear_velocity  
bool | sleeping  
float | step  
float | total_angular_damp  
Vector2 | total_gravity  
float | total_linear_damp  
Transform2D | transform  
  
## Methods

void | add_constant_central_force(force: Vector2 = Vector2(0, 0))  
---|---  
void | add_constant_force(force: Vector2, position: Vector2 = Vector2(0, 0))  
void | add_constant_torque(torque: float)  
void | apply_central_force(force: Vector2 = Vector2(0, 0))  
void | apply_central_impulse(impulse: Vector2)  
void | apply_force(force: Vector2, position: Vector2 = Vector2(0, 0))  
void | apply_impulse(impulse: Vector2, position: Vector2 = Vector2(0, 0))  
void | apply_torque(torque: float)  
void | apply_torque_impulse(impulse: float)  
Vector2 | get_constant_force() const  
float | get_constant_torque() const  
RID | get_contact_collider(contact_idx: int) const  
int | get_contact_collider_id(contact_idx: int) const  
Object | get_contact_collider_object(contact_idx: int) const  
Vector2 | get_contact_collider_position(contact_idx: int) const  
int | get_contact_collider_shape(contact_idx: int) const  
Vector2 | get_contact_collider_velocity_at_position(contact_idx: int) const  
int | get_contact_count() const  
Vector2 | get_contact_impulse(contact_idx: int) const  
Vector2 | get_contact_local_normal(contact_idx: int) const  
Vector2 | get_contact_local_position(contact_idx: int) const  
int | get_contact_local_shape(contact_idx: int) const  
Vector2 | get_contact_local_velocity_at_position(contact_idx: int) const  
PhysicsDirectSpaceState2D | get_space_state()  
Vector2 | get_velocity_at_local_position(local_position: Vector2) const  
void | integrate_forces()  
void | set_constant_force(force: Vector2)  
void | set_constant_torque(torque: float)  
  
## Property Descriptions

float angular_velocity

  * void set_angular_velocity(value: float)

  * float get_angular_velocity()

The body's rotational velocity in radians per second.

Vector2 center_of_mass

  * Vector2 get_center_of_mass()

The body's center of mass position relative to the body's center in the global
coordinate system.

Vector2 center_of_mass_local

  * Vector2 get_center_of_mass_local()

The body's center of mass position in the body's local coordinate system.

float inverse_inertia

  * float get_inverse_inertia()

The inverse of the inertia of the body.

float inverse_mass

  * float get_inverse_mass()

The inverse of the mass of the body.

Vector2 linear_velocity

  * void set_linear_velocity(value: Vector2)

  * Vector2 get_linear_velocity()

The body's linear velocity in pixels per second.

bool sleeping

  * void set_sleep_state(value: bool)

  * bool is_sleeping()

If `true`, this body is currently sleeping (not active).

float step

  * float get_step()

The timestep (delta) used for the simulation.

float total_angular_damp

  * float get_total_angular_damp()

The rate at which the body stops rotating, if there are not any other forces
moving it.

Vector2 total_gravity

  * Vector2 get_total_gravity()

The total gravity vector being currently applied to this body.

float total_linear_damp

  * float get_total_linear_damp()

The rate at which the body stops moving, if there are not any other forces
moving it.

Transform2D transform

  * void set_transform(value: Transform2D)

  * Transform2D get_transform()

The body's transformation matrix.

## Method Descriptions

void add_constant_central_force(force: Vector2 = Vector2(0, 0))

Adds a constant directional force without affecting rotation that keeps being
applied over time until cleared with `constant_force = Vector2(0, 0)`.

This is equivalent to using add_constant_force() at the body's center of mass.

void add_constant_force(force: Vector2, position: Vector2 = Vector2(0, 0))

Adds a constant positioned force to the body that keeps being applied over
time until cleared with `constant_force = Vector2(0, 0)`.

`position` is the offset from the body origin in global coordinates.

void add_constant_torque(torque: float)

Adds a constant rotational force without affecting position that keeps being
applied over time until cleared with `constant_torque = 0`.

void apply_central_force(force: Vector2 = Vector2(0, 0))

Applies a directional force without affecting rotation. A force is time
dependent and meant to be applied every physics update.

This is equivalent to using apply_force() at the body's center of mass.

void apply_central_impulse(impulse: Vector2)

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result
in a framerate-dependent force. For this reason, it should only be used when
simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using apply_impulse() at the body's center of mass.

void apply_force(force: Vector2, position: Vector2 = Vector2(0, 0))

Applies a positioned force to the body. A force is time dependent and meant to
be applied every physics update.

`position` is the offset from the body origin in global coordinates.

void apply_impulse(impulse: Vector2, position: Vector2 = Vector2(0, 0))

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result
in a framerate-dependent force. For this reason, it should only be used when
simulating one-time impacts (use the "_force" functions otherwise).

`position` is the offset from the body origin in global coordinates.

void apply_torque(torque: float)

Applies a rotational force without affecting position. A force is time
dependent and meant to be applied every physics update.

Note: inverse_inertia is required for this to work. To have inverse_inertia,
an active CollisionShape2D must be a child of the node, or you can manually
set inverse_inertia.

void apply_torque_impulse(impulse: float)

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result
in a framerate-dependent force. For this reason, it should only be used when
simulating one-time impacts (use the "_force" functions otherwise).

Note: inverse_inertia is required for this to work. To have inverse_inertia,
an active CollisionShape2D must be a child of the node, or you can manually
set inverse_inertia.

Vector2 get_constant_force() const

Returns the body's total constant positional forces applied during each
physics update.

See add_constant_force() and add_constant_central_force().

float get_constant_torque() const

Returns the body's total constant rotational forces applied during each
physics update.

See add_constant_torque().

RID get_contact_collider(contact_idx: int) const

Returns the collider's RID.

int get_contact_collider_id(contact_idx: int) const

Returns the collider's object id.

Object get_contact_collider_object(contact_idx: int) const

Returns the collider object. This depends on how it was created (will return a
scene node if such was used to create it).

Vector2 get_contact_collider_position(contact_idx: int) const

Returns the position of the contact point on the collider in the global
coordinate system.

int get_contact_collider_shape(contact_idx: int) const

Returns the collider's shape index.

Vector2 get_contact_collider_velocity_at_position(contact_idx: int) const

Returns the velocity vector at the collider's contact point.

int get_contact_count() const

Returns the number of contacts this body has with other bodies.

Note: By default, this returns 0 unless bodies are configured to monitor
contacts. See RigidBody2D.contact_monitor.

Vector2 get_contact_impulse(contact_idx: int) const

Returns the impulse created by the contact.

Vector2 get_contact_local_normal(contact_idx: int) const

Returns the local normal at the contact point.

Vector2 get_contact_local_position(contact_idx: int) const

Returns the position of the contact point on the body in the global coordinate
system.

int get_contact_local_shape(contact_idx: int) const

Returns the local shape index of the collision.

Vector2 get_contact_local_velocity_at_position(contact_idx: int) const

Returns the velocity vector at the body's contact point.

PhysicsDirectSpaceState2D get_space_state()

Returns the current state of the space, useful for queries.

Vector2 get_velocity_at_local_position(local_position: Vector2) const

Returns the body's velocity at the given relative position, including both
translation and rotation.

void integrate_forces()

Updates the body's linear and angular velocity by applying gravity and damping
for the equivalent of one physics tick.

void set_constant_force(force: Vector2)

Sets the body's total constant positional forces applied during each physics
update.

See add_constant_force() and add_constant_central_force().

void set_constant_torque(torque: float)

Sets the body's total constant rotational forces applied during each physics
update.

See add_constant_torque().

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

