# AnimationNodeBlendSpace1D

Inherits: AnimationRootNode < AnimationNode < Resource < RefCounted < Object

A set of AnimationRootNodes placed on a virtual axis, crossfading between the
two adjacent ones. Used by AnimationTree.

## Description

A resource used by AnimationNodeBlendTree.

AnimationNodeBlendSpace1D represents a virtual axis on which any type of
AnimationRootNodes can be added using add_blend_point(). Outputs the linear
blend of the two AnimationRootNodes adjacent to the current value.

You can set the extents of the axis with min_space and max_space.

## Tutorials

  * Using AnimationTree

## Properties

BlendMode | blend_mode | `0`  
---|---|---  
float | max_space | `1.0`  
float | min_space | `-1.0`  
float | snap | `0.1`  
bool | sync | `false`  
String | value_label | `"value"`  
  
## Methods

void | add_blend_point(node: AnimationRootNode, pos: float, at_index: int = -1)  
---|---  
int | get_blend_point_count() const  
AnimationRootNode | get_blend_point_node(point: int) const  
float | get_blend_point_position(point: int) const  
void | remove_blend_point(point: int)  
void | set_blend_point_node(point: int, node: AnimationRootNode)  
void | set_blend_point_position(point: int, pos: float)  
  
## Enumerations

enum BlendMode:

BlendMode BLEND_MODE_INTERPOLATED = `0`

The interpolation between animations is linear.

BlendMode BLEND_MODE_DISCRETE = `1`

The blend space plays the animation of the animation node which blending
position is closest to. Useful for frame-by-frame 2D animations.

BlendMode BLEND_MODE_DISCRETE_CARRY = `2`

Similar to BLEND_MODE_DISCRETE, but starts the new animation at the last
animation's playback position.

## Property Descriptions

BlendMode blend_mode = `0`

  * void set_blend_mode(value: BlendMode)

  * BlendMode get_blend_mode()

Controls the interpolation between animations. See BlendMode constants.

float max_space = `1.0`

  * void set_max_space(value: float)

  * float get_max_space()

The blend space's axis's upper limit for the points' position. See
add_blend_point().

float min_space = `-1.0`

  * void set_min_space(value: float)

  * float get_min_space()

The blend space's axis's lower limit for the points' position. See
add_blend_point().

float snap = `0.1`

  * void set_snap(value: float)

  * float get_snap()

Position increment to snap to when moving a point on the axis.

bool sync = `false`

  * void set_use_sync(value: bool)

  * bool is_using_sync()

If `false`, the blended animations' frame are stopped when the blend value is
`0`.

If `true`, forcing the blended animations to advance frame.

String value_label = `"value"`

  * void set_value_label(value: String)

  * String get_value_label()

Label of the virtual axis of the blend space.

## Method Descriptions

void add_blend_point(node: AnimationRootNode, pos: float, at_index: int = -1)

Adds a new point that represents a `node` on the virtual axis at a given
position set by `pos`. You can insert it at a specific index using the
`at_index` argument. If you use the default value for `at_index`, the point is
inserted at the end of the blend points array.

int get_blend_point_count() const

Returns the number of points on the blend axis.

AnimationRootNode get_blend_point_node(point: int) const

Returns the AnimationNode referenced by the point at index `point`.

float get_blend_point_position(point: int) const

Returns the position of the point at index `point`.

void remove_blend_point(point: int)

Removes the point at index `point` from the blend axis.

void set_blend_point_node(point: int, node: AnimationRootNode)

Changes the AnimationNode referenced by the point at index `point`.

void set_blend_point_position(point: int, pos: float)

Updates the position of the point at index `point` on the blend axis.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

