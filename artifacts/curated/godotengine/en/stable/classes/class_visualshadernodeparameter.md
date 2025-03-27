# VisualShaderNodeParameter

Inherits: VisualShaderNode < Resource < RefCounted < Object

Inherited By: VisualShaderNodeBooleanParameter,
VisualShaderNodeColorParameter, VisualShaderNodeFloatParameter,
VisualShaderNodeIntParameter, VisualShaderNodeTextureParameter,
VisualShaderNodeTransformParameter, VisualShaderNodeUIntParameter,
VisualShaderNodeVec2Parameter, VisualShaderNodeVec3Parameter,
VisualShaderNodeVec4Parameter

A base type for the parameters within the visual shader graph.

## Description

A parameter represents a variable in the shader which is set externally, i.e.
from the ShaderMaterial. Parameters are exposed as properties in the
ShaderMaterial and can be assigned from the Inspector or from a script.

## Properties

String | parameter_name | `""`  
---|---|---  
Qualifier | qualifier | `0`  
  
## Enumerations

enum Qualifier:

Qualifier QUAL_NONE = `0`

The parameter will be tied to the ShaderMaterial using this shader.

Qualifier QUAL_GLOBAL = `1`

The parameter will use a global value, defined in Project Settings.

Qualifier QUAL_INSTANCE = `2`

The parameter will be tied to the node with attached ShaderMaterial using this
shader.

Qualifier QUAL_MAX = `3`

Represents the size of the Qualifier enum.

## Property Descriptions

String parameter_name = `""`

  * void set_parameter_name(value: String)

  * String get_parameter_name()

Name of the parameter, by which it can be accessed through the ShaderMaterial
properties.

Qualifier qualifier = `0`

  * void set_qualifier(value: Qualifier)

  * Qualifier get_qualifier()

Defines the scope of the parameter.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

