# CubemapArray

Inherits: ImageTextureLayered < TextureLayered < Texture < Resource <
RefCounted < Object

An array of Cubemaps, stored together and with a single reference.

## Description

CubemapArrays are made of an array of Cubemaps. Like Cubemaps, they are made
of multiple textures, the amount of which must be divisible by 6 (one for each
face of the cube).

The primary benefit of CubemapArrays is that they can be accessed in shader
code using a single texture reference. In other words, you can pass multiple
Cubemaps into a shader using a single CubemapArray. Cubemaps are allocated in
adjacent cache regions on the GPU, which makes CubemapArrays the most
efficient way to store multiple Cubemaps.

Godot uses CubemapArrays internally for many effects, including the Sky if you
set
ProjectSettings.rendering/reflections/sky_reflections/texture_array_reflections
to `true`.

To create such a texture file yourself, reimport your image files using the
Godot Editor import presets. To create a CubemapArray from code, use
ImageTextureLayered.create_from_images() on an instance of the CubemapArray
class.

The expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot's coordinate
system, so Y+ is "up" and Z- is "forward"). You can use one of the following
templates as a base:

  * 23 cubemap template (default layout option)

  * 32 cubemap template

  * 16 cubemap template

  * 61 cubemap template

Multiple layers are stacked on top of each other when using the default
vertical import option (with the first layer at the top). Alternatively, you
can choose an horizontal layout in the import options (with the first layer at
the left).

Note: CubemapArray is not supported in the Compatibility renderer due to
graphics API limitations.

## Methods

Resource | create_placeholder() const  
---|---  
  
## Method Descriptions

Resource create_placeholder() const

Creates a placeholder version of this resource (PlaceholderCubemapArray).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

