# CanvasGroup

Inherits: Node2D < CanvasItem < Node < Object

Merges several 2D nodes into a single draw operation.

## Description

Child CanvasItem nodes of a CanvasGroup are drawn as a single object. It
allows to e.g. draw overlapping translucent 2D nodes without blending (set
CanvasItem.self_modulate property of CanvasGroup to achieve this effect).

Note: The CanvasGroup uses a custom shader to read from the backbuffer to draw
its children. Assigning a Material to the CanvasGroup overrides the builtin
shader. To duplicate the behavior of the builtin shader in a custom Shader use
the following:

    
    
    shader_type canvas_item;
    render_mode unshaded;
    
    uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;
    
    void fragment() {
        vec4 c = textureLod(screen_texture, SCREEN_UV, 0.0);
    
        if (c.a > 0.0001) {
            c.rgb /= c.a;
        }
    
        COLOR *= c;
    }
    

Note: Since CanvasGroup and CanvasItem.clip_children both utilize the
backbuffer, children of a CanvasGroup who have their CanvasItem.clip_children
set to anything other than CanvasItem.CLIP_CHILDREN_DISABLED will not function
correctly.

## Properties

float | clear_margin | `10.0`  
---|---|---  
float | fit_margin | `10.0`  
bool | use_mipmaps | `false`  
  
## Property Descriptions

float clear_margin = `10.0`

  * void set_clear_margin(value: float)

  * float get_clear_margin()

Sets the size of the margin used to expand the clearing rect of this
CanvasGroup. This expands the area of the backbuffer that will be used by the
CanvasGroup. A smaller margin will reduce the area of the backbuffer used
which can increase performance, however if use_mipmaps is enabled, a small
margin may result in mipmap errors at the edge of the CanvasGroup.
Accordingly, this should be left as small as possible, but should be increased
if artifacts appear along the edges of the canvas group.

float fit_margin = `10.0`

  * void set_fit_margin(value: float)

  * float get_fit_margin()

Sets the size of a margin used to expand the drawable rect of this
CanvasGroup. The size of the CanvasGroup is determined by fitting a rect
around its children then expanding that rect by fit_margin. This increases
both the backbuffer area used and the area covered by the CanvasGroup both of
which can reduce performance. This should be kept as small as possible and
should only be expanded when an increased size is needed (e.g. for custom
shader effects).

bool use_mipmaps = `false`

  * void set_use_mipmaps(value: bool)

  * bool is_using_mipmaps()

If `true`, calculates mipmaps for the backbuffer before drawing the
CanvasGroup so that mipmaps can be used in a custom ShaderMaterial attached to
the CanvasGroup. Generating mipmaps has a performance cost so this should not
be enabled unless required.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

