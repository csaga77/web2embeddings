# RDShaderSPIRV

Inherits: Resource < RefCounted < Object

SPIR-V intermediate representation as part of a RDShaderFile (used by
RenderingDevice).

## Description

RDShaderSPIRV represents a RDShaderFile's SPIR-V code for various shader
stages, as well as possible compilation error messages. SPIR-V is a low-level
intermediate shader representation. This intermediate representation is not
used directly by GPUs for rendering, but it can be compiled into binary
shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable
across GPU models and driver versions.

This object is used by RenderingDevice.

## Properties

PackedByteArray | bytecode_compute | `PackedByteArray()`  
---|---|---  
PackedByteArray | bytecode_fragment | `PackedByteArray()`  
PackedByteArray | bytecode_tesselation_control | `PackedByteArray()`  
PackedByteArray | bytecode_tesselation_evaluation | `PackedByteArray()`  
PackedByteArray | bytecode_vertex | `PackedByteArray()`  
String | compile_error_compute | `""`  
String | compile_error_fragment | `""`  
String | compile_error_tesselation_control | `""`  
String | compile_error_tesselation_evaluation | `""`  
String | compile_error_vertex | `""`  
  
## Methods

PackedByteArray | get_stage_bytecode(stage: ShaderStage) const  
---|---  
String | get_stage_compile_error(stage: ShaderStage) const  
void | set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)  
void | set_stage_compile_error(stage: ShaderStage, compile_error: String)  
  
## Property Descriptions

PackedByteArray bytecode_compute = `PackedByteArray()`

  * void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

  * PackedByteArray get_stage_bytecode(stage: ShaderStage) const

The SPIR-V bytecode for the compute shader stage.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

PackedByteArray bytecode_fragment = `PackedByteArray()`

  * void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

  * PackedByteArray get_stage_bytecode(stage: ShaderStage) const

The SPIR-V bytecode for the fragment shader stage.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

PackedByteArray bytecode_tesselation_control = `PackedByteArray()`

  * void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

  * PackedByteArray get_stage_bytecode(stage: ShaderStage) const

The SPIR-V bytecode for the tessellation control shader stage.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

PackedByteArray bytecode_tesselation_evaluation = `PackedByteArray()`

  * void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

  * PackedByteArray get_stage_bytecode(stage: ShaderStage) const

The SPIR-V bytecode for the tessellation evaluation shader stage.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

PackedByteArray bytecode_vertex = `PackedByteArray()`

  * void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

  * PackedByteArray get_stage_bytecode(stage: ShaderStage) const

The SPIR-V bytecode for the vertex shader stage.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedByteArray for more details.

String compile_error_compute = `""`

  * void set_stage_compile_error(stage: ShaderStage, compile_error: String)

  * String get_stage_compile_error(stage: ShaderStage) const

The compilation error message for the compute shader stage (set by the SPIR-V
compiler and Godot). If empty, shader compilation was successful.

String compile_error_fragment = `""`

  * void set_stage_compile_error(stage: ShaderStage, compile_error: String)

  * String get_stage_compile_error(stage: ShaderStage) const

The compilation error message for the fragment shader stage (set by the SPIR-V
compiler and Godot). If empty, shader compilation was successful.

String compile_error_tesselation_control = `""`

  * void set_stage_compile_error(stage: ShaderStage, compile_error: String)

  * String get_stage_compile_error(stage: ShaderStage) const

The compilation error message for the tessellation control shader stage (set
by the SPIR-V compiler and Godot). If empty, shader compilation was
successful.

String compile_error_tesselation_evaluation = `""`

  * void set_stage_compile_error(stage: ShaderStage, compile_error: String)

  * String get_stage_compile_error(stage: ShaderStage) const

The compilation error message for the tessellation evaluation shader stage
(set by the SPIR-V compiler and Godot). If empty, shader compilation was
successful.

String compile_error_vertex = `""`

  * void set_stage_compile_error(stage: ShaderStage, compile_error: String)

  * String get_stage_compile_error(stage: ShaderStage) const

The compilation error message for the vertex shader stage (set by the SPIR-V
compiler and Godot). If empty, shader compilation was successful.

## Method Descriptions

PackedByteArray get_stage_bytecode(stage: ShaderStage) const

Equivalent to getting one of bytecode_compute, bytecode_fragment,
bytecode_tesselation_control, bytecode_tesselation_evaluation,
bytecode_vertex.

String get_stage_compile_error(stage: ShaderStage) const

Returns the compilation error message for the given shader `stage`. Equivalent
to getting one of compile_error_compute, compile_error_fragment,
compile_error_tesselation_control, compile_error_tesselation_evaluation,
compile_error_vertex.

void set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to setting
one of bytecode_compute, bytecode_fragment, bytecode_tesselation_control,
bytecode_tesselation_evaluation, bytecode_vertex.

void set_stage_compile_error(stage: ShaderStage, compile_error: String)

Sets the compilation error message for the given shader `stage` to
`compile_error`. Equivalent to setting one of compile_error_compute,
compile_error_fragment, compile_error_tesselation_control,
compile_error_tesselation_evaluation, compile_error_vertex.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

