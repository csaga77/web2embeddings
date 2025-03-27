# Shape2D

Inherits: Resource < RefCounted < Object

Inherited By: CapsuleShape2D, CircleShape2D, ConcavePolygonShape2D,
ConvexPolygonShape2D, RectangleShape2D, SegmentShape2D, SeparationRayShape2D,
WorldBoundaryShape2D

Abstract base class for 2D shapes used for physics collision.

## Description

Abstract base class for all 2D shapes, intended for use in physics.

Performance: Primitive shapes, especially CircleShape2D, are fast to check
collisions against. ConvexPolygonShape2D is slower, and ConcavePolygonShape2D
is the slowest.

## Tutorials

  * Physics introduction

## Properties

float | custom_solver_bias | `0.0`  
---|---|---  
  
## Methods

bool | collide(local_xform: Transform2D, with_shape: Shape2D, shape_xform: Transform2D)  
---|---  
PackedVector2Array | collide_and_get_contacts(local_xform: Transform2D, with_shape: Shape2D, shape_xform: Transform2D)  
bool | collide_with_motion(local_xform: Transform2D, local_motion: Vector2, with_shape: Shape2D, shape_xform: Transform2D, shape_motion: Vector2)  
PackedVector2Array | collide_with_motion_and_get_contacts(local_xform: Transform2D, local_motion: Vector2, with_shape: Shape2D, shape_xform: Transform2D, shape_motion: Vector2)  
void | draw(canvas_item: RID, color: Color)  
Rect2 | get_rect() const  
  
## Property Descriptions

float custom_solver_bias = `0.0`

  * void set_custom_solver_bias(value: float)

  * float get_custom_solver_bias()

The shape's custom solver bias. Defines how much bodies react to enforce
contact separation when this shape is involved.

When set to `0`, the default value from
ProjectSettings.physics/2d/solver/default_contact_bias is used.

## Method Descriptions

bool collide(local_xform: Transform2D, with_shape: Shape2D, shape_xform:
Transform2D)

Returns `true` if this shape is colliding with another.

This method needs the transformation matrix for this shape (`local_xform`),
the shape to check collisions with (`with_shape`), and the transformation
matrix of that shape (`shape_xform`).

PackedVector2Array collide_and_get_contacts(local_xform: Transform2D,
with_shape: Shape2D, shape_xform: Transform2D)

Returns a list of contact point pairs where this shape touches another.

If there are no collisions, the returned list is empty. Otherwise, the
returned list contains contact points arranged in pairs, with entries
alternating between points on the boundary of this shape and points on the
boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with `(B -
A).normalized()`, and the collision depth with `(B - A).length()`. This
information is typically used to separate shapes, particularly in collision
solvers.

This method needs the transformation matrix for this shape (`local_xform`),
the shape to check collisions with (`with_shape`), and the transformation
matrix of that shape (`shape_xform`).

bool collide_with_motion(local_xform: Transform2D, local_motion: Vector2,
with_shape: Shape2D, shape_xform: Transform2D, shape_motion: Vector2)

Returns whether this shape would collide with another, if a given movement was
applied.

This method needs the transformation matrix for this shape (`local_xform`),
the movement to test on this shape (`local_motion`), the shape to check
collisions with (`with_shape`), the transformation matrix of that shape
(`shape_xform`), and the movement to test onto the other object
(`shape_motion`).

PackedVector2Array collide_with_motion_and_get_contacts(local_xform:
Transform2D, local_motion: Vector2, with_shape: Shape2D, shape_xform:
Transform2D, shape_motion: Vector2)

Returns a list of contact point pairs where this shape would touch another, if
a given movement was applied.

If there would be no collisions, the returned list is empty. Otherwise, the
returned list contains contact points arranged in pairs, with entries
alternating between points on the boundary of this shape and points on the
boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with `(B -
A).normalized()`, and the collision depth with `(B - A).length()`. This
information is typically used to separate shapes, particularly in collision
solvers.

This method needs the transformation matrix for this shape (`local_xform`),
the movement to test on this shape (`local_motion`), the shape to check
collisions with (`with_shape`), the transformation matrix of that shape
(`shape_xform`), and the movement to test onto the other object
(`shape_motion`).

void draw(canvas_item: RID, color: Color)

Draws a solid shape onto a CanvasItem with the RenderingServer API filled with
the specified `color`. The exact drawing method is specific for each shape and
cannot be configured.

Rect2 get_rect() const

Returns a Rect2 representing the shapes boundary.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

