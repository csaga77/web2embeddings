# ShaderIncludeDB

Inherits: Object

Internal database of built in shader include files.

## Description

This object contains shader fragments from Godot's internal shaders. These can
be used when access to internal uniform buffers and/or internal functions is
required for instance when composing compositor effects or compute shaders.
Only fragments for the current rendering device are loaded.

## Methods

String | get_built_in_include_file(filename: String) static  
---|---  
bool | has_built_in_include_file(filename: String) static  
PackedStringArray | list_built_in_include_files() static  
  
## Method Descriptions

String get_built_in_include_file(filename: String) static

Returns the code for the built-in shader fragment. You can also access this in
your shader code through `#include "filename"`.

bool has_built_in_include_file(filename: String) static

Returns `true` if an include file with this name exists.

PackedStringArray list_built_in_include_files() static

Returns a list of built-in include files that are currently registered.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.

