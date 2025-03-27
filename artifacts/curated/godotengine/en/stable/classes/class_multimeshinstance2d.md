# MultiMeshInstance2D

Inherits: Node2D < CanvasItem < Node < Object

Node that instances a MultiMesh in 2D.

## Description

MultiMeshInstance2D is a specialized node to instance a MultiMesh resource in
2D.

Usage is the same as MultiMeshInstance3D.

## Properties

MultiMesh | multimesh  
---|---  
Texture2D | texture  
  
## Signals

texture_changed()

Emitted when the texture is changed.

## Property Descriptions

MultiMesh multimesh

  * void set_multimesh(value: MultiMesh)

  * MultiMesh get_multimesh()

The MultiMesh that will be drawn by the MultiMeshInstance2D.

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

