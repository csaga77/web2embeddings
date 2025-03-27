# MeshInstance2D

Inherits: Node2D < CanvasItem < Node < Object

Node used for displaying a Mesh in 2D.

## Description

Node used for displaying a Mesh in 2D. A MeshInstance2D can be automatically
created from an existing Sprite2D via a tool in the editor toolbar. Select the
Sprite2D node, then choose Sprite2D > Convert to MeshInstance2D at the top of
the 2D editor viewport.

## Tutorials

  * 2D meshes

## Properties

Mesh | mesh  
---|---  
Texture2D | texture  
  
## Signals

texture_changed()

Emitted when the texture is changed.

## Property Descriptions

Mesh mesh

  * void set_mesh(value: Mesh)

  * Mesh get_mesh()

The Mesh that will be drawn by the MeshInstance2D.

Texture2D texture

  * void set_texture(value: Texture2D)

  * Texture2D get_texture()

The Texture2D that will be used if using the default CanvasItemMaterial. Can
be accessed as `TEXTURE` in CanvasItem shader.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

