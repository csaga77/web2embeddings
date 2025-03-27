# ViewportTexture

Inherits: Texture2D < Texture < Resource < RefCounted < Object

Provides the content of a Viewport as a dynamic texture.

## Description

A ViewportTexture provides the content of a Viewport as a dynamic Texture2D.
This can be used to combine the rendering of Control, Node2D and Node3D nodes.
For example, you can use this texture to display a 3D scene inside a
TextureRect, or a 2D overlay in a Sprite3D.

To get a ViewportTexture in code, use the Viewport.get_texture() method on the
target viewport.

Note: A ViewportTexture is always local to its scene (see
Resource.resource_local_to_scene). If the scene root is not ready, it may
return incorrect data (see Node.ready).

Note: Instantiating scenes containing a high-resolution ViewportTexture may
cause noticeable stutter.

Note: When using a Viewport with Viewport.use_hdr_2d set to `true`, the
returned texture will be an HDR image encoded in linear space. This may look
darker than normal when displayed directly on screen. To convert to gamma
space, you can do the following:

    
    
    img.convert(Image.FORMAT_RGBA8)
    imb.linear_to_srgb()
    

Note: Some nodes such as Decal, Light3D, and PointLight2D do not support using
ViewportTexture directly. To use texture data from a ViewportTexture in these
nodes, you need to create an ImageTexture by calling Texture2D.get_image() on
the ViewportTexture and passing the result to
ImageTexture.create_from_image(). This conversion is a slow operation, so it
should not be performed every frame.

## Tutorials

  * GUI in 3D Viewport Demo

  * 3D in 2D Viewport Demo

  * 2D in 3D Viewport Demo

  * 3D Resolution Scaling Demo

## Properties

NodePath | viewport_path | `NodePath("")`  
---|---|---  
  
## Property Descriptions

NodePath viewport_path = `NodePath("")`

  * void set_viewport_path_in_scene(value: NodePath)

  * NodePath get_viewport_path_in_scene()

The path to the Viewport node to display. This is relative to the local scene
root (see Resource.get_local_scene()), not to the nodes that use this texture.

Note: In the editor, this path is automatically updated when the target
viewport or one of its ancestors is renamed or moved. At runtime, this path
may not automatically update if the scene root cannot be found.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

