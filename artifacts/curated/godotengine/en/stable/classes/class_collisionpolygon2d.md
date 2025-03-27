# CollisionPolygon2D

Inherits: Node2D < CanvasItem < Node < Object

A node that provides a polygon shape to a CollisionObject2D parent.

## Description

A node that provides a polygon shape to a CollisionObject2D parent and allows
to edit it. The polygon can be concave or convex. This can give a detection
shape to an Area2D, turn PhysicsBody2D into a solid object, or give a hollow
shape to a StaticBody2D.

Warning: A non-uniformly scaled CollisionPolygon2D will likely not behave as
expected. Make sure to keep its scale the same on all axes and adjust its
polygon instead.

## Properties

BuildMode | build_mode | `0`  
---|---|---  
bool | disabled | `false`  
bool | one_way_collision | `false`  
float | one_way_collision_margin | `1.0`  
PackedVector2Array | polygon | `PackedVector2Array()`  
  
## Enumerations

enum BuildMode:

BuildMode BUILD_SOLIDS = `0`

Collisions will include the polygon and its contained area. In this mode the
node has the same effect as several ConvexPolygonShape2D nodes, one for each
convex shape in the convex decomposition of the polygon (but without the
overhead of multiple nodes).

BuildMode BUILD_SEGMENTS = `1`

Collisions will only include the polygon edges. In this mode the node has the
same effect as a single ConcavePolygonShape2D made of segments, with the
restriction that each segment (after the first one) starts where the previous
one ends, and the last one ends where the first one starts (forming a closed
but hollow polygon).

## Property Descriptions

BuildMode build_mode = `0`

  * void set_build_mode(value: BuildMode)

  * BuildMode get_build_mode()

Collision build mode. Use one of the BuildMode constants.

bool disabled = `false`

  * void set_disabled(value: bool)

  * bool is_disabled()

If `true`, no collisions will be detected.

bool one_way_collision = `false`

  * void set_one_way_collision(value: bool)

  * bool is_one_way_collision_enabled()

If `true`, only edges that face up, relative to CollisionPolygon2D's rotation,
will collide with other objects.

Note: This property has no effect if this CollisionPolygon2D is a child of an
Area2D node.

float one_way_collision_margin = `1.0`

  * void set_one_way_collision_margin(value: float)

  * float get_one_way_collision_margin()

The margin used for one-way collision (in pixels). Higher values will make the
shape thicker, and work better for colliders that enter the polygon at a high
velocity.

PackedVector2Array polygon = `PackedVector2Array()`

  * void set_polygon(value: PackedVector2Array)

  * PackedVector2Array get_polygon()

The polygon's list of vertices. Each point will be connected to the next, and
the final point will be connected to the first.

Note: The returned vertices are in the local coordinate space of the given
CollisionPolygon2D.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedVector2Array for more details.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

