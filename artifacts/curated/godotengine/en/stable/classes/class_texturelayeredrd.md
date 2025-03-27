# TextureLayeredRD

Inherits: TextureLayered < Texture < Resource < RefCounted < Object

Inherited By: Texture2DArrayRD, TextureCubemapArrayRD, TextureCubemapRD

Abstract base class for layered texture RD types.

## Description

Base class for Texture2DArrayRD, TextureCubemapRD and TextureCubemapArrayRD.
Cannot be used directly, but contains all the functions necessary for
accessing the derived resource types.

## Properties

RID | texture_rd_rid  
---|---  
  
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

