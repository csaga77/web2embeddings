# EditorFileDialog

Inherits: ConfirmationDialog < AcceptDialog < Window < Viewport < Node <
Object

A modified version of FileDialog used by the editor.

## Description

EditorFileDialog is an enhanced version of FileDialog available only to editor
plugins. Additional features include list of favorited/recent files and the
ability to see files as thumbnails grid instead of list.

Unlike FileDialog, EditorFileDialog does not have a property for using native
dialogs. Instead, native dialogs can be enabled globally via the
EditorSettings.interface/editor/use_native_file_dialogs editor setting. They
are also enabled automatically when running in sandbox (e.g. on macOS).

## Properties

Access | access | `0`  
---|---|---  
String | current_dir  
String | current_file  
String | current_path  
bool | dialog_hide_on_ok | `false` (overrides AcceptDialog)  
bool | disable_overwrite_warning | `false`  
DisplayMode | display_mode | `0`  
FileMode | file_mode | `4`  
PackedStringArray | filters | `PackedStringArray()`  
int | option_count | `0`  
bool | show_hidden_files | `false`  
String | title | `"Save a File"` (overrides Window)  
  
## Methods

void | add_filter(filter: String, description: String = "")  
---|---  
void | add_option(name: String, values: PackedStringArray, default_value_index: int)  
void | add_side_menu(menu: Control, title: String = "")  
void | clear_filename_filter()  
void | clear_filters()  
String | get_filename_filter() const  
LineEdit | get_line_edit()  
int | get_option_default(option: int) const  
String | get_option_name(option: int) const  
PackedStringArray | get_option_values(option: int) const  
Dictionary | get_selected_options() const  
VBoxContainer | get_vbox()  
void | invalidate()  
void | popup_file_dialog()  
void | set_filename_filter(filter: String)  
void | set_option_default(option: int, default_value_index: int)  
void | set_option_name(option: int, name: String)  
void | set_option_values(option: int, values: PackedStringArray)  
  
## Signals

dir_selected(dir: String)

Emitted when a directory is selected.

file_selected(path: String)

Emitted when a file is selected.

filename_filter_changed(filter: String)

Emitted when the filter for file names changes.

files_selected(paths: PackedStringArray)

Emitted when multiple files are selected.

## Enumerations

enum FileMode:

FileMode FILE_MODE_OPEN_FILE = `0`

The EditorFileDialog can select only one file. Accepting the window will open
the file.

FileMode FILE_MODE_OPEN_FILES = `1`

The EditorFileDialog can select multiple files. Accepting the window will open
all files.

FileMode FILE_MODE_OPEN_DIR = `2`

The EditorFileDialog can select only one directory. Accepting the window will
open the directory.

FileMode FILE_MODE_OPEN_ANY = `3`

The EditorFileDialog can select a file or directory. Accepting the window will
open it.

FileMode FILE_MODE_SAVE_FILE = `4`

The EditorFileDialog can select only one file. Accepting the window will save
the file.

enum Access:

Access ACCESS_RESOURCES = `0`

The EditorFileDialog can only view `res://` directory contents.

Access ACCESS_USERDATA = `1`

The EditorFileDialog can only view `user://` directory contents.

Access ACCESS_FILESYSTEM = `2`

The EditorFileDialog can view the entire local file system.

enum DisplayMode:

DisplayMode DISPLAY_THUMBNAILS = `0`

The EditorFileDialog displays resources as thumbnails.

DisplayMode DISPLAY_LIST = `1`

The EditorFileDialog displays resources as a list of filenames.

## Property Descriptions

Access access = `0`

  * void set_access(value: Access)

  * Access get_access()

The location from which the user may select a file, including `res://`,
`user://`, and the local file system.

String current_dir

  * void set_current_dir(value: String)

  * String get_current_dir()

The currently occupied directory.

String current_file

  * void set_current_file(value: String)

  * String get_current_file()

The currently selected file.

String current_path

  * void set_current_path(value: String)

  * String get_current_path()

The file system path in the address bar.

