# CollisionShape2D

Inherits: Node2D < CanvasItem < Node < Object

A node that provides a Shape2D to a CollisionObject2D parent.

## Description

A node that provides a Shape2D to a CollisionObject2D parent and allows to
edit it. This can give a detection shape to an Area2D or turn a PhysicsBody2D
into a solid object.

## Tutorials

  * Physics introduction

  * 2D Dodge The Creeps Demo

  * 2D Pong Demo

  * 2D Kinematic Character Demo

## Properties

Color | debug_color | `Color(0, 0, 0, 0)`  
---|---|---  
bool | disabled | `false`  
bool | one_way_collision | `false`  
float | one_way_collision_margin | `1.0`  
Shape2D | shape  
  
## Property Descriptions

Color debug_color = `Color(0, 0, 0, 0)`

  * void set_debug_color(value: Color)

  * Color get_debug_color()

The collision shape color that is displayed in the editor, or in the running
project if Debug > Visible Collision Shapes is checked at the top of the
editor.

Note: The default value is ProjectSettings.debug/shapes/collision/shape_color.
The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the
actual default debug color.

bool disabled = `false`

  * void set_disabled(value: bool)

  * bool is_disabled()

A disabled collision shape has no effect in the world. This property should be
changed with Object.set_deferred().

bool one_way_collision = `false`

  * void set_one_way_collision(value: bool)

  * bool is_one_way_collision_enabled()

Sets whether this collision shape should only detect collision on one side
(top or bottom).

Note: This property has no effect if this CollisionShape2D is a child of an
Area2D node.

float one_way_collision_margin = `1.0`

  * void set_one_way_collision_margin(value: float)

  * float get_one_way_collision_margin()

The margin used for one-way collision (in pixels). Higher values will make the
shape thicker, and work better for colliders that enter the shape at a high
velocity.

Shape2D shape

  * void set_shape(value: Shape2D)

  * Shape2D get_shape()

The actual shape owned by this collision shape.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

