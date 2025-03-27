# ShaderMaterial

Inherits: Material < Resource < RefCounted < Object

A material defined by a custom Shader program and the values of its shader
parameters.

## Description

A material that uses a custom Shader program to render visual items (canvas
items, meshes, skies, fog), or to process particles. Compared to other
materials, ShaderMaterial gives deeper control over the generated shader code.
For more information, see the shaders documentation index below.

Multiple ShaderMaterials can use the same shader and configure different
values for the shader uniforms.

Note: For performance reasons, the Resource.changed signal is only emitted
when the Resource.resource_name changes. Only in editor, it is also emitted
for shader changes.

## Tutorials

  * Shaders documentation index

## Properties

Shader | shader  
---|---  
  
## Methods

Variant | get_shader_parameter(param: StringName) const  
---|---  
void | set_shader_parameter(param: StringName, value: Variant)  
  
## Property Descriptions

Shader shader

  * void set_shader(value: Shader)

  * Shader get_shader()

The Shader program used to render this material.

## Method Descriptions

Variant get_shader_parameter(param: StringName) const

Returns the current value set for this material of a uniform in the shader.

void set_shader_parameter(param: StringName, value: Variant)

Changes the value set for this material of a uniform in the shader.

Note: `param` is case-sensitive and must match the name of the uniform in the
code exactly (not the capitalized name in the inspector).

Note: Changes to the shader uniform will be effective on all instances using
this ShaderMaterial. To prevent this, use per-instance uniforms with
GeometryInstance3D.set_instance_shader_parameter() or duplicate the
ShaderMaterial resource using Resource.duplicate(). Per-instance uniforms
allow for better shader reuse and are therefore faster, so they should be
preferred over duplicating the ShaderMaterial when possible.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

