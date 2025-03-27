# PlaceholderMaterial

Inherits: Material < Resource < RefCounted < Object

Placeholder class for a material.

## Description

This class is used when loading a project that uses a Material subclass in 2
conditions:

  * When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

  * When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

