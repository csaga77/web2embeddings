# OpenXRCompositionLayer

Experimental: This class may be changed or removed in future versions.

Inherits: Node3D < Node < Object

Inherited By: OpenXRCompositionLayerCylinder, OpenXRCompositionLayerEquirect,
OpenXRCompositionLayerQuad

The parent class of all OpenXR composition layer nodes.

## Description

Composition layers allow 2D viewports to be displayed inside of the headset by
the XR compositor through special projections that retain their quality. This
allows for rendering clear text while keeping the layer at a native
resolution.

Note: If the OpenXR runtime doesn't support the given composition layer type,
a fallback mesh can be generated with a ViewportTexture, in order to emulate
the composition layer.

## Properties

bool | alpha_blend | `false`  
---|---|---  
Vector2i | android_surface_size | `Vector2i(1024, 1024)`  
bool | enable_hole_punch | `false`  
SubViewport | layer_viewport  
int | sort_order | `1`  
bool | use_android_surface | `false`  
  
## Methods

JavaObject | get_android_surface()  
---|---  
Vector2 | intersects_ray(origin: Vector3, direction: Vector3) const  
bool | is_natively_supported() const  
  
## Property Descriptions

bool alpha_blend = `false`

  * void set_alpha_blend(value: bool)

  * bool get_alpha_blend()

Enables the blending the layer using its alpha channel.

Can be combined with Viewport.transparent_bg to give the layer a transparent
background.

Vector2i android_surface_size = `Vector2i(1024, 1024)`

  * void set_android_surface_size(value: Vector2i)

  * Vector2i get_android_surface_size()

The size of the Android surface to create if use_android_surface is enabled.

bool enable_hole_punch = `false`

  * void set_enable_hole_punch(value: bool)

  * bool get_enable_hole_punch()

Enables a technique called "hole punching", which allows putting the
composition layer behind the main projection layer (i.e. setting sort_order to
a negative value) while "punching a hole" through everything rendered by Godot
so that the layer is still visible.

This can be used to create the illusion that the composition layer exists in
the same 3D space as everything rendered by Godot, allowing objects to appear
to pass both behind or in front of the composition layer.

SubViewport layer_viewport

  * void set_layer_viewport(value: SubViewport)

  * SubViewport get_layer_viewport()

The SubViewport to render on the composition layer.

int sort_order = `1`

  * void set_sort_order(value: int)

  * int get_sort_order()

The sort order for this composition layer. Higher numbers will be shown in
front of lower numbers.

Note: This will have no effect if a fallback mesh is being used.

bool use_android_surface = `false`

  * void set_use_android_surface(value: bool)

  * bool get_use_android_surface()

If enabled, an Android surface will be created (with the dimensions from
android_surface_size) which will provide the 2D content for the composition
layer, rather than using layer_viewport.

See get_android_surface() for information about how to get the surface so that
your application can draw to it.

Note: This will only work in Android builds.

## Method Descriptions

JavaObject get_android_surface()

Returns a JavaObject representing an `android.view.Surface` if
use_android_surface is enabled and OpenXR has created the surface. Otherwise,
this will return `null`.

Note: The surface can only be created during an active OpenXR session. So, if
use_android_surface is enabled outside of an OpenXR session, it won't be
created until a new session fully starts.

Vector2 intersects_ray(origin: Vector3, direction: Vector3) const

Returns UV coordinates where the given ray intersects with the composition
layer. `origin` and `direction` must be in global space.

Returns `Vector2(-1.0, -1.0)` if the ray doesn't intersect.

bool is_natively_supported() const

Returns `true` if the OpenXR runtime natively supports this composition layer
type.

Note: This will only return an accurate result after the OpenXR session has
started.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

