# ParallaxLayer

Inherits: Node2D < CanvasItem < Node < Object

A parallax scrolling layer to be used with ParallaxBackground.

## Description

A ParallaxLayer must be the child of a ParallaxBackground node. Each
ParallaxLayer can be set to move at different speeds relative to the camera
movement or the ParallaxBackground.scroll_offset value.

This node's children will be affected by its scroll offset.

Note: Any changes to this node's position and scale made after it enters the
scene will be ignored.

## Properties

Vector2 | motion_mirroring | `Vector2(0, 0)`  
---|---|---  
Vector2 | motion_offset | `Vector2(0, 0)`  
Vector2 | motion_scale | `Vector2(1, 1)`  
PhysicsInterpolationMode | physics_interpolation_mode | `2` (overrides Node)  
  
## Property Descriptions

Vector2 motion_mirroring = `Vector2(0, 0)`

  * void set_mirroring(value: Vector2)

  * Vector2 get_mirroring()

The interval, in pixels, at which the ParallaxLayer is drawn repeatedly.
Useful for creating an infinitely scrolling background. If an axis is set to
`0`, the ParallaxLayer will be drawn only once along that direction.

Note: If you want the repetition to pixel-perfect match a Texture2D displayed
by a child node, you should account for any scale applied to the texture when
defining this interval. For example, if you use a child Sprite2D scaled to
`0.5` to display a 600x600 texture, and want this sprite to be repeated
continuously horizontally, you should set the mirroring to `Vector2(300, 0)`.

Note: If the length of the viewport axis is bigger than twice the repeated
axis size, it will not repeat infinitely, as the parallax layer only draws 2
instances of the layer at any given time. The visibility window is calculated
from the parent ParallaxBackground's position, not the layer's own position.
So, if you use mirroring, do not change the ParallaxLayer position relative to
its parent. Instead, if you need to adjust the background's position, set the
CanvasLayer.offset property in the parent ParallaxBackground.

Note: Despite the name, the layer will not be mirrored, it will only be
repeated.

Vector2 motion_offset = `Vector2(0, 0)`

  * void set_motion_offset(value: Vector2)

  * Vector2 get_motion_offset()

The ParallaxLayer's offset relative to the parent ParallaxBackground's
ParallaxBackground.scroll_offset.

Vector2 motion_scale = `Vector2(1, 1)`

  * void set_motion_scale(value: Vector2)

  * Vector2 get_motion_scale()

Multiplies the ParallaxLayer's motion. If an axis is set to `0`, it will not
scroll.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

