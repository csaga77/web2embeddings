# Path3D

Inherits: Node3D < Node < Object

Contains a Curve3D path for PathFollow3D nodes to follow.

## Description

Can have PathFollow3D child nodes moving along the Curve3D. See PathFollow3D
for more information on the usage.

Note that the path is considered as relative to the moved nodes (children of
PathFollow3D). As such, the curve should usually start with a zero vector `(0,
0, 0)`.

## Properties

Curve3D | curve  
---|---  
  
## Signals

curve_changed()

Emitted when the curve changes.

## Property Descriptions

Curve3D curve

  * void set_curve(value: Curve3D)

  * Curve3D get_curve()

A Curve3D describing the path.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

