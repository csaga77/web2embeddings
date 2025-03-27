# CapsuleMesh

Inherits: PrimitiveMesh < Mesh < Resource < RefCounted < Object

Class representing a capsule-shaped PrimitiveMesh.

## Description

Class representing a capsule-shaped PrimitiveMesh.

## Properties

float | height | `2.0`  
---|---|---  
int | radial_segments | `64`  
float | radius | `0.5`  
int | rings | `8`  
  
## Property Descriptions

float height = `2.0`

  * void set_height(value: float)

  * float get_height()

Total height of the capsule mesh (including the hemispherical ends).

int radial_segments = `64`

  * void set_radial_segments(value: int)

  * int get_radial_segments()

Number of radial segments on the capsule mesh.

float radius = `0.5`

  * void set_radius(value: float)

  * float get_radius()

Radius of the capsule mesh.

int rings = `8`

  * void set_rings(value: int)

  * int get_rings()

Number of rings along the height of the capsule.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

