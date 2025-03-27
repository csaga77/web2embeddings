# VisualShaderNodeIf

Inherits: VisualShaderNode < Resource < RefCounted < Object

Outputs a 3D vector based on the result of a floating-point comparison within
the visual shader graph.

## Description

This visual shader node has six input ports:

  * Port 1 and 2 provide the two floating-point numbers `a` and `b` that will be compared.

  * Port 3 is the tolerance, which allows similar floating-point numbers to be considered equal.

  * Ports 4, 5, and 6 are the possible outputs, returned if `a == b`, `a > b`, or `a < b` respectively.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

