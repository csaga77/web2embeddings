# UniformSetCacheRD

Inherits: Object

Uniform set cache manager for Rendering Device based renderers.

## Description

Uniform set cache manager for Rendering Device based renderers. Provides a way
to create a uniform set and reuse it in subsequent calls for as long as the
uniform set exists. Uniform set will automatically be cleaned up when
dependent objects are freed.

## Methods

RID | get_cache(shader: RID, set: int, uniforms: Array[RDUniform]) static  
---|---  
  
## Method Descriptions

RID get_cache(shader: RID, set: int, uniforms: Array[RDUniform]) static

Creates/returns a cached uniform set based on the provided uniforms for a
given shader.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.

