# CapsuleShape3D

Inherits: Shape3D < Resource < RefCounted < Object

A 3D capsule shape used for physics collision.

## Description

A 3D capsule shape, intended for use in physics. Usually used to provide a
shape for a CollisionShape3D.

Performance: CapsuleShape3D is fast to check collisions against. It is faster
than CylinderShape3D, but slower than SphereShape3D and BoxShape3D.

## Tutorials

  * 3D Physics Tests Demo

## Properties

float | height | `2.0`  
---|---|---  
float | radius | `0.5`  
  
## Property Descriptions

float height = `2.0`

  * void set_height(value: float)

  * float get_height()

The capsule's height.

float radius = `0.5`

  * void set_radius(value: float)

  * float get_radius()

The capsule's radius.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

