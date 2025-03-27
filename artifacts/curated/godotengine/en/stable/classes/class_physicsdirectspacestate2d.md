# PhysicsDirectSpaceState2D

Inherits: Object

Inherited By: PhysicsDirectSpaceState2DExtension

Provides direct access to a physics space in the PhysicsServer2D.

## Description

Provides direct access to a physics space in the PhysicsServer2D. It's used
mainly to do queries against objects and areas residing in a given space.

## Tutorials

  * Physics introduction

  * Ray-casting

## Methods

PackedFloat32Array | cast_motion(parameters: PhysicsShapeQueryParameters2D)  
---|---  
Array[Vector2] | collide_shape(parameters: PhysicsShapeQueryParameters2D, max_results: int = 32)  
Dictionary | get_rest_info(parameters: PhysicsShapeQueryParameters2D)  
Array[Dictionary] | intersect_point(parameters: PhysicsPointQueryParameters2D, max_results: int = 32)  
Dictionary | intersect_ray(parameters: PhysicsRayQueryParameters2D)  
Array[Dictionary] | intersect_shape(parameters: PhysicsShapeQueryParameters2D, max_results: int = 32)  
  
## Method Descriptions

PackedFloat32Array cast_motion(parameters: PhysicsShapeQueryParameters2D)

Checks how far a Shape2D can move without colliding. All the parameters for
the query, including the shape and the motion, are supplied through a
PhysicsShapeQueryParameters2D object.

Returns an array with the safe and unsafe proportions (between 0 and 1) of the
motion. The safe proportion is the maximum fraction of the motion that can be
made without a collision. The unsafe proportion is the minimum fraction of the
distance that must be moved for a collision. If no collision is detected a
result of `[1.0, 1.0]` will be returned.

Note: Any Shape2Ds that the shape is already colliding with e.g. inside of,
will be ignored. Use collide_shape() to determine the Shape2Ds that the shape
is already colliding with.

Array[Vector2] collide_shape(parameters: PhysicsShapeQueryParameters2D,
max_results: int = 32)

Checks the intersections of a shape, given through a
PhysicsShapeQueryParameters2D object, against the space. The resulting array
contains a list of points where the shape intersects another. Like with
intersect_shape(), the number of returned results can be limited to save
processing time.

Returned points are a list of pairs of contact points. For each pair the first
one is in the shape passed in PhysicsShapeQueryParameters2D object, second one
is in the collided shape from the physics space.

Dictionary get_rest_info(parameters: PhysicsShapeQueryParameters2D)

Checks the intersections of a shape, given through a
PhysicsShapeQueryParameters2D object, against the space. If it collides with
more than one shape, the nearest one is selected. If the shape did not
intersect anything, then an empty dictionary is returned instead.

Note: This method does not take into account the `motion` property of the
object. The returned object is a dictionary containing the following fields:

`collider_id`: The colliding object's ID.

`linear_velocity`: The colliding object's velocity Vector2. If the object is
an Area2D, the result is `(0, 0)`.

`normal`: The collision normal of the query shape at the intersection point,
pointing away from the intersecting object.

`point`: The intersection point.

`rid`: The intersecting object's RID.

`shape`: The shape index of the colliding shape.

Array[Dictionary] intersect_point(parameters: PhysicsPointQueryParameters2D,
max_results: int = 32)

Checks whether a point is inside any solid shape. Position and other
parameters are defined through PhysicsPointQueryParameters2D. The shapes the
point is inside of are returned in an array containing dictionaries with the
following fields:

`collider`: The colliding object.

`collider_id`: The colliding object's ID.

`rid`: The intersecting object's RID.

`shape`: The shape index of the colliding shape.

The number of intersections can be limited with the `max_results` parameter,
to reduce the processing time.

Note: ConcavePolygonShape2Ds and CollisionPolygon2Ds in `Segments` build mode
are not solid shapes. Therefore, they will not be detected.

Dictionary intersect_ray(parameters: PhysicsRayQueryParameters2D)

Intersects a ray in a given space. Ray position and other parameters are
defined through PhysicsRayQueryParameters2D. The returned object is a
dictionary with the following fields:

`collider`: The colliding object.

`collider_id`: The colliding object's ID.

`normal`: The object's surface normal at the intersection point, or
`Vector2(0, 0)` if the ray starts inside the shape and
PhysicsRayQueryParameters2D.hit_from_inside is `true`.

`position`: The intersection point.

`rid`: The intersecting object's RID.

`shape`: The shape index of the colliding shape.

If the ray did not intersect anything, then an empty dictionary is returned
instead.

Array[Dictionary] intersect_shape(parameters: PhysicsShapeQueryParameters2D,
max_results: int = 32)

Checks the intersections of a shape, given through a
PhysicsShapeQueryParameters2D object, against the space. The intersected
shapes are returned in an array containing dictionaries with the following
fields:

`collider`: The colliding object.

`collider_id`: The colliding object's ID.

`rid`: The intersecting object's RID.

`shape`: The shape index of the colliding shape.

The number of intersections can be limited with the `max_results` parameter,
to reduce the processing time.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

