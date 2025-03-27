# LabelSettings

Inherits: Resource < RefCounted < Object

Provides common settings to customize the text in a Label.

## Description

LabelSettings is a resource that provides common settings to customize the
text in a Label. It will take priority over the properties defined in
Control.theme. The resource can be shared between multiple labels and changed
on the fly, so it's convenient and flexible way to setup text style.

## Properties

Font | font  
---|---  
Color | font_color | `Color(1, 1, 1, 1)`  
int | font_size | `16`  
float | line_spacing | `3.0`  
Color | outline_color | `Color(1, 1, 1, 1)`  
int | outline_size | `0`  
float | paragraph_spacing | `0.0`  
Color | shadow_color | `Color(0, 0, 0, 0)`  
Vector2 | shadow_offset | `Vector2(1, 1)`  
int | shadow_size | `1`  
  
## Property Descriptions

Font font

  * void set_font(value: Font)

  * Font get_font()

Font used for the text.

Color font_color = `Color(1, 1, 1, 1)`

  * void set_font_color(value: Color)

  * Color get_font_color()

Color of the text.

int font_size = `16`

  * void set_font_size(value: int)

  * int get_font_size()

Size of the text.

float line_spacing = `3.0`

  * void set_line_spacing(value: float)

  * float get_line_spacing()

Additional vertical spacing between lines (in pixels), spacing is added to
line descent. This value can be negative.

Color outline_color = `Color(1, 1, 1, 1)`

  * void set_outline_color(value: Color)

  * Color get_outline_color()

The color of the outline.

int outline_size = `0`

  * void set_outline_size(value: int)

  * int get_outline_size()

Text outline size.

float paragraph_spacing = `0.0`

  * void set_paragraph_spacing(value: float)

  * float get_paragraph_spacing()

Vertical space between paragraphs. Added on top of line_spacing.

Color shadow_color = `Color(0, 0, 0, 0)`

  * void set_shadow_color(value: Color)

  * Color get_shadow_color()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

Vector2 shadow_offset = `Vector2(1, 1)`

  * void set_shadow_offset(value: Vector2)

  * Vector2 get_shadow_offset()

Offset of the shadow effect, in pixels.

int shadow_size = `1`

  * void set_shadow_size(value: int)

  * int get_shadow_size()

Size of the shadow effect.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

