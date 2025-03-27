# CapsuleShape2D

Inherits: Shape2D < Resource < RefCounted < Object

A 2D capsule shape used for physics collision.

## Description

A 2D capsule shape, intended for use in physics. Usually used to provide a
shape for a CollisionShape2D.

Performance: CapsuleShape2D is fast to check collisions against, but it is
slower than RectangleShape2D and CircleShape2D.

## Properties

float | height | `30.0`  
---|---|---  
float | radius | `10.0`  
  
## Property Descriptions

float height = `30.0`

  * void set_height(value: float)

  * float get_height()

The capsule's height.

float radius = `10.0`

  * void set_radius(value: float)

  * float get_radius()

The capsule's radius.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

