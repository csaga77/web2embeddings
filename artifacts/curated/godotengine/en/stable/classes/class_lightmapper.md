# Lightmapper

Inherits: RefCounted < Object

Inherited By: LightmapperRD

Abstract class extended by lightmappers, for use in LightmapGI.

## Description

This class should be extended by custom lightmapper classes. Lightmappers can
then be used with LightmapGI to provide fast baked global illumination in 3D.

Godot contains a built-in GPU-based lightmapper LightmapperRD that uses
compute shaders, but custom lightmappers can be implemented by C++ modules.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

