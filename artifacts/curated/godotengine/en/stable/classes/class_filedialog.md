# FileDialog

Inherits: ConfirmationDialog < AcceptDialog < Window < Viewport < Node <
Object

A dialog for selecting files or directories in the filesystem.

## Description

FileDialog is a preset dialog used to choose files and directories in the
filesystem. It supports filter masks. FileDialog automatically sets its window
title according to the file_mode. If you want to use a custom title, disable
this by setting mode_overrides_title to `false`.

## Properties

Access | access | `0`  
---|---|---  
String | current_dir  
String | current_file  
String | current_path  
bool | dialog_hide_on_ok | `false` (overrides AcceptDialog)  
FileMode | file_mode | `4`  
String | filename_filter | `""`  
PackedStringArray | filters | `PackedStringArray()`  
bool | mode_overrides_title | `true`  
String | ok_button_text | `"Save"` (overrides AcceptDialog)  
int | option_count | `0`  
String | root_subfolder | `""`  
bool | show_hidden_files | `false`  
Vector2i | size | `Vector2i(640, 360)` (overrides Window)  
String | title | `"Save a File"` (overrides Window)  
bool | use_native_dialog | `false`  
  
## Methods

void | add_filter(filter: String, description: String = "")  
---|---  
void | add_option(name: String, values: PackedStringArray, default_value_index: int)  
void | clear_filename_filter()  
void | clear_filters()  
void | deselect_all()  
LineEdit | get_line_edit()  
int | get_option_default(option: int) const  
String | get_option_name(option: int) const  
PackedStringArray | get_option_values(option: int) const  
Dictionary | get_selected_options() const  
VBoxContainer | get_vbox()  
void | invalidate()  
void | set_option_default(option: int, default_value_index: int)  
void | set_option_name(option: int, name: String)  
void | set_option_values(option: int, values: PackedStringArray)  
  
## Theme Properties

Color | file_disabled_color | `Color(1, 1, 1, 0.25)`  
---|---|---  
Color | file_icon_color | `Color(1, 1, 1, 1)`  
Color | folder_icon_color | `Color(1, 1, 1, 1)`  
Texture2D | back_folder  
Texture2D | create_folder  
Texture2D | file  
Texture2D | folder  
Texture2D | forward_folder  
Texture2D | parent_folder  
Texture2D | reload  
Texture2D | toggle_filename_filter  
Texture2D | toggle_hidden  
  
## Signals

dir_selected(dir: String)

Emitted when the user selects a directory.

file_selected(path: String)

Emitted when the user selects a file by double-clicking it or pressing the OK
button.

filename_filter_changed(filter: String)

Emitted when the filter for file names changes.

files_selected(paths: PackedStringArray)

Emitted when the user selects multiple files.

## Enumerations

enum FileMode:

FileMode FILE_MODE_OPEN_FILE = `0`

The dialog allows selecting one, and only one file.

FileMode FILE_MODE_OPEN_FILES = `1`

The dialog allows selecting multiple files.

FileMode FILE_MODE_OPEN_DIR = `2`

The dialog only allows selecting a directory, disallowing the selection of any
file.

FileMode FILE_MODE_OPEN_ANY = `3`

The dialog allows selecting one file or directory.

FileMode FILE_MODE_SAVE_FILE = `4`

The dialog will warn when a file exists.

enum Access:

Access ACCESS_RESOURCES = `0`

The dialog only allows accessing files under the Resource path (`res://`).

Access ACCESS_USERDATA = `1`

The dialog only allows accessing files under user data path (`user://`).

Access ACCESS_FILESYSTEM = `2`

The dialog allows accessing files on the whole file system.

## Property Descriptions

Access access = `0`

  * void set_access(value: Access)

  * Access get_access()

The file system access scope. See Access constants.

Warning: In Web builds, FileDialog cannot access the host file system. In
sandboxed Linux and macOS environments, use_native_dialog is automatically
used to allow limited access to host file system.

String current_dir

  * void set_current_dir(value: String)

  * String get_current_dir()

The current working directory of the file dialog.

Note: For native file dialogs, this property is only treated as a hint and may
not be respected by specific OS implementations.

String current_file

  * void set_current_file(value: String)

  * String get_current_file()

The currently selected file of the file dialog.

String current_path

  * void set_current_path(value: String)

  * String get_current_path()

The currently selected file path of the file dialog.

FileMode file_mode = `4`

  * void set_file_mode(value: FileMode)

  * FileMode get_file_mode()

The dialog's open or save mode, which affects the selection behavior. See
FileMode.

String filename_filter = `""`

  * void set_filename_filter(value: String)

  * String get_filename_filter()

The filter for file names (case-insensitive). When set to a non-empty string,
only files that contains the substring will be shown. filename_filter can be
edited by the user with the filter button at the top of the file dialog.

