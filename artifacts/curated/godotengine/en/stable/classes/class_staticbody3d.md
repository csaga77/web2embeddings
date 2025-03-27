# StaticBody3D

Inherits: PhysicsBody3D < CollisionObject3D < Node3D < Node < Object

Inherited By: AnimatableBody3D

A 3D physics body that can't be moved by external forces. When moved manually,
it doesn't affect other bodies in its path.

## Description

A static 3D physics body. It can't be moved by external forces or contacts,
but can be moved manually by other means such as code, AnimationMixers (with
AnimationMixer.callback_mode_process set to
AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and
RemoteTransform3D.

When StaticBody3D is moved, it is teleported to its new position without
affecting other physics bodies in its path. If this is not desired, use
AnimatableBody3D instead.

StaticBody3D is useful for completely static objects like floors and walls, as
well as moving surfaces like conveyor belts and circular revolving platforms
(by using constant_linear_velocity and constant_angular_velocity).

## Tutorials

  * 3D Physics Tests Demo

  * Third Person Shooter (TPS) Demo

  * 3D Voxel Demo

## Properties

Vector3 | constant_angular_velocity | `Vector3(0, 0, 0)`  
---|---|---  
Vector3 | constant_linear_velocity | `Vector3(0, 0, 0)`  
PhysicsMaterial | physics_material_override  
  
## Property Descriptions

Vector3 constant_angular_velocity = `Vector3(0, 0, 0)`

  * void set_constant_angular_velocity(value: Vector3)

  * Vector3 get_constant_angular_velocity()

The body's constant angular velocity. This does not rotate the body, but
affects touching bodies, as if it were rotating.

Vector3 constant_linear_velocity = `Vector3(0, 0, 0)`

  * void set_constant_linear_velocity(value: Vector3)

  * Vector3 get_constant_linear_velocity()

The body's constant linear velocity. This does not move the body, but affects
touching bodies, as if it were moving.

PhysicsMaterial physics_material_override

  * void set_physics_material_override(value: PhysicsMaterial)

  * PhysicsMaterial get_physics_material_override()

The physics material override for the body.

If a material is assigned to this property, it will be used instead of any
other physics material, such as an inherited one.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

