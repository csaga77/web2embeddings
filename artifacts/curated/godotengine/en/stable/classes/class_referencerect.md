# ReferenceRect

Inherits: Control < CanvasItem < Node < Object

A rectangle hint for designing UIs.

## Description

A rectangle box that displays only a colored border around its rectangle. It
is used to visualize the extents of a Control.

## Properties

Color | border_color | `Color(1, 0, 0, 1)`  
---|---|---  
float | border_width | `1.0`  
bool | editor_only | `true`  
  
## Property Descriptions

Color border_color = `Color(1, 0, 0, 1)`

  * void set_border_color(value: Color)

  * Color get_border_color()

Sets the border color of the ReferenceRect.

float border_width = `1.0`

  * void set_border_width(value: float)

  * float get_border_width()

Sets the border width of the ReferenceRect. The border grows both inwards and
outwards with respect to the rectangle box.

bool editor_only = `true`

  * void set_editor_only(value: bool)

  * bool get_editor_only()

If `true`, the ReferenceRect will only be visible while in editor. Otherwise,
ReferenceRect will be visible in the running project.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

