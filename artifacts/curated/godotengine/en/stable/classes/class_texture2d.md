# Texture2D

Inherits: Texture < Resource < RefCounted < Object

Inherited By: AnimatedTexture, AtlasTexture, CameraTexture, CanvasTexture,
CompressedTexture2D, CurveTexture, CurveXYZTexture, ExternalTexture,
GradientTexture1D, GradientTexture2D, ImageTexture, MeshTexture,
NoiseTexture2D, PlaceholderTexture2D, PortableCompressedTexture2D,
Texture2DRD, ViewportTexture

Texture for 2D and 3D.

## Description

A texture works by registering an image in the video hardware, which then can
be used in 3D models or 2D Sprite2D or GUI Control.

Textures are often created by loading them from a file. See @GDScript.load().

Texture2D is a base for other resources. It cannot be used directly.

Note: The maximum texture size is 1638416384 pixels due to graphics hardware
limitations. Larger textures may fail to import.

## Methods

void | _draw(to_canvas_item: RID, pos: Vector2, modulate: Color, transpose: bool) virtual const  
---|---  
void | _draw_rect(to_canvas_item: RID, rect: Rect2, tile: bool, modulate: Color, transpose: bool) virtual const  
void | _draw_rect_region(to_canvas_item: RID, rect: Rect2, src_rect: Rect2, modulate: Color, transpose: bool, clip_uv: bool) virtual const  
int | _get_height() virtual const  
int | _get_width() virtual const  
bool | _has_alpha() virtual const  
bool | _is_pixel_opaque(x: int, y: int) virtual const  
Resource | create_placeholder() const  
void | draw(canvas_item: RID, position: Vector2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) const  
void | draw_rect(canvas_item: RID, rect: Rect2, tile: bool, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) const  
void | draw_rect_region(canvas_item: RID, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool = true) const  
int | get_height() const  
Image | get_image() const  
Vector2 | get_size() const  
int | get_width() const  
bool | has_alpha() const  
  
## Method Descriptions

void _draw(to_canvas_item: RID, pos: Vector2, modulate: Color, transpose:
bool) virtual const

Called when the entire Texture2D is requested to be drawn over a CanvasItem,
with the top-left offset specified in `pos`. `modulate` specifies a multiplier
for the colors being drawn, while `transpose` specifies whether drawing should
be performed in column-major order instead of row-major order (resulting in
90-degree clockwise rotation).

Note: This is only used in 2D rendering, not 3D.

void _draw_rect(to_canvas_item: RID, rect: Rect2, tile: bool, modulate: Color,
transpose: bool) virtual const

Called when the Texture2D is requested to be drawn onto CanvasItem's specified
`rect`. `modulate` specifies a multiplier for the colors being drawn, while
`transpose` specifies whether drawing should be performed in column-major
order instead of row-major order (resulting in 90-degree clockwise rotation).

Note: This is only used in 2D rendering, not 3D.

void _draw_rect_region(to_canvas_item: RID, rect: Rect2, src_rect: Rect2,
modulate: Color, transpose: bool, clip_uv: bool) virtual const

Called when a part of the Texture2D specified by `src_rect`'s coordinates is
requested to be drawn onto CanvasItem's specified `rect`. `modulate` specifies
a multiplier for the colors being drawn, while `transpose` specifies whether
drawing should be performed in column-major order instead of row-major order
(resulting in 90-degree clockwise rotation).

Note: This is only used in 2D rendering, not 3D.

int _get_height() virtual const

Called when the Texture2D's height is queried.

int _get_width() virtual const

Called when the Texture2D's width is queried.

bool _has_alpha() virtual const

Called when the presence of an alpha channel in the Texture2D is queried.

bool _is_pixel_opaque(x: int, y: int) virtual const

Called when a pixel's opaque state in the Texture2D is queried at the
specified `(x, y)` position.

Resource create_placeholder() const

Creates a placeholder version of this resource (PlaceholderTexture2D).

void draw(canvas_item: RID, position: Vector2, modulate: Color = Color(1, 1,
1, 1), transpose: bool = false) const

Draws the texture using a CanvasItem with the RenderingServer API at the
specified `position`.

void draw_rect(canvas_item: RID, rect: Rect2, tile: bool, modulate: Color =
Color(1, 1, 1, 1), transpose: bool = false) const

Draws the texture using a CanvasItem with the RenderingServer API.

void draw_rect_region(canvas_item: RID, rect: Rect2, src_rect: Rect2,
modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool =
true) const

Draws a part of the texture using a CanvasItem with the RenderingServer API.

int get_height() const

Returns the texture height in pixels.

Image get_image() const

Returns an Image that is a copy of data from this Texture2D (a new Image is
created each time). Images can be accessed and manipulated directly.

Note: This will return `null` if this Texture2D is invalid.

Note: This will fetch the texture data from the GPU, which might cause
performance problems when overused. Avoid calling get_image() every frame,
especially on large textures.

Vector2 get_size() const

Returns the texture size in pixels.

int get_width() const

Returns the texture width in pixels.

bool has_alpha() const

Returns `true` if this Texture2D has an alpha channel.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

