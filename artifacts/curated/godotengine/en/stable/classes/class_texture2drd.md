# Texture2DRD

Inherits: Texture2D < Texture < Resource < RefCounted < Object

Texture for 2D that is bound to a texture created on the RenderingDevice.

## Description

This texture class allows you to use a 2D texture created directly on the
RenderingDevice as a texture for materials, meshes, etc.

## Properties

bool | resource_local_to_scene | `false` (overrides Resource)  
---|---|---  
RID | texture_rd_rid  
  
## Property Descriptions

RID texture_rd_rid

  * void set_texture_rd_rid(value: RID)

  * RID get_texture_rd_rid()

The RID of the texture object created on the RenderingDevice.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

