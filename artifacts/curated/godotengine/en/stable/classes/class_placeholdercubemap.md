# PlaceholderCubemap

Inherits: PlaceholderTextureLayered < TextureLayered < Texture < Resource <
RefCounted < Object

A Cubemap without image data.

## Description

This class replaces a Cubemap or a Cubemap-derived class in 2 conditions:

  * In dedicated server mode, where the image data shouldn't affect game logic. This allows reducing the exported PCK's size significantly.

  * When the Cubemap-derived class is missing, for example when using a different engine version.

Note: This class is not intended for rendering or for use in shaders.
Operations like calculating UV are not guaranteed to work.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

