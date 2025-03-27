# RDPipelineSpecializationConstant

Inherits: RefCounted < Object

Pipeline specialization constant (used by RenderingDevice).

## Description

A specialization constant is a way to create additional variants of shaders
without actually increasing the number of shader versions that are compiled.
This allows improving performance by reducing the number of shader versions
and reducing `if` branching, while still allowing shaders to be flexible for
different use cases.

This object is used by RenderingDevice.

## Properties

int | constant_id | `0`  
---|---|---  
Variant | value  
  
## Property Descriptions

int constant_id = `0`

  * void set_constant_id(value: int)

  * int get_constant_id()

The identifier of the specialization constant. This is a value starting from
`0` and that increments for every different specialization constant for a
given shader.

Variant value

  * void set_value(value: Variant)

  * Variant get_value()

The specialization constant's value. Only bool, int and float types are valid
for specialization constants.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

