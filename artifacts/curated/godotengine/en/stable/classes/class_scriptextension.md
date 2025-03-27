# ScriptExtension

Inherits: Script < Resource < RefCounted < Object

There is currently no description for this class. Please help us by
contributing one!

## Methods

bool | _can_instantiate() virtual const  
---|---  
bool | _editor_can_reload_from_file() virtual  
Script | _get_base_script() virtual const  
String | _get_class_icon_path() virtual const  
Dictionary | _get_constants() virtual const  
StringName | _get_doc_class_name() virtual const  
Array[Dictionary] | _get_documentation() virtual const  
StringName | _get_global_name() virtual const  
StringName | _get_instance_base_type() virtual const  
ScriptLanguage | _get_language() virtual const  
int | _get_member_line(member: StringName) virtual const  
Array[StringName] | _get_members() virtual const  
Dictionary | _get_method_info(method: StringName) virtual const  
Variant | _get_property_default_value(property: StringName) virtual const  
Variant | _get_rpc_config() virtual const  
Variant | _get_script_method_argument_count(method: StringName) virtual const  
Array[Dictionary] | _get_script_method_list() virtual const  
Array[Dictionary] | _get_script_property_list() virtual const  
Array[Dictionary] | _get_script_signal_list() virtual const  
String | _get_source_code() virtual const  
bool | _has_method(method: StringName) virtual const  
bool | _has_property_default_value(property: StringName) virtual const  
bool | _has_script_signal(signal: StringName) virtual const  
bool | _has_source_code() virtual const  
bool | _has_static_method(method: StringName) virtual const  
bool | _inherits_script(script: Script) virtual const  
`void*` | _instance_create(for_object: Object) virtual const  
bool | _instance_has(object: Object) virtual const  
bool | _is_abstract() virtual const  
bool | _is_placeholder_fallback_enabled() virtual const  
bool | _is_tool() virtual const  
bool | _is_valid() virtual const  
void | _placeholder_erased(placeholder: `void*`) virtual  
`void*` | _placeholder_instance_create(for_object: Object) virtual const  
Error | _reload(keep_state: bool) virtual  
void | _set_source_code(code: String) virtual  
void | _update_exports() virtual  
  
## Method Descriptions

bool _can_instantiate() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _editor_can_reload_from_file() virtual

There is currently no description for this method. Please help us by
contributing one!

Script _get_base_script() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_class_icon_path() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _get_constants() virtual const

There is currently no description for this method. Please help us by
contributing one!

StringName _get_doc_class_name() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_documentation() virtual const

There is currently no description for this method. Please help us by
contributing one!

StringName _get_global_name() virtual const

There is currently no description for this method. Please help us by
contributing one!

StringName _get_instance_base_type() virtual const

There is currently no description for this method. Please help us by
contributing one!

ScriptLanguage _get_language() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_member_line(member: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[StringName] _get_members() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _get_method_info(method: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _get_property_default_value(property: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _get_rpc_config() virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _get_script_method_argument_count(method: StringName) virtual const

Return the expected argument count for the given `method`, or `null` if it
can't be determined (which will then fall back to the default behavior).

Array[Dictionary] _get_script_method_list() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_script_property_list() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_script_signal_list() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_source_code() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_method(method: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_property_default_value(property: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_script_signal(signal: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_source_code() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_static_method(method: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _inherits_script(script: Script) virtual const

There is currently no description for this method. Please help us by
contributing one!

`void*` _instance_create(for_object: Object) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _instance_has(object: Object) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_abstract() virtual const

Returns `true` if the script is an abstract script. An abstract script does
not have a constructor and cannot be instantiated.

bool _is_placeholder_fallback_enabled() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_tool() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_valid() virtual const

There is currently no description for this method. Please help us by
contributing one!

void _placeholder_erased(placeholder: `void*`) virtual

There is currently no description for this method. Please help us by
contributing one!

`void*` _placeholder_instance_create(for_object: Object) virtual const

There is currently no description for this method. Please help us by
contributing one!

Error _reload(keep_state: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_source_code(code: String) virtual

There is currently no description for this method. Please help us by
contributing one!

void _update_exports() virtual

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

