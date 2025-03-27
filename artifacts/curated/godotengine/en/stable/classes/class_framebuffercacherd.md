# FramebufferCacheRD

Inherits: Object

Framebuffer cache manager for Rendering Device based renderers.

## Description

Framebuffer cache manager for Rendering Device based renderers. Provides a way
to create a framebuffer and reuse it in subsequent calls for as long as the
used textures exists. Framebuffers will automatically be cleaned up when
dependent objects are freed.

## Methods

RID | get_cache_multipass(textures: Array[RID], passes: Array[RDFramebufferPass], views: int) static  
---|---  
  
## Method Descriptions

RID get_cache_multipass(textures: Array[RID], passes:
Array[RDFramebufferPass], views: int) static

Creates, or obtains a cached, framebuffer. `textures` lists textures accessed.
`passes` defines the subpasses and texture allocation, if left empty a single
pass is created and textures are allocated depending on their usage flags.
`views` defines the number of views used when rendering.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.