bool disable_overwrite_warning = `false`

  * void set_disable_overwrite_warning(value: bool)

  * bool is_overwrite_warning_disabled()

If `true`, the EditorFileDialog will not warn the user before overwriting
files.

DisplayMode display_mode = `0`

  * void set_display_mode(value: DisplayMode)

  * DisplayMode get_display_mode()

The view format in which the EditorFileDialog displays resources to the user.

FileMode file_mode = `4`

  * void set_file_mode(value: FileMode)

  * FileMode get_file_mode()

The dialog's open or save mode, which affects the selection behavior. See
FileMode.

PackedStringArray filters = `PackedStringArray()`

  * void set_filters(value: PackedStringArray)

  * PackedStringArray get_filters()

The available file type filters. For example, this shows only `.png` and `.gd`
files: `set_filters(PackedStringArray(["*.png ; PNG Images","*.gd ; GDScript
Files"]))`. Multiple file types can also be specified in a single filter.
`"*.png, *.jpg, *.jpeg ; Supported Images"` will show both PNG and JPEG files
when selected.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedStringArray for more details.

int option_count = `0`

  * void set_option_count(value: int)

  * int get_option_count()

The number of additional OptionButtons and CheckBoxes in the dialog.

bool show_hidden_files = `false`

  * void set_show_hidden_files(value: bool)

  * bool is_showing_hidden_files()

If `true`, hidden files and directories will be visible in the
EditorFileDialog. This property is synchronized with
EditorSettings.filesystem/file_dialog/show_hidden_files.

## Method Descriptions

void add_filter(filter: String, description: String = "")

Adds a comma-delimited file name `filter` option to the EditorFileDialog with
an optional `description`, which restricts what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename and
extension can be `*` to match any string. Filters starting with `.` (i.e.
empty filenames) are not allowed.

For example, a `filter` of `"*.tscn, *.scn"` and a `description` of `"Scenes"`
results in filter text "Scenes (*.tscn, *.scn)".

void add_option(name: String, values: PackedStringArray, default_value_index:
int)

Adds an additional OptionButton to the file dialog. If `values` is empty, a
CheckBox is added instead.

`default_value_index` should be an index of the value in the `values`. If
`values` is empty it should be either `1` (checked), or `0` (unchecked).

void add_side_menu(menu: Control, title: String = "")

Adds the given `menu` to the side of the file dialog with the given `title`
text on top. Only one side menu is allowed.

void clear_filename_filter()

Clear the filter for file names.

void clear_filters()

Removes all filters except for "All Files (*.*)".

String get_filename_filter() const

Returns the value of the filter for file names.

LineEdit get_line_edit()

Returns the LineEdit for the selected file.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to hide it or any of its children, use their
CanvasItem.visible property.

int get_option_default(option: int) const

Returns the default value index of the OptionButton or CheckBox with index
`option`.

String get_option_name(option: int) const

Returns the name of the OptionButton or CheckBox with index `option`.

PackedStringArray get_option_values(option: int) const

Returns an array of values of the OptionButton with index `option`.

Dictionary get_selected_options() const

Returns a Dictionary with the selected values of the additional OptionButtons
and/or CheckBoxes. Dictionary keys are names and values are selected value
indices.

VBoxContainer get_vbox()

Returns the VBoxContainer used to display the file system.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to hide it or any of its children, use their
CanvasItem.visible property.

void invalidate()

Notify the EditorFileDialog that its view of the data is no longer accurate.
Updates the view contents on next view update.

void popup_file_dialog()

Shows the EditorFileDialog at the default size and position for file dialogs
in the editor, and selects the file name if there is a current file.

void set_filename_filter(filter: String)

Sets the value of the filter for file names.

void set_option_default(option: int, default_value_index: int)

Sets the default value index of the OptionButton or CheckBox with index
`option`.

void set_option_name(option: int, name: String)

Sets the name of the OptionButton or CheckBox with index `option`.

void set_option_values(option: int, values: PackedStringArray)

Sets the option values of the OptionButton with index `option`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