See also filters, which should be used to restrict the file types that can be
selected instead of filename_filter which is meant to be set by the user.

PackedStringArray filters = `PackedStringArray()`

  * void set_filters(value: PackedStringArray)

  * PackedStringArray get_filters()

The available file type filters. Each filter string in the array should be
formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`.
The description text of the filter is optional and can be omitted. Both file
extensions and MIME type should be always set.

Note: Embedded file dialog and Windows file dialog support only file
extensions, while Android, Linux, and macOS file dialogs also support MIME
types.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedStringArray for more details.

bool mode_overrides_title = `true`

  * void set_mode_overrides_title(value: bool)

  * bool is_mode_overriding_title()

If `true`, changing the file_mode property will set the window title
accordingly (e.g. setting file_mode to FILE_MODE_OPEN_FILE will change the
window title to "Open a File").

int option_count = `0`

  * void set_option_count(value: int)

  * int get_option_count()

The number of additional OptionButtons and CheckBoxes in the dialog.

String root_subfolder = `""`

  * void set_root_subfolder(value: String)

  * String get_root_subfolder()

If non-empty, the given sub-folder will be "root" of this FileDialog, i.e.
user won't be able to go to its parent directory.

Note: This property is ignored by native file dialogs.

bool show_hidden_files = `false`

  * void set_show_hidden_files(value: bool)

  * bool is_showing_hidden_files()

If `true`, the dialog will show hidden files.

Note: This property is ignored by native file dialogs on Android and Linux.

bool use_native_dialog = `false`

  * void set_use_native_dialog(value: bool)

  * bool get_use_native_dialog()

If `true`, and if supported by the current DisplayServer, OS native dialog
will be used instead of custom one.

Note: On Android, it is only supported when using ACCESS_FILESYSTEM. For
access mode ACCESS_RESOURCES and ACCESS_USERDATA, the system will fall back to
custom FileDialog.

Note: On Linux and macOS, sandboxed apps always use native dialogs to access
the host file system.

Note: On macOS, sandboxed apps will save security-scoped bookmarks to retain
access to the opened folders across multiple sessions. Use
OS.get_granted_permissions() to get a list of saved bookmarks.

Note: Native dialogs are isolated from the base process, file dialog
properties can't be modified once the dialog is shown.

## Method Descriptions

void add_filter(filter: String, description: String = "")

Adds a comma-delimited file name `filter` option to the FileDialog with an
optional `description`, which restricts what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename and
extension can be `*` to match any string. Filters starting with `.` (i.e.
empty filenames) are not allowed.

For example, a `filter` of `"*.png, *.jpg"` and a `description` of `"Images"`
results in filter text "Images (*.png, *.jpg)".

void add_option(name: String, values: PackedStringArray, default_value_index:
int)

Adds an additional OptionButton to the file dialog. If `values` is empty, a
CheckBox is added instead.

`default_value_index` should be an index of the value in the `values`. If
`values` is empty it should be either `1` (checked), or `0` (unchecked).

void clear_filename_filter()

Clear the filter for file names.

void clear_filters()

Clear all the added filters in the dialog.

void deselect_all()

Clear all currently selected items in the dialog.

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

Returns the vertical box container of the dialog, custom controls can be added
to it.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to hide it or any of its children, use their
CanvasItem.visible property.

Note: Changes to this node are ignored by native file dialogs, use
add_option() to add custom elements to the dialog instead.

void invalidate()

Invalidate and update the current dialog content list.

Note: This method does nothing on native file dialogs.

void set_option_default(option: int, default_value_index: int)

Sets the default value index of the OptionButton or CheckBox with index
`option`.

void set_option_name(option: int, name: String)

Sets the name of the OptionButton or CheckBox with index `option`.

void set_option_values(option: int, values: PackedStringArray)

Sets the option values of the OptionButton with index `option`.

## Theme Property Descriptions

Color file_disabled_color = `Color(1, 1, 1, 0.25)`

The color tint for disabled files (when the FileDialog is used in open folder
mode).

Color file_icon_color = `Color(1, 1, 1, 1)`

The color modulation applied to the file icon.

Color folder_icon_color = `Color(1, 1, 1, 1)`

The color modulation applied to the folder icon.

Texture2D back_folder

Custom icon for the back arrow.

Texture2D create_folder

Custom icon for the create folder button.

Texture2D file

Custom icon for files.

Texture2D folder

Custom icon for folders.

Texture2D forward_folder

Custom icon for the forward arrow.

Texture2D parent_folder

Custom icon for the parent folder arrow.

Texture2D reload

Custom icon for the reload button.

Texture2D toggle_filename_filter

Custom icon for the toggle button for the filter for file names.

Texture2D toggle_hidden

Custom icon for the toggle hidden button.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

