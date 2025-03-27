# ConcavePolygonShape2D

Inherits: Shape2D < Resource < RefCounted < Object

A 2D polyline shape used for physics collision.

## Description

A 2D polyline shape, intended for use in physics. Used internally in
CollisionPolygon2D when it's in CollisionPolygon2D.BUILD_SEGMENTS mode.

Being just a collection of interconnected line segments, ConcavePolygonShape2D
is the most freely configurable single 2D shape. It can be used to form
polygons of any nature, or even shapes that don't enclose an area. However,
ConcavePolygonShape2D is hollow even if the interconnected line segments do
enclose an area, which often makes it unsuitable for physics or detection.

Note: When used for collision, ConcavePolygonShape2D is intended to work with
static CollisionShape2D nodes like StaticBody2D and will likely not behave
well for CharacterBody2Ds or RigidBody2Ds in a mode other than Static.

Warning: Physics bodies that are small have a chance to clip through this
shape when moving fast. This happens because on one frame, the physics body
may be on the "outside" of the shape, and on the next frame it may be "inside"
it. ConcavePolygonShape2D is hollow, so it won't detect a collision.

Performance: Due to its complexity, ConcavePolygonShape2D is the slowest 2D
collision shape to check collisions against. Its use should generally be
limited to level geometry. If the polyline is closed, CollisionPolygon2D's
CollisionPolygon2D.BUILD_SOLIDS mode can be used, which decomposes the polygon
into convex ones; see ConvexPolygonShape2D's documentation for instructions.

## Properties

PackedVector2Array | segments | `PackedVector2Array()`  
---|---|---  
  
## Property Descriptions

PackedVector2Array segments = `PackedVector2Array()`

  * void set_segments(value: PackedVector2Array)

  * PackedVector2Array get_segments()

The array of points that make up the ConcavePolygonShape2D's line segments.
The array (of length divisible by two) is naturally divided into pairs (one
pair for each segment); each pair consists of the starting point of a segment
and the endpoint of a segment.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedVector2Array for more details.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

