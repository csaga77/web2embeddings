# ConvexPolygonShape3D

Inherits: Shape3D < Resource < RefCounted < Object

A 3D convex polyhedron shape used for physics collision.

## Description

A 3D convex polyhedron shape, intended for use in physics. Usually used to
provide a shape for a CollisionShape3D.

ConvexPolygonShape3D is solid, which means it detects collisions from objects
that are fully inside it, unlike ConcavePolygonShape3D which is hollow. This
makes it more suitable for both detection and physics.

Convex decomposition: A concave polyhedron can be split up into several convex
polyhedra. This allows dynamic physics bodies to have complex concave
collisions (at a performance cost) and can be achieved by using several
ConvexPolygonShape3D nodes. To generate a convex decomposition from a mesh,
select the MeshInstance3D node, go to the Mesh menu that appears above the
viewport, and choose Create Multiple Convex Collision Siblings. Alternatively,
MeshInstance3D.create_multiple_convex_collisions() can be called in a script
to perform this decomposition at run-time.

Performance: ConvexPolygonShape3D is faster to check collisions against
compared to ConcavePolygonShape3D, but it is slower than primitive collision
shapes such as SphereShape3D and BoxShape3D. Its use should generally be
limited to medium-sized objects that cannot have their collision accurately
represented by primitive shapes.

## Tutorials

  * 3D Physics Tests Demo

## Properties

PackedVector3Array | points | `PackedVector3Array()`  
---|---|---  
  
## Property Descriptions

PackedVector3Array points = `PackedVector3Array()`

  * void set_points(value: PackedVector3Array)

  * PackedVector3Array get_points()

The list of 3D points forming the convex polygon shape.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedVector3Array for more details.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

