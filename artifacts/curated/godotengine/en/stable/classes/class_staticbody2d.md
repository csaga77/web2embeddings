# StaticBody2D

Inherits: PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node <
Object

Inherited By: AnimatableBody2D

A 2D physics body that can't be moved by external forces. When moved manually,
it doesn't affect other bodies in its path.

## Description

A static 2D physics body. It can't be moved by external forces or contacts,
but can be moved manually by other means such as code, AnimationMixers (with
AnimationMixer.callback_mode_process set to
AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), and
RemoteTransform2D.

When StaticBody2D is moved, it is teleported to its new position without
affecting other physics bodies in its path. If this is not desired, use
AnimatableBody2D instead.

StaticBody2D is useful for completely static objects like floors and walls, as
well as moving surfaces like conveyor belts and circular revolving platforms
(by using constant_linear_velocity and constant_angular_velocity).

## Properties

float | constant_angular_velocity | `0.0`  
---|---|---  
Vector2 | constant_linear_velocity | `Vector2(0, 0)`  
PhysicsMaterial | physics_material_override  
  
## Property Descriptions

float constant_angular_velocity = `0.0`

  * void set_constant_angular_velocity(value: float)

  * float get_constant_angular_velocity()

The body's constant angular velocity. This does not rotate the body, but
affects touching bodies, as if it were rotating.

Vector2 constant_linear_velocity = `Vector2(0, 0)`

  * void set_constant_linear_velocity(value: Vector2)

  * Vector2 get_constant_linear_velocity()

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

