# EditorExportPreset

Inherits: RefCounted < Object

Export preset configuration.

## Description

Export preset configuration. Instances of EditorExportPreset by editor UI and
intended to be used a read-only configuration passed to the
EditorExportPlatform methods when exporting the project.

## Methods

bool | are_advanced_options_enabled() const  
---|---  
String | get_custom_features() const  
Dictionary | get_customized_files() const  
int | get_customized_files_count() const  
bool | get_encrypt_directory() const  
bool | get_encrypt_pck() const  
String | get_encryption_ex_filter() const  
String | get_encryption_in_filter() const  
String | get_encryption_key() const  
String | get_exclude_filter() const  
ExportFilter | get_export_filter() const  
String | get_export_path() const  
FileExportMode | get_file_export_mode(path: String, default: FileExportMode = 0) const  
PackedStringArray | get_files_to_export() const  
String | get_include_filter() const  
Variant | get_or_env(name: StringName, env_var: String) const  
PackedStringArray | get_patches() const  
String | get_preset_name() const  
int | get_script_export_mode() const  
String | get_version(name: StringName, windows_version: bool) const  
bool | has(property: StringName) const  
bool | has_export_file(path: String)  
bool | is_dedicated_server() const  
bool | is_runnable() const  
  
## Enumerations

enum ExportFilter:

ExportFilter EXPORT_ALL_RESOURCES = `0`

There is currently no description for this enum. Please help us by
contributing one!

ExportFilter EXPORT_SELECTED_SCENES = `1`

There is currently no description for this enum. Please help us by
contributing one!

ExportFilter EXPORT_SELECTED_RESOURCES = `2`

There is currently no description for this enum. Please help us by
contributing one!

ExportFilter EXCLUDE_SELECTED_RESOURCES = `3`

There is currently no description for this enum. Please help us by
contributing one!

ExportFilter EXPORT_CUSTOMIZED = `4`

There is currently no description for this enum. Please help us by
contributing one!

enum FileExportMode:

FileExportMode MODE_FILE_NOT_CUSTOMIZED = `0`

There is currently no description for this enum. Please help us by
contributing one!

FileExportMode MODE_FILE_STRIP = `1`

There is currently no description for this enum. Please help us by
contributing one!

FileExportMode MODE_FILE_KEEP = `2`

There is currently no description for this enum. Please help us by
contributing one!

FileExportMode MODE_FILE_REMOVE = `3`

There is currently no description for this enum. Please help us by
contributing one!

enum ScriptExportMode:

ScriptExportMode MODE_SCRIPT_TEXT = `0`

There is currently no description for this enum. Please help us by
contributing one!

ScriptExportMode MODE_SCRIPT_BINARY_TOKENS = `1`

There is currently no description for this enum. Please help us by
contributing one!

ScriptExportMode MODE_SCRIPT_BINARY_TOKENS_COMPRESSED = `2`

There is currently no description for this enum. Please help us by
contributing one!

## Method Descriptions

bool are_advanced_options_enabled() const

Returns `true`, is "Advanced" toggle is enabled in the export dialog.

String get_custom_features() const

Returns string with a comma separated list of custom features.

Dictionary get_customized_files() const

Returns Dictionary of files selected in the "Resources" tab of the export
dialog. Dictionary keys are file names and values are export mode - `"strip`,
`"keep"`, or `"remove"`. See also get_file_export_mode().

int get_customized_files_count() const

Returns number of files selected in the "Resources" tab of the export dialog.

bool get_encrypt_directory() const

Returns `true`, PCK directory encryption is enabled in the export dialog.

bool get_encrypt_pck() const

Returns `true`, PCK encryption is enabled in the export dialog.

String get_encryption_ex_filter() const

Returns file filters to exclude during PCK encryption.

String get_encryption_in_filter() const

Returns file filters to include during PCK encryption.

String get_encryption_key() const

Returns PCK encryption key.

String get_exclude_filter() const

Returns file filters to exclude during export.

ExportFilter get_export_filter() const

Returns export file filter mode selected in the "Resources" tab of the export
dialog.

String get_export_path() const

Returns export target path.

FileExportMode get_file_export_mode(path: String, default: FileExportMode = 0)
const

Returns file export mode for the specified file.

PackedStringArray get_files_to_export() const

Returns array of files to export.

String get_include_filter() const

Returns file filters to include during export.

Variant get_or_env(name: StringName, env_var: String) const

Returns export option value or value of environment variable if it is set.

PackedStringArray get_patches() const

Returns the list of packs on which to base a patch export on.

String get_preset_name() const

Returns export preset name.

int get_script_export_mode() const

Returns script export mode.

String get_version(name: StringName, windows_version: bool) const

Returns the preset's version number, or fall back to the
ProjectSettings.application/config/version project setting if set to an empty
string.

If `windows_version` is `true`, formats the returned version number to be
compatible with Windows executable metadata.

bool has(property: StringName) const

Returns `true` if preset has specified property.

bool has_export_file(path: String)

Returns `true` if specified file is exported.

bool is_dedicated_server() const

Returns `true` if dedicated server export mode is selected in the export
dialog.

bool is_runnable() const

Returns `true` if "Runnable" toggle is enabled in the export dialog.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

