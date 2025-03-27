# DisplayServer

Inherits: Object

A server interface for low-level window management.

## Description

DisplayServer handles everything related to window management. It is separated
from OS as a single operating system may support multiple display servers.

Headless mode: Starting the engine with the `--headless` command line argument
disables all rendering and window management functions. Most functions from
DisplayServer will return dummy values in this case.

## Methods

void | beep() const  
---|---  
String | clipboard_get() const  
Image | clipboard_get_image() const  
String | clipboard_get_primary() const  
bool | clipboard_has() const  
bool | clipboard_has_image() const  
void | clipboard_set(clipboard: String)  
void | clipboard_set_primary(clipboard_primary: String)  
int | create_status_indicator(icon: Texture2D, tooltip: String, callback: Callable)  
CursorShape | cursor_get_shape() const  
void | cursor_set_custom_image(cursor: Resource, shape: CursorShape = 0, hotspot: Vector2 = Vector2(0, 0))  
void | cursor_set_shape(shape: CursorShape)  
void | delete_status_indicator(id: int)  
Error | dialog_input_text(title: String, description: String, existing_text: String, callback: Callable)  
Error | dialog_show(title: String, description: String, buttons: PackedStringArray, callback: Callable)  
void | enable_for_stealing_focus(process_id: int)  
Error | file_dialog_show(title: String, current_directory: String, filename: String, show_hidden: bool, mode: FileDialogMode, filters: PackedStringArray, callback: Callable)  
Error | file_dialog_with_options_show(title: String, current_directory: String, root: String, filename: String, show_hidden: bool, mode: FileDialogMode, filters: PackedStringArray, options: Array[Dictionary], callback: Callable)  
void | force_process_and_drop_events()  
Color | get_accent_color() const  
Color | get_base_color() const  
Array[Rect2] | get_display_cutouts() const  
Rect2i | get_display_safe_area() const  
int | get_keyboard_focus_screen() const  
String | get_name() const  
int | get_primary_screen() const  
int | get_screen_count() const  
int | get_screen_from_rect(rect: Rect2) const  
bool | get_swap_cancel_ok()  
int | get_window_at_screen_position(position: Vector2i) const  
PackedInt32Array | get_window_list() const  
int | global_menu_add_check_item(menu_root: String, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_icon_check_item(menu_root: String, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_icon_item(menu_root: String, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_icon_radio_check_item(menu_root: String, icon: Texture2D, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_item(menu_root: String, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_multistate_item(menu_root: String, label: String, max_states: int, default_state: int, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_radio_check_item(menu_root: String, label: String, callback: Callable = Callable(), key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)  
int | global_menu_add_separator(menu_root: String, index: int = -1)  
int | global_menu_add_submenu_item(menu_root: String, label: String, submenu: String, index: int = -1)  
void | global_menu_clear(menu_root: String)  
Key | global_menu_get_item_accelerator(menu_root: String, idx: int) const  
Callable | global_menu_get_item_callback(menu_root: String, idx: int) const  
int | global_menu_get_item_count(menu_root: String) const  
Texture2D | global_menu_get_item_icon(menu_root: String, idx: int) const  
int | global_menu_get_item_indentation_level(menu_root: String, idx: int) const  
int | global_menu_get_item_index_from_tag(menu_root: String, tag: Variant) const  
int | global_menu_get_item_index_from_text(menu_root: String, text: String) const  
Callable | global_menu_get_item_key_callback(menu_root: String, idx: int) const  
int | global_menu_get_item_max_states(menu_root: String, idx: int) const  
int | global_menu_get_item_state(menu_root: String, idx: int) const  
String | global_menu_get_item_submenu(menu_root: String, idx: int) const  
Variant | global_menu_get_item_tag(menu_root: String, idx: int) const  
String | global_menu_get_item_text(menu_root: String, idx: int) const  
String | global_menu_get_item_tooltip(menu_root: String, idx: int) const  
Dictionary | global_menu_get_system_menu_roots() const  
bool | global_menu_is_item_checkable(menu_root: String, idx: int) const  
bool | global_menu_is_item_checked(menu_root: String, idx: int) const  
bool | global_menu_is_item_disabled(menu_root: String, idx: int) const  
bool | global_menu_is_item_hidden(menu_root: String, idx: int) const  
bool | global_menu_is_item_radio_checkable(menu_root: String, idx: int) const  
void | global_menu_remove_item(menu_root: String, idx: int)  
void | global_menu_set_item_accelerator(menu_root: String, idx: int, keycode: Key)  
void | global_menu_set_item_callback(menu_root: String, idx: int, callback: Callable)  
void | global_menu_set_item_checkable(menu_root: String, idx: int, checkable: bool)  
void | global_menu_set_item_checked(menu_root: String, idx: int, checked: bool)  
void | global_menu_set_item_disabled(menu_root: String, idx: int, disabled: bool)  
void | global_menu_set_item_hidden(menu_root: String, idx: int, hidden: bool)  
void | global_menu_set_item_hover_callbacks(menu_root: String, idx: int, callback: Callable)  
void | global_menu_set_item_icon(menu_root: String, idx: int, icon: Texture2D)  
void | global_menu_set_item_indentation_level(menu_root: String, idx: int, level: int)  
void | global_menu_set_item_key_callback(menu_root: String, idx: int, key_callback: Callable)  
void | global_menu_set_item_max_states(menu_root: String, idx: int, max_states: int)  
void | global_menu_set_item_radio_checkable(menu_root: String, idx: int, checkable: bool)  
void | global_menu_set_item_state(menu_root: String, idx: int, state: int)  
void | global_menu_set_item_submenu(menu_root: String, idx: int, submenu: String)  
void | global_menu_set_item_tag(menu_root: String, idx: int, tag: Variant)  
void | global_menu_set_item_text(menu_root: String, idx: int, text: String)  
void | global_menu_set_item_tooltip(menu_root: String, idx: int, tooltip: String)  
void | global_menu_set_popup_callbacks(menu_root: String, open_callback: Callable, close_callback: Callable)  
bool | has_additional_outputs() const  
bool | has_feature(feature: Feature) const  
bool | has_hardware_keyboard() const  
void | help_set_search_callbacks(search_callback: Callable, action_callback: Callable)  
Vector2i | ime_get_selection() const  
String | ime_get_text() const  
bool | is_dark_mode() const  
bool | is_dark_mode_supported() const  
bool | is_touchscreen_available() const  
bool | is_window_transparency_available() const  
int | keyboard_get_current_layout() const  
Key | keyboard_get_keycode_from_physical(keycode: Key) const  
Key | keyboard_get_label_from_physical(keycode: Key) const  
int | keyboard_get_layout_count() const  
String | keyboard_get_layout_language(index: int) const  
String | keyboard_get_layout_name(index: int) const  
void | keyboard_set_current_layout(index: int)  
BitField[MouseButtonMask] | mouse_get_button_state() const  
MouseMode | mouse_get_mode() const  
Vector2i | mouse_get_position() const  
void | mouse_set_mode(mouse_mode: MouseMode)  
void | process_events()  
void | register_additional_output(object: Object)  
int | screen_get_dpi(screen: int = -1) const  
Image | screen_get_image(screen: int = -1) const  
Image | screen_get_image_rect(rect: Rect2i) const  
float | screen_get_max_scale() const  
ScreenOrientation | screen_get_orientation(screen: int = -1) const  
Color | screen_get_pixel(position: Vector2i) const  
Vector2i | screen_get_position(screen: int = -1) const  
float | screen_get_refresh_rate(screen: int = -1) const  
float | screen_get_scale(screen: int = -1) const  
Vector2i | screen_get_size(screen: int = -1) const  
Rect2i | screen_get_usable_rect(screen: int = -1) const  
bool | screen_is_kept_on() const  
void | screen_set_keep_on(enable: bool)  
void | screen_set_orientation(orientation: ScreenOrientation, screen: int = -1)  
void | set_icon(image: Image)  
void | set_native_icon(filename: String)  
void | set_system_theme_change_callback(callable: Callable)  
void | show_emoji_and_symbol_picker() const  
Rect2 | status_indicator_get_rect(id: int) const  
void | status_indicator_set_callback(id: int, callback: Callable)  
void | status_indicator_set_icon(id: int, icon: Texture2D)  
void | status_indicator_set_menu(id: int, menu_rid: RID)  
void | status_indicator_set_tooltip(id: int, tooltip: String)  
String | tablet_get_current_driver() const  
int | tablet_get_driver_count() const  
String | tablet_get_driver_name(idx: int) const  
void | tablet_set_current_driver(name: String)  
Array[Dictionary] | tts_get_voices() const  
PackedStringArray | tts_get_voices_for_language(language: String) const  
bool | tts_is_paused() const  
bool | tts_is_speaking() const  
void | tts_pause()  
void | tts_resume()  
void | tts_set_utterance_callback(event: TTSUtteranceEvent, callable: Callable)  
void | tts_speak(text: String, voice: String, volume: int = 50, pitch: float = 1.0, rate: float = 1.0, utterance_id: int = 0, interrupt: bool = false)  
void | tts_stop()  
void | unregister_additional_output(object: Object)  
int | virtual_keyboard_get_height() const  
void | virtual_keyboard_hide()  
void | virtual_keyboard_show(existing_text: String, position: Rect2 = Rect2(0, 0, 0, 0), type: VirtualKeyboardType = 0, max_length: int = -1, cursor_start: int = -1, cursor_end: int = -1)  
void | warp_mouse(position: Vector2i)  
bool | window_can_draw(window_id: int = 0) const  
int | window_get_active_popup() const  
int | window_get_attached_instance_id(window_id: int = 0) const  
int | window_get_current_screen(window_id: int = 0) const  
bool | window_get_flag(flag: WindowFlags, window_id: int = 0) const  
Vector2i | window_get_max_size(window_id: int = 0) const  
Vector2i | window_get_min_size(window_id: int = 0) const  
WindowMode | window_get_mode(window_id: int = 0) const  
int | window_get_native_handle(handle_type: HandleType, window_id: int = 0) const  
Rect2i | window_get_popup_safe_rect(window: int) const  
Vector2i | window_get_position(window_id: int = 0) const  
Vector2i | window_get_position_with_decorations(window_id: int = 0) const  
Vector3i | window_get_safe_title_margins(window_id: int = 0) const  
Vector2i | window_get_size(window_id: int = 0) const  
Vector2i | window_get_size_with_decorations(window_id: int = 0) const  
Vector2i | window_get_title_size(title: String, window_id: int = 0) const  
VSyncMode | window_get_vsync_mode(window_id: int = 0) const  
bool | window_is_focused(window_id: int = 0) const  
bool | window_is_maximize_allowed(window_id: int = 0) const  
bool | window_maximize_on_title_dbl_click() const  
bool | window_minimize_on_title_dbl_click() const  
void | window_move_to_foreground(window_id: int = 0)  
void | window_request_attention(window_id: int = 0)  
void | window_set_current_screen(screen: int, window_id: int = 0)  
void | window_set_drop_files_callback(callback: Callable, window_id: int = 0)  
void | window_set_exclusive(window_id: int, exclusive: bool)  
void | window_set_flag(flag: WindowFlags, enabled: bool, window_id: int = 0)  
void | window_set_ime_active(active: bool, window_id: int = 0)  
void | window_set_ime_position(position: Vector2i, window_id: int = 0)  
void | window_set_input_event_callback(callback: Callable, window_id: int = 0)  
void | window_set_input_text_callback(callback: Callable, window_id: int = 0)  
void | window_set_max_size(max_size: Vector2i, window_id: int = 0)  
void | window_set_min_size(min_size: Vector2i, window_id: int = 0)  
void | window_set_mode(mode: WindowMode, window_id: int = 0)  
void | window_set_mouse_passthrough(region: PackedVector2Array, window_id: int = 0)  
void | window_set_popup_safe_rect(window: int, rect: Rect2i)  
void | window_set_position(position: Vector2i, window_id: int = 0)  
void | window_set_rect_changed_callback(callback: Callable, window_id: int = 0)  
void | window_set_size(size: Vector2i, window_id: int = 0)  
void | window_set_title(title: String, window_id: int = 0)  
void | window_set_transient(window_id: int, parent_window_id: int)  
void | window_set_vsync_mode(vsync_mode: VSyncMode, window_id: int = 0)  
void | window_set_window_buttons_offset(offset: Vector2i, window_id: int = 0)  
void | window_set_window_event_callback(callback: Callable, window_id: int = 0)  
void | window_start_drag(window_id: int = 0)  
void | window_start_resize(edge: WindowResizeEdge, window_id: int = 0)  
  
## Enumerations

enum Feature:

Feature FEATURE_GLOBAL_MENU = `0`

Deprecated: Use NativeMenu or PopupMenu instead.

Display server supports global menu. This allows the application to display
its menu items in the operating system's top bar. macOS

Feature FEATURE_SUBWINDOWS = `1`

Display server supports multiple windows that can be moved outside of the main
window. Windows, macOS, Linux (X11)

Feature FEATURE_TOUCHSCREEN = `2`

Display server supports touchscreen input. Windows, Linux (X11), Android, iOS,
Web

Feature FEATURE_MOUSE = `3`

Display server supports mouse input. Windows, macOS, Linux (X11/Wayland),
Android, Web

Feature FEATURE_MOUSE_WARP = `4`

Display server supports warping mouse coordinates to keep the mouse cursor
constrained within an area, but looping when one of the edges is reached.
Windows, macOS, Linux (X11/Wayland)

Feature FEATURE_CLIPBOARD = `5`

Display server supports setting and getting clipboard data. See also
FEATURE_CLIPBOARD_PRIMARY. Windows, macOS, Linux (X11/Wayland), Android, iOS,
Web

Feature FEATURE_VIRTUAL_KEYBOARD = `6`

Display server supports popping up a virtual keyboard when requested to input
text without a physical keyboard. Android, iOS, Web

Feature FEATURE_CURSOR_SHAPE = `7`

Display server supports setting the mouse cursor shape to be different from
the default. Windows, macOS, Linux (X11/Wayland), Android, Web

Feature FEATURE_CUSTOM_CURSOR_SHAPE = `8`

Display server supports setting the mouse cursor shape to a custom image.
Windows, macOS, Linux (X11/Wayland), Web

Feature FEATURE_NATIVE_DIALOG = `9`

Display server supports spawning text dialogs using the operating system's
native look-and-feel. See dialog_show(). Windows, macOS

Feature FEATURE_IME = `10`

Display server supports Input Method Editor, which is commonly used for
inputting Chinese/Japanese/Korean text. This is handled by the operating
system, rather than by Godot. Windows, macOS, Linux (X11)

Feature FEATURE_WINDOW_TRANSPARENCY = `11`

Display server supports windows can use per-pixel transparency to make windows
behind them partially or fully visible. Windows, macOS, Linux (X11/Wayland)

Feature FEATURE_HIDPI = `12`

Display server supports querying the operating system's display scale factor.
This allows for reliable automatic hiDPI display detection, as opposed to
guessing based on the screen resolution and reported display DPI (which can be
unreliable due to broken monitor EDID). Windows, Linux (Wayland), macOS

Feature FEATURE_ICON = `13`

Display server supports changing the window icon (usually displayed in the
top-left corner). Windows, macOS, Linux (X11)

Feature FEATURE_NATIVE_ICON = `14`

Display server supports changing the window icon (usually displayed in the
top-left corner). Windows, macOS

Feature FEATURE_ORIENTATION = `15`

Display server supports changing the screen orientation. Android, iOS

Feature FEATURE_SWAP_BUFFERS = `16`

Display server supports V-Sync status can be changed from the default (which
is forced to be enabled platforms not supporting this feature). Windows,
macOS, Linux (X11/Wayland)

Feature FEATURE_CLIPBOARD_PRIMARY = `18`

Display server supports Primary clipboard can be used. This is a different
clipboard from FEATURE_CLIPBOARD. Linux (X11/Wayland)

Feature FEATURE_TEXT_TO_SPEECH = `19`

Display server supports text-to-speech. See `tts_*` methods. Windows, macOS,
Linux (X11/Wayland), Android, iOS, Web

Feature FEATURE_EXTEND_TO_TITLE = `20`

Display server supports expanding window content to the title. See
WINDOW_FLAG_EXTEND_TO_TITLE. macOS

Feature FEATURE_SCREEN_CAPTURE = `21`

Display server supports reading screen pixels. See screen_get_pixel().

Feature FEATURE_STATUS_INDICATOR = `22`

Display server supports application status indicators.

Feature FEATURE_NATIVE_HELP = `23`

Display server supports native help system search callbacks. See
help_set_search_callbacks().

Feature FEATURE_NATIVE_DIALOG_INPUT = `24`

Display server supports spawning text input dialogs using the operating
system's native look-and-feel. See dialog_input_text(). Windows, macOS

Feature FEATURE_NATIVE_DIALOG_FILE = `25`

Display server supports spawning dialogs for selecting files or directories
using the operating system's native look-and-feel. See file_dialog_show().
Windows, macOS, Linux (X11/Wayland), Android

Feature FEATURE_NATIVE_DIALOG_FILE_EXTRA = `26`

The display server supports all features of FEATURE_NATIVE_DIALOG_FILE, with
the added functionality of Options and native dialog file access to `res://`
and `user://` paths. See file_dialog_show() and
file_dialog_with_options_show(). Windows, macOS, Linux (X11/Wayland)

Feature FEATURE_WINDOW_DRAG = `27`

The display server supports initiating window drag and resize operations on
demand. See window_start_drag() and window_start_resize().

Feature FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE = `28`

Display server supports WINDOW_FLAG_EXCLUDE_FROM_CAPTURE window flag.

Feature FEATURE_WINDOW_EMBEDDING = `29`

Display server supports embedding a window from another process. Windows,
Linux (X11)

Feature FEATURE_NATIVE_DIALOG_FILE_MIME = `30`

Native file selection dialog supports MIME types as filters.

Feature FEATURE_EMOJI_AND_SYMBOL_PICKER = `31`

Display server supports system emoji and symbol picker. Windows, macOS

enum MouseMode:

MouseMode MOUSE_MODE_VISIBLE = `0`

Makes the mouse cursor visible if it is hidden.

MouseMode MOUSE_MODE_HIDDEN = `1`

Makes the mouse cursor hidden if it is visible.

MouseMode MOUSE_MODE_CAPTURED = `2`

Captures the mouse. The mouse will be hidden and its position locked at the
center of the window manager's window.

Note: If you want to process the mouse's movement in this mode, you need to
use InputEventMouseMotion.relative.

MouseMode MOUSE_MODE_CONFINED = `3`

Confines the mouse cursor to the game window, and make it visible.

MouseMode MOUSE_MODE_CONFINED_HIDDEN = `4`

Confines the mouse cursor to the game window, and make it hidden.

MouseMode MOUSE_MODE_MAX = `5`

Max value of the MouseMode.

enum ScreenOrientation:

ScreenOrientation SCREEN_LANDSCAPE = `0`

Default landscape orientation.

ScreenOrientation SCREEN_PORTRAIT = `1`

Default portrait orientation.

ScreenOrientation SCREEN_REVERSE_LANDSCAPE = `2`

Reverse landscape orientation (upside down).

ScreenOrientation SCREEN_REVERSE_PORTRAIT = `3`

Reverse portrait orientation (upside down).

ScreenOrientation SCREEN_SENSOR_LANDSCAPE = `4`

Automatic landscape orientation (default or reverse depending on sensor).

ScreenOrientation SCREEN_SENSOR_PORTRAIT = `5`

Automatic portrait orientation (default or reverse depending on sensor).

ScreenOrientation SCREEN_SENSOR = `6`

Automatic landscape or portrait orientation (default or reverse depending on
sensor).

enum VirtualKeyboardType:

VirtualKeyboardType KEYBOARD_TYPE_DEFAULT = `0`

Default text virtual keyboard.

VirtualKeyboardType KEYBOARD_TYPE_MULTILINE = `1`

Multiline virtual keyboard.

VirtualKeyboardType KEYBOARD_TYPE_NUMBER = `2`

Virtual number keypad, useful for PIN entry.

VirtualKeyboardType KEYBOARD_TYPE_NUMBER_DECIMAL = `3`

Virtual number keypad, useful for entering fractional numbers.

VirtualKeyboardType KEYBOARD_TYPE_PHONE = `4`

Virtual phone number keypad.

VirtualKeyboardType KEYBOARD_TYPE_EMAIL_ADDRESS = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

VirtualKeyboardType KEYBOARD_TYPE_PASSWORD = `6`

Virtual keyboard for entering a password. On most platforms, this should
disable autocomplete and autocapitalization.

Note: This is not supported on Web. Instead, this behaves identically to
KEYBOARD_TYPE_DEFAULT.

VirtualKeyboardType KEYBOARD_TYPE_URL = `7`

Virtual keyboard with additional keys to assist with typing URLs.

enum CursorShape:

CursorShape CURSOR_ARROW = `0`

Arrow cursor shape. This is the default when not pointing anything that
overrides the mouse cursor, such as a LineEdit or TextEdit.

CursorShape CURSOR_IBEAM = `1`

I-beam cursor shape. This is used by default when hovering a control that
accepts text input, such as LineEdit or TextEdit.

CursorShape CURSOR_POINTING_HAND = `2`

Pointing hand cursor shape. This is used by default when hovering a LinkButton
or a URL tag in a RichTextLabel.

CursorShape CURSOR_CROSS = `3`

Crosshair cursor. This is intended to be displayed when the user needs precise
aim over an element, such as a rectangle selection tool or a color picker.

CursorShape CURSOR_WAIT = `4`

Wait cursor. On most cursor themes, this displays a spinning icon besides the
arrow. Intended to be used for non-blocking operations (when the user can do
something else at the moment). See also CURSOR_BUSY.

CursorShape CURSOR_BUSY = `5`

Wait cursor. On most cursor themes, this replaces the arrow with a spinning
icon. Intended to be used for blocking operations (when the user can't do
anything else at the moment). See also CURSOR_WAIT.

CursorShape CURSOR_DRAG = `6`

Dragging hand cursor. This is displayed during drag-and-drop operations. See
also CURSOR_CAN_DROP.

CursorShape CURSOR_CAN_DROP = `7`

"Can drop" cursor. This is displayed during drag-and-drop operations if
hovering over a Control that can accept the drag-and-drop event. On most
cursor themes, this displays a dragging hand with an arrow symbol besides it.
See also CURSOR_DRAG.

CursorShape CURSOR_FORBIDDEN = `8`

Forbidden cursor. This is displayed during drag-and-drop operations if the
hovered Control can't accept the drag-and-drop event.

CursorShape CURSOR_VSIZE = `9`

Vertical resize cursor. Intended to be displayed when the hovered Control can
be vertically resized using the mouse. See also CURSOR_VSPLIT.

CursorShape CURSOR_HSIZE = `10`

Horizontal resize cursor. Intended to be displayed when the hovered Control
can be horizontally resized using the mouse. See also CURSOR_HSPLIT.

CursorShape CURSOR_BDIAGSIZE = `11`

Secondary diagonal resize cursor (top-right/bottom-left). Intended to be
displayed when the hovered Control can be resized on both axes at once using
the mouse.

CursorShape CURSOR_FDIAGSIZE = `12`

Main diagonal resize cursor (top-left/bottom-right). Intended to be displayed
when the hovered Control can be resized on both axes at once using the mouse.

CursorShape CURSOR_MOVE = `13`

Move cursor. Intended to be displayed when the hovered Control can be moved
using the mouse.

CursorShape CURSOR_VSPLIT = `14`

Vertical split cursor. This is displayed when hovering a Control with splits
that can be vertically resized using the mouse, such as VSplitContainer. On
some cursor themes, this cursor may have the same appearance as CURSOR_VSIZE.

CursorShape CURSOR_HSPLIT = `15`

Horizontal split cursor. This is displayed when hovering a Control with splits
that can be horizontally resized using the mouse, such as HSplitContainer. On
some cursor themes, this cursor may have the same appearance as CURSOR_HSIZE.

CursorShape CURSOR_HELP = `16`

Help cursor. On most cursor themes, this displays a question mark icon instead
of the mouse cursor. Intended to be used when the user has requested help on
the next element that will be clicked.

CursorShape CURSOR_MAX = `17`

Represents the size of the CursorShape enum.

enum FileDialogMode:

FileDialogMode FILE_DIALOG_MODE_OPEN_FILE = `0`

The native file dialog allows selecting one, and only one file.

FileDialogMode FILE_DIALOG_MODE_OPEN_FILES = `1`

The native file dialog allows selecting multiple files.

FileDialogMode FILE_DIALOG_MODE_OPEN_DIR = `2`

The native file dialog only allows selecting a directory, disallowing the
selection of any file.

FileDialogMode FILE_DIALOG_MODE_OPEN_ANY = `3`

The native file dialog allows selecting one file or directory.

FileDialogMode FILE_DIALOG_MODE_SAVE_FILE = `4`

The native file dialog will warn when a file exists.

enum WindowMode:

WindowMode WINDOW_MODE_WINDOWED = `0`

Windowed mode, i.e. Window doesn't occupy the whole screen (unless set to the
size of the screen).

WindowMode WINDOW_MODE_MINIMIZED = `1`

Minimized window mode, i.e. Window is not visible and available on window
manager's window list. Normally happens when the minimize button is pressed.

WindowMode WINDOW_MODE_MAXIMIZED = `2`

Maximized window mode, i.e. Window will occupy whole screen area except task
bar and still display its borders. Normally happens when the maximize button
is pressed.

WindowMode WINDOW_MODE_FULLSCREEN = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no
decorations. The display's video mode is not changed.

On Android: This enables immersive mode.

On Windows: Multi-window full-screen mode has a 1px border of the
ProjectSettings.rendering/environment/defaults/default_clear_color color.

On macOS: A new desktop is used to display the running project.

Note: Regardless of the platform, enabling full screen will change the window
size to match the monitor's size. Therefore, make sure your project supports
multiple resolutions when enabling full screen mode.

WindowMode WINDOW_MODE_EXCLUSIVE_FULLSCREEN = `4`

A single window full screen mode. This mode has less overhead, but only one
window can be open on a given screen at a time (opening a child window or
application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no
border or decorations. The display's video mode is not changed.

On Android: This enables immersive mode.

On Windows: Depending on video driver, full screen transition might cause
screens to go black for a moment.

On macOS: A new desktop is used to display the running project. Exclusive full
screen mode prevents Dock and Menu from showing up when the mouse pointer is
hovering the edge of the screen.

On Linux (X11): Exclusive full screen mode bypasses compositor.

On Linux (Wayland): Equivalent to WINDOW_MODE_FULLSCREEN.

Note: Regardless of the platform, enabling full screen will change the window
size to match the monitor's size. Therefore, make sure your project supports
multiple resolutions when enabling full screen mode.

enum WindowFlags:

WindowFlags WINDOW_FLAG_RESIZE_DISABLED = `0`

The window can't be resized by dragging its resize grip. It's still possible
to resize the window using window_set_size(). This flag is ignored for full
screen windows.

WindowFlags WINDOW_FLAG_BORDERLESS = `1`

The window do not have native title bar and other decorations. This flag is
ignored for full-screen windows.

WindowFlags WINDOW_FLAG_ALWAYS_ON_TOP = `2`

The window is floating on top of all other windows. This flag is ignored for
full-screen windows.

WindowFlags WINDOW_FLAG_TRANSPARENT = `3`

The window background can be transparent.

Note: This flag has no effect if is_window_transparency_available() returns
`false`.

Note: Transparency support is implemented on Linux (X11/Wayland), macOS, and
Windows, but availability might vary depending on GPU driver, display manager,
and compositor capabilities.

WindowFlags WINDOW_FLAG_NO_FOCUS = `4`

The window can't be focused. No-focus window will ignore all input, except
mouse clicks.

WindowFlags WINDOW_FLAG_POPUP = `5`

Window is part of menu or OptionButton dropdown. This flag can't be changed
when the window is visible. An active popup window will exclusively receive
all input, without stealing focus from its parent. Popup windows are
automatically closed when uses click outside it, or when an application is
switched. Popup window must have transient parent set (see
window_set_transient()).

WindowFlags WINDOW_FLAG_EXTEND_TO_TITLE = `6`

Window content is expanded to the full size of the window. Unlike borderless
window, the frame is left intact and can be used to resize the window, title
bar is transparent, but have minimize/maximize/close buttons.

Use window_set_window_buttons_offset() to adjust minimize/maximize/close
buttons offset.

Use window_get_safe_title_margins() to determine area under the title bar that
is not covered by decorations.

Note: This flag is implemented only on macOS.

WindowFlags WINDOW_FLAG_MOUSE_PASSTHROUGH = `7`

All mouse events are passed to the underlying window of the same application.

WindowFlags WINDOW_FLAG_SHARP_CORNERS = `8`

Window style is overridden, forcing sharp corners.

Note: This flag is implemented only on Windows (11).

WindowFlags WINDOW_FLAG_EXCLUDE_FROM_CAPTURE = `9`

Windows is excluded from screenshots taken by screen_get_image(),
screen_get_image_rect(), and screen_get_pixel().

Note: This flag is implemented on macOS and Windows.

Note: Setting this flag will NOT prevent other apps from capturing an image,
it should not be used as a security measure.

WindowFlags WINDOW_FLAG_MAX = `10`

Max value of the WindowFlags.

enum WindowEvent:

WindowEvent WINDOW_EVENT_MOUSE_ENTER = `0`

Sent when the mouse pointer enters the window.

WindowEvent WINDOW_EVENT_MOUSE_EXIT = `1`

Sent when the mouse pointer exits the window.

WindowEvent WINDOW_EVENT_FOCUS_IN = `2`

Sent when the window grabs focus.

WindowEvent WINDOW_EVENT_FOCUS_OUT = `3`

Sent when the window loses focus.

WindowEvent WINDOW_EVENT_CLOSE_REQUEST = `4`

Sent when the user has attempted to close the window (e.g. close button is
pressed).

WindowEvent WINDOW_EVENT_GO_BACK_REQUEST = `5`

Sent when the device "Back" button is pressed.

Note: This event is implemented only on Android.

WindowEvent WINDOW_EVENT_DPI_CHANGE = `6`

Sent when the window is moved to the display with different DPI, or display
DPI is changed.

Note: This flag is implemented only on macOS.

WindowEvent WINDOW_EVENT_TITLEBAR_CHANGE = `7`

Sent when the window title bar decoration is changed (e.g.
WINDOW_FLAG_EXTEND_TO_TITLE is set or window entered/exited full screen mode).

Note: This flag is implemented only on macOS.

enum WindowResizeEdge:

WindowResizeEdge WINDOW_EDGE_TOP_LEFT = `0`

Top-left edge of a window.

WindowResizeEdge WINDOW_EDGE_TOP = `1`

Top edge of a window.

WindowResizeEdge WINDOW_EDGE_TOP_RIGHT = `2`

Top-right edge of a window.

WindowResizeEdge WINDOW_EDGE_LEFT = `3`

Left edge of a window.

WindowResizeEdge WINDOW_EDGE_RIGHT = `4`

Right edge of a window.

WindowResizeEdge WINDOW_EDGE_BOTTOM_LEFT = `5`

Bottom-left edge of a window.

WindowResizeEdge WINDOW_EDGE_BOTTOM = `6`

Bottom edge of a window.

WindowResizeEdge WINDOW_EDGE_BOTTOM_RIGHT = `7`

Bottom-right edge of a window.

WindowResizeEdge WINDOW_EDGE_MAX = `8`

Represents the size of the WindowResizeEdge enum.

enum VSyncMode:

VSyncMode VSYNC_DISABLED = `0`

No vertical synchronization, which means the engine will display frames as
fast as possible (tearing may be visible). Framerate is unlimited (regardless
of Engine.max_fps).

VSyncMode VSYNC_ENABLED = `1`

Default vertical synchronization mode, the image is displayed only on vertical
blanking intervals (no tearing is visible). Framerate is limited by the
monitor refresh rate (regardless of Engine.max_fps).

VSyncMode VSYNC_ADAPTIVE = `2`

Behaves like VSYNC_DISABLED when the framerate drops below the screen's
refresh rate to reduce stuttering (tearing may be visible). Otherwise,
vertical synchronization is enabled to avoid tearing. Framerate is limited by
the monitor refresh rate (regardless of Engine.max_fps). Behaves like
VSYNC_ENABLED when using the Compatibility rendering method.

VSyncMode VSYNC_MAILBOX = `3`

Displays the most recent image in the queue on vertical blanking intervals,
while rendering to the other images (no tearing is visible). Framerate is
unlimited (regardless of Engine.max_fps).

Although not guaranteed, the images can be rendered as fast as possible, which
may reduce input lag (also called "Fast" V-Sync mode). VSYNC_MAILBOX works
best when at least twice as many frames as the display refresh rate are
rendered. Behaves like VSYNC_ENABLED when using the Compatibility rendering
method.

enum HandleType:

HandleType DISPLAY_HANDLE = `0`

Display handle:

  * Linux (X11): `X11::Display*` for the display.

  * Linux (Wayland): `wl_display` for the display.

  * Android: `EGLDisplay` for the display.

HandleType WINDOW_HANDLE = `1`

Window handle:

  * Windows: `HWND` for the window.

  * Linux (X11): `X11::Window*` for the window.

  * Linux (Wayland): `wl_surface` for the window.

  * macOS: `NSWindow*` for the window.

  * iOS: `UIViewController*` for the view controller.

  * Android: `jObject` for the activity.

HandleType WINDOW_VIEW = `2`

Window view:

  * Windows: `HDC` for the window (only with the Compatibility renderer).

  * macOS: `NSView*` for the window main view.

  * iOS: `UIView*` for the window main view.

HandleType OPENGL_CONTEXT = `3`

OpenGL context (only with the Compatibility renderer):

  * Windows: `HGLRC` for the window (native GL), or `EGLContext` for the window (ANGLE).

  * Linux (X11): `GLXContext*` for the window.

  * Linux (Wayland): `EGLContext` for the window.

  * macOS: `NSOpenGLContext*` for the window (native GL), or `EGLContext` for the window (ANGLE).

  * Android: `EGLContext` for the window.

HandleType EGL_DISPLAY = `4`

  * Windows: `EGLDisplay` for the window (ANGLE).

  * macOS: `EGLDisplay` for the window (ANGLE).

  * Linux (Wayland): `EGLDisplay` for the window.

HandleType EGL_CONFIG = `5`

  * Windows: `EGLConfig` for the window (ANGLE).

  * macOS: `EGLConfig` for the window (ANGLE).

  * Linux (Wayland): `EGLConfig` for the window.

enum TTSUtteranceEvent:

TTSUtteranceEvent TTS_UTTERANCE_STARTED = `0`

Utterance has begun to be spoken.

TTSUtteranceEvent TTS_UTTERANCE_ENDED = `1`

Utterance was successfully finished.

TTSUtteranceEvent TTS_UTTERANCE_CANCELED = `2`

Utterance was canceled, or TTS service was unable to process it.

TTSUtteranceEvent TTS_UTTERANCE_BOUNDARY = `3`

Utterance reached a word or sentence boundary.

## Constants

SCREEN_WITH_MOUSE_FOCUS = `-4`

Represents the screen containing the mouse pointer.

Note: On Linux (Wayland), this constant always represents the screen at index
`0`.

SCREEN_WITH_KEYBOARD_FOCUS = `-3`

Represents the screen containing the window with the keyboard focus.

Note: On Linux (Wayland), this constant always represents the screen at index
`0`.

SCREEN_PRIMARY = `-2`

Represents the primary screen.

Note: On Linux (Wayland), this constant always represents the screen at index
`0`.

SCREEN_OF_MAIN_WINDOW = `-1`

Represents the screen where the main window is located. This is usually the
default value in functions that allow specifying one of several screens.

Note: On Linux (Wayland), this constant always represents the screen at index
`0`.

MAIN_WINDOW_ID = `0`

The ID of the main window spawned by the engine, which can be passed to
methods expecting a `window_id`.

INVALID_WINDOW_ID = `-1`

The ID that refers to a nonexistent window. This is returned by some
DisplayServer methods if no window matches the requested result.

INVALID_INDICATOR_ID = `-1`

The ID that refers to a nonexistent application status indicator.

## Method Descriptions

void beep() const

Plays the beep sound from the operative system, if possible. Because it comes
from the OS, the beep sound will be audible even if the application is muted.
It may also be disabled for the entire OS by the user.

Note: This method is implemented on macOS, Linux (X11/Wayland), and Windows.

String clipboard_get() const

Returns the user's clipboard as a string if possible.

Image clipboard_get_image() const

Returns the user's clipboard as an image if possible.

Note: This method uses the copied pixel data, e.g. from a image editing
software or a web browser, not an image file copied from file explorer.

String clipboard_get_primary() const

Returns the user's primary clipboard as a string if possible. This is the
clipboard that is set when the user selects text in any application, rather
than when pressing ``Ctrl` + `C``. The clipboard data can then be pasted by
clicking the middle mouse button in any application that supports the primary
clipboard mechanism.

Note: This method is only implemented on Linux (X11/Wayland).

bool clipboard_has() const

Returns `true` if there is a text content on the user's clipboard.

bool clipboard_has_image() const

Returns `true` if there is an image content on the user's clipboard.

void clipboard_set(clipboard: String)

Sets the user's clipboard content to the given string.

void clipboard_set_primary(clipboard_primary: String)

Sets the user's primary clipboard content to the given string. This is the
clipboard that is set when the user selects text in any application, rather
than when pressing ``Ctrl` + `C``. The clipboard data can then be pasted by
clicking the middle mouse button in any application that supports the primary
clipboard mechanism.

Note: This method is only implemented on Linux (X11/Wayland).

int create_status_indicator(icon: Texture2D, tooltip: String, callback:
Callable)

Creates a new application status indicator with the specified icon, tooltip,
and activation callback.

`callback` should take two arguments: the pressed mouse button (one of the
MouseButton constants) and the click position in screen coordinates (a
Vector2i).

CursorShape cursor_get_shape() const

Returns the default mouse cursor shape set by cursor_set_shape().

void cursor_set_custom_image(cursor: Resource, shape: CursorShape = 0,
hotspot: Vector2 = Vector2(0, 0))

Sets a custom mouse cursor image for the given `shape`. This means the user's
operating system and mouse cursor theme will no longer influence the mouse
cursor's appearance.

`cursor` can be either a Texture2D or an Image, and it should not be larger
than 256256 to display correctly. Optionally, `hotspot` can be set to offset
the image's position relative to the click point. By default, `hotspot` is set
to the top-left corner of the image. See also cursor_set_shape().

void cursor_set_shape(shape: CursorShape)

Sets the default mouse cursor shape. The cursor's appearance will vary
depending on the user's operating system and mouse cursor theme. See also
cursor_get_shape() and cursor_set_custom_image().

void delete_status_indicator(id: int)

Removes the application status indicator.

Error dialog_input_text(title: String, description: String, existing_text:
String, callback: Callable)

Shows a text input dialog which uses the operating system's native look-and-
feel. `callback` should accept a single String parameter which contains the
text field's contents.

Note: This method is implemented if the display server has the
FEATURE_NATIVE_DIALOG_INPUT feature. Supported platforms include macOS,
Windows, and Android.

Error dialog_show(title: String, description: String, buttons:
PackedStringArray, callback: Callable)

Shows a text dialog which uses the operating system's native look-and-feel.
`callback` should accept a single int parameter which corresponds to the index
of the pressed button.

Note: This method is implemented if the display server has the
FEATURE_NATIVE_DIALOG feature. Supported platforms include macOS, Windows, and
Android.

void enable_for_stealing_focus(process_id: int)

Allows the `process_id` PID to steal focus from this window. In other words,
this disables the operating system's focus stealing protection for the
specified PID.

Note: This method is implemented only on Windows.

Error file_dialog_show(title: String, current_directory: String, filename:
String, show_hidden: bool, mode: FileDialogMode, filters: PackedStringArray,
callback: Callable)

Displays OS native dialog for selecting files or directories in the file
system.

Each filter string in the `filters` array should be formatted like this:
`*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of
the filter is optional and can be omitted. It is recommended to set both file
extension and MIME type. See also FileDialog.filters.

Callbacks have the following arguments: `status: bool, selected_paths:
PackedStringArray, selected_filter_index: int`. On Android, callback argument
`selected_filter_index` is always zero.

Note: This method is implemented if the display server has the
FEATURE_NATIVE_DIALOG_FILE feature. Supported platforms include Linux
(X11/Wayland), Windows, macOS, and Android.

Note: `current_directory` might be ignored.

Note: Embedded file dialog and Windows file dialog support only file
extensions, while Android, Linux, and macOS file dialogs also support MIME
types.

Note: On Android and Linux, `show_hidden` is ignored.

Note: On Android and macOS, native file dialogs have no title.

Note: On macOS, sandboxed apps will save security-scoped bookmarks to retain
access to the opened folders across multiple sessions. Use
OS.get_granted_permissions() to get a list of saved bookmarks.

Error file_dialog_with_options_show(title: String, current_directory: String,
root: String, filename: String, show_hidden: bool, mode: FileDialogMode,
filters: PackedStringArray, options: Array[Dictionary], callback: Callable)

Displays OS native dialog for selecting files or directories in the file
system with additional user selectable options.

Each filter string in the `filters` array should be formatted like this:
`*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of
the filter is optional and can be omitted. It is recommended to set both file
extension and MIME type. See also FileDialog.filters.

`options` is array of Dictionarys with the following keys:

  * `"name"` \- option's name String.

  * `"values"` \- PackedStringArray of values. If empty, boolean option (check box) is used.

  * `"default"` \- default selected option index (int) or default boolean value (bool).

Callbacks have the following arguments: `status: bool, selected_paths:
PackedStringArray, selected_filter_index: int, selected_option: Dictionary`.

Note: This method is implemented if the display server has the
FEATURE_NATIVE_DIALOG_FILE_EXTRA feature. Supported platforms include Linux
(X11/Wayland), Windows, and macOS.

Note: `current_directory` might be ignored.

Note: Embedded file dialog and Windows file dialog support only file
extensions, while Android, Linux, and macOS file dialogs also support MIME
types.

Note: On Linux (X11), `show_hidden` is ignored.

Note: On macOS, native file dialogs have no title.

Note: On macOS, sandboxed apps will save security-scoped bookmarks to retain
access to the opened folders across multiple sessions. Use
OS.get_granted_permissions() to get a list of saved bookmarks.

void force_process_and_drop_events()

Forces window manager processing while ignoring all InputEvents. See also
process_events().

Note: This method is implemented on Windows and macOS.

Color get_accent_color() const

Returns OS theme accent color. Returns `Color(0, 0, 0, 0)`, if accent color is
unknown.

Note: This method is implemented on macOS, Windows, and Android.

Color get_base_color() const

Returns the OS theme base color (default control background). Returns
`Color(0, 0, 0, 0)` if the base color is unknown.

Note: This method is implemented on macOS, Windows, and Android.

Array[Rect2] get_display_cutouts() const

Returns an Array of Rect2, each of which is the bounding rectangle for a
display cutout or notch. These are non-functional areas on edge-to-edge
screens used by cameras and sensors. Returns an empty array if the device does
not have cutouts. See also get_display_safe_area().

Note: Currently only implemented on Android. Other platforms will return an
empty array even if they do have display cutouts or notches.

Rect2i get_display_safe_area() const

Returns the unobscured area of the display where interactive controls should
be rendered. See also get_display_cutouts().

Note: Currently only implemented on Android and iOS. On other platforms,
`screen_get_usable_rect(SCREEN_OF_MAIN_WINDOW)` will be returned as a
fallback. See also screen_get_usable_rect().

int get_keyboard_focus_screen() const

Returns the index of the screen containing the window with the keyboard focus,
or the primary screen if there's no focused window.

String get_name() const

Returns the name of the DisplayServer currently in use. Most operating systems
only have a single DisplayServer, but Linux has access to more than one
DisplayServer (currently X11 and Wayland).

The names of built-in display servers are `Windows`, `macOS`, `X11` (Linux),
`Wayland` (Linux), `Android`, `iOS`, `web` (HTML5), and `headless` (when
started with the `--headless` command line argument).

int get_primary_screen() const

Returns index of the primary screen.

int get_screen_count() const

Returns the number of displays available.

int get_screen_from_rect(rect: Rect2) const

Returns the index of the screen that overlaps the most with the given
rectangle. Returns `-1` if the rectangle doesn't overlap with any screen or
has no area.

bool get_swap_cancel_ok()

Returns `true` if positions of OK and Cancel buttons are swapped in dialogs.
This is enabled by default on Windows to follow interface conventions, and be
toggled by changing ProjectSettings.gui/common/swap_cancel_ok.

Note: This doesn't affect native dialogs such as the ones spawned by
dialog_show().

int get_window_at_screen_position(position: Vector2i) const

Returns the ID of the window at the specified screen `position` (in pixels).
On multi-monitor setups, the screen position is relative to the virtual
desktop area. On multi-monitor setups with different screen resolutions or
orientations, the origin may be located outside any display like this:

    
    
    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+
    

PackedInt32Array get_window_list() const

Returns the list of Godot window IDs belonging to this process.

Note: Native dialogs are not included in this list.

int global_menu_add_check_item(menu_root: String, label: String, callback:
Callable = Callable(), key_callback: Callable = Callable(), tag: Variant =
null, accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new checkable item with text `label` to the global menu with ID
`menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_icon_check_item(menu_root: String, icon: Texture2D, label:
String, callback: Callable = Callable(), key_callback: Callable = Callable(),
tag: Variant = null, accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new checkable item with text `label` and icon `icon` to the global menu
with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_icon_item(menu_root: String, icon: Texture2D, label:
String, callback: Callable = Callable(), key_callback: Callable = Callable(),
tag: Variant = null, accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new item with text `label` and icon `icon` to the global menu with ID
`menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_icon_radio_check_item(menu_root: String, icon: Texture2D,
label: String, callback: Callable = Callable(), key_callback: Callable =
Callable(), tag: Variant = null, accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new radio-checkable item with text `label` and icon `icon` to the
global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: Radio-checkable items just display a checkmark, but don't have any
built-in checking behavior and must be checked/unchecked manually. See
global_menu_set_item_checked() for more info on how to control it.

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_item(menu_root: String, label: String, callback: Callable
= Callable(), key_callback: Callable = Callable(), tag: Variant = null,
accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_multistate_item(menu_root: String, label: String,
max_states: int, default_state: int, callback: Callable = Callable(),
key_callback: Callable = Callable(), tag: Variant = null, accelerator: Key =
0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Contrarily to normal binary items, multistate items can have more than two
states, as defined by `max_states`. Each press or activate of the item will
increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: By default, there's no indication of the current item state, it should
be changed manually.

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_radio_check_item(menu_root: String, label: String,
callback: Callable = Callable(), key_callback: Callable = Callable(), tag:
Variant = null, accelerator: Key = 0, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a new radio-checkable item with text `label` to the global menu with ID
`menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: Radio-checkable items just display a checkmark, but don't have any
built-in checking behavior and must be checked/unchecked manually. See
global_menu_set_item_checked() for more info on how to control it.

Note: The `callback` and `key_callback` Callables need to accept exactly one
Variant parameter, the parameter passed to the Callables will be the value
passed to `tag`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_separator(menu_root: String, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds a separator between items to the global menu with ID `menu_root`.
Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

int global_menu_add_submenu_item(menu_root: String, label: String, submenu:
String, index: int = -1)

Deprecated: Use NativeMenu or PopupMenu instead.

Adds an item that will act as a submenu of the global menu `menu_root`. The
`submenu` argument is the ID of the global menu root that will be shown when
the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as
`index` value.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

void global_menu_clear(menu_root: String)

Deprecated: Use NativeMenu or PopupMenu instead.

Removes all items from the global menu with ID `menu_root`.

Note: This method is implemented only on macOS.

Supported system menu IDs:

    
    
    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).
    

Key global_menu_get_item_accelerator(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the accelerator of the item at index `idx`. Accelerators are special
combinations of keys that activate the item, no matter which control is
focused.

Note: This method is implemented only on macOS.

Callable global_menu_get_item_callback(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the callback of the item at index `idx`.

Note: This method is implemented only on macOS.

int global_menu_get_item_count(menu_root: String) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns number of items in the global menu with ID `menu_root`.

Note: This method is implemented only on macOS.

Texture2D global_menu_get_item_icon(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the icon of the item at index `idx`.

Note: This method is implemented only on macOS.

int global_menu_get_item_indentation_level(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the horizontal offset of the item at the given `idx`.

Note: This method is implemented only on macOS.

int global_menu_get_item_index_from_tag(menu_root: String, tag: Variant) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the index of the item with the specified `tag`. Indices are
automatically assigned to each item by the engine, and cannot be set manually.

Note: This method is implemented only on macOS.

int global_menu_get_item_index_from_text(menu_root: String, text: String)
const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the index of the item with the specified `text`. Indices are
automatically assigned to each item by the engine, and cannot be set manually.

Note: This method is implemented only on macOS.

Callable global_menu_get_item_key_callback(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the callback of the item accelerator at index `idx`.

Note: This method is implemented only on macOS.

int global_menu_get_item_max_states(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns number of states of a multistate item. See
global_menu_add_multistate_item() for details.

Note: This method is implemented only on macOS.

int global_menu_get_item_state(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the state of a multistate item. See global_menu_add_multistate_item()
for details.

Note: This method is implemented only on macOS.

String global_menu_get_item_submenu(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the submenu ID of the item at index `idx`. See
global_menu_add_submenu_item() for more info on how to add a submenu.

Note: This method is implemented only on macOS.

Variant global_menu_get_item_tag(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the metadata of the specified item, which might be of any type. You
can set it with global_menu_set_item_tag(), which provides a simple way of
assigning context data to items.

Note: This method is implemented only on macOS.

String global_menu_get_item_text(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the text of the item at index `idx`.

Note: This method is implemented only on macOS.

String global_menu_get_item_tooltip(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns the tooltip associated with the specified index `idx`.

Note: This method is implemented only on macOS.

Dictionary global_menu_get_system_menu_roots() const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns Dictionary of supported system menu IDs and names.

Note: This method is implemented only on macOS.

bool global_menu_is_item_checkable(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it
has a checkbox or radio button.

Note: This method is implemented only on macOS.

bool global_menu_is_item_checked(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns `true` if the item at index `idx` is checked.

Note: This method is implemented only on macOS.

bool global_menu_is_item_disabled(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns `true` if the item at index `idx` is disabled. When it is disabled it
can't be selected, or its action invoked.

See global_menu_set_item_disabled() for more info on how to disable an item.

Note: This method is implemented only on macOS.

bool global_menu_is_item_hidden(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns `true` if the item at index `idx` is hidden.

See global_menu_set_item_hidden() for more info on how to hide an item.

Note: This method is implemented only on macOS.

bool global_menu_is_item_radio_checkable(menu_root: String, idx: int) const

Deprecated: Use NativeMenu or PopupMenu instead.

Returns `true` if the item at index `idx` has radio button-style checkability.

Note: This is purely cosmetic; you must add the logic for checking/unchecking
items in radio groups.

Note: This method is implemented only on macOS.

void global_menu_remove_item(menu_root: String, idx: int)

Deprecated: Use NativeMenu or PopupMenu instead.

Removes the item at index `idx` from the global menu `menu_root`.

Note: The indices of items after the removed item will be shifted by one.

Note: This method is implemented only on macOS.

void global_menu_set_item_accelerator(menu_root: String, idx: int, keycode:
Key)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the accelerator of the item at index `idx`. `keycode` can be a single Key, or a combination of KeyModifierMasks and Keys using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (``Ctrl` + `A``).

Note: This method is implemented only on macOS.

void global_menu_set_item_callback(menu_root: String, idx: int, callback:
Callable)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the callback of the item at index `idx`. Callback is emitted when an item
is pressed.

Note: The `callback` Callable needs to accept exactly one Variant parameter,
the parameter passed to the Callable will be the value passed to the `tag`
parameter when the menu item was created.

Note: This method is implemented only on macOS.

void global_menu_set_item_checkable(menu_root: String, idx: int, checkable:
bool)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type
of the item to plain text.

Note: This method is implemented only on macOS.

void global_menu_set_item_checked(menu_root: String, idx: int, checked: bool)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the checkstate status of the item at index `idx`.

Note: This method is implemented only on macOS.

void global_menu_set_item_disabled(menu_root: String, idx: int, disabled:
bool)

Deprecated: Use NativeMenu or PopupMenu instead.

Enables/disables the item at index `idx`. When it is disabled, it can't be
selected and its action can't be invoked.

Note: This method is implemented only on macOS.

void global_menu_set_item_hidden(menu_root: String, idx: int, hidden: bool)

Deprecated: Use NativeMenu or PopupMenu instead.

Hides/shows the item at index `idx`. When it is hidden, an item does not
appear in a menu and its action cannot be invoked.

Note: This method is implemented only on macOS.

void global_menu_set_item_hover_callbacks(menu_root: String, idx: int,
callback: Callable)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the callback of the item at index `idx`. The callback is emitted when an
item is hovered.

Note: The `callback` Callable needs to accept exactly one Variant parameter,
the parameter passed to the Callable will be the value passed to the `tag`
parameter when the menu item was created.

Note: This method is implemented only on macOS.

void global_menu_set_item_icon(menu_root: String, idx: int, icon: Texture2D)

Deprecated: Use NativeMenu or PopupMenu instead.

Replaces the Texture2D icon of the specified `idx`.

Note: This method is implemented only on macOS.

Note: This method is not supported by macOS "_dock" menu items.

void global_menu_set_item_indentation_level(menu_root: String, idx: int,
level: int)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the horizontal offset of the item at the given `idx`.

Note: This method is implemented only on macOS.

void global_menu_set_item_key_callback(menu_root: String, idx: int,
key_callback: Callable)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the callback of the item at index `idx`. Callback is emitted when its
accelerator is activated.

Note: The `key_callback` Callable needs to accept exactly one Variant
parameter, the parameter passed to the Callable will be the value passed to
the `tag` parameter when the menu item was created.

Note: This method is implemented only on macOS.

void global_menu_set_item_max_states(menu_root: String, idx: int, max_states:
int)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets number of state of a multistate item. See
global_menu_add_multistate_item() for details.

Note: This method is implemented only on macOS.

void global_menu_set_item_radio_checkable(menu_root: String, idx: int,
checkable: bool)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the type of the item at the specified index `idx` to radio button. If
`false`, sets the type of the item to plain text.

Note: This is purely cosmetic; you must add the logic for checking/unchecking
items in radio groups.

Note: This method is implemented only on macOS.

void global_menu_set_item_state(menu_root: String, idx: int, state: int)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the state of a multistate item. See global_menu_add_multistate_item() for
details.

Note: This method is implemented only on macOS.

void global_menu_set_item_submenu(menu_root: String, idx: int, submenu:
String)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the submenu of the item at index `idx`. The submenu is the ID of a global
menu root that would be shown when the item is clicked.

Note: This method is implemented only on macOS.

void global_menu_set_item_tag(menu_root: String, idx: int, tag: Variant)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the metadata of an item, which may be of any type. You can later get it
with global_menu_get_item_tag(), which provides a simple way of assigning
context data to items.

Note: This method is implemented only on macOS.

void global_menu_set_item_text(menu_root: String, idx: int, text: String)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the text of the item at index `idx`.

Note: This method is implemented only on macOS.

void global_menu_set_item_tooltip(menu_root: String, idx: int, tooltip:
String)

Deprecated: Use NativeMenu or PopupMenu instead.

Sets the String tooltip of the item at the specified index `idx`.

Note: This method is implemented only on macOS.

void global_menu_set_popup_callbacks(menu_root: String, open_callback:
Callable, close_callback: Callable)

Deprecated: Use NativeMenu or PopupMenu instead.

Registers callables to emit when the menu is respectively about to show or
closed. Callback methods should have zero arguments.

bool has_additional_outputs() const

Returns `true` if any additional outputs have been registered via
register_additional_output().

bool has_feature(feature: Feature) const

Returns `true` if the specified `feature` is supported by the current
DisplayServer, `false` otherwise.

bool has_hardware_keyboard() const

Returns `true` if hardware keyboard is connected.

Note: This method is implemented on Android and iOS, on other platforms this
method always returns `true`.

void help_set_search_callbacks(search_callback: Callable, action_callback:
Callable)

Sets native help system search callbacks.

`search_callback` has the following arguments: `String search_string, int
result_limit` and return a Dictionary with "key, display name" pairs for the
search results. Called when the user enters search terms in the `Help` menu.

`action_callback` has the following arguments: `String key`. Called when the
user selects a search result in the `Help` menu.

Note: This method is implemented only on macOS.

Vector2i ime_get_selection() const

Returns the text selection in the Input Method Editor composition string, with
the Vector2i's `x` component being the caret position and `y` being the length
of the selection.

Note: This method is implemented only on macOS.

String ime_get_text() const

Returns the composition string contained within the Input Method Editor
window.

Note: This method is implemented only on macOS.

bool is_dark_mode() const

Returns `true` if OS is using dark mode.

Note: This method is implemented on Android, iOS, macOS, Windows, and Linux
(X11/Wayland).

bool is_dark_mode_supported() const

Returns `true` if OS supports dark mode.

Note: This method is implemented on Android, iOS, macOS, Windows, and Linux
(X11/Wayland).

bool is_touchscreen_available() const

Returns `true` if touch events are available (Android or iOS), the capability
is detected on the Web platform or if
ProjectSettings.input_devices/pointing/emulate_touch_from_mouse is `true`.

bool is_window_transparency_available() const

Returns `true` if the window background can be made transparent. This method
returns `false` if
ProjectSettings.display/window/per_pixel_transparency/allowed is set to
`false`, or if transparency is not supported by the renderer or OS compositor.

int keyboard_get_current_layout() const

Returns active keyboard layout index.

Note: This method is implemented on Linux (X11/Wayland), macOS, and Windows.

Key keyboard_get_keycode_from_physical(keycode: Key) const

Converts a physical (US QWERTY) `keycode` to one in the active keyboard
layout.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

Key keyboard_get_label_from_physical(keycode: Key) const

Converts a physical (US QWERTY) `keycode` to localized label printed on the
key in the active keyboard layout.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

int keyboard_get_layout_count() const

Returns the number of keyboard layouts.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

String keyboard_get_layout_language(index: int) const

Returns the ISO-639/BCP-47 language code of the keyboard layout at position
`index`.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

String keyboard_get_layout_name(index: int) const

Returns the localized name of the keyboard layout at position `index`.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

void keyboard_set_current_layout(index: int)

Sets the active keyboard layout.

Note: This method is implemented on Linux (X11/Wayland), macOS and Windows.

BitField[MouseButtonMask] mouse_get_button_state() const

Returns the current state of mouse buttons (whether each button is pressed) as
a bitmask. If multiple mouse buttons are pressed at the same time, the bits
are added together. Equivalent to Input.get_mouse_button_mask().

MouseMode mouse_get_mode() const

Returns the current mouse mode. See also mouse_set_mode().

Vector2i mouse_get_position() const

Returns the mouse cursor's current position in screen coordinates.

void mouse_set_mode(mouse_mode: MouseMode)

Sets the current mouse mode. See also mouse_get_mode().

void process_events()

Perform window manager processing, including input flushing. See also
force_process_and_drop_events(), Input.flush_buffered_events() and
Input.use_accumulated_input.

void register_additional_output(object: Object)

Registers an Object which represents an additional output that will be
rendered too, beyond normal windows. The Object is only used as an identifier,
which can be later passed to unregister_additional_output().

This can be used to prevent Godot from skipping rendering when no normal
windows are visible.

int screen_get_dpi(screen: int = -1) const

Returns the dots per inch density of the specified screen. If `screen` is
SCREEN_OF_MAIN_WINDOW (the default value), a screen with the main window will
be used.

Note: On macOS, returned value is inaccurate if fractional display scaling
mode is used.

Note: On Android devices, the actual screen densities are grouped into six
generalized densities:

    
    
       ldpi - 120 dpi
       mdpi - 160 dpi
       hdpi - 240 dpi
      xhdpi - 320 dpi
     xxhdpi - 480 dpi
    xxxhdpi - 640 dpi
    

Note: This method is implemented on Android, Linux (X11/Wayland), macOS and
Windows. Returns `72` on unsupported platforms.

Image screen_get_image(screen: int = -1) const

Returns screenshot of the `screen`.

Note: This method is implemented on Linux (X11), macOS, and Windows.

Note: On macOS, this method requires "Screen Recording" permission, if
permission is not granted it will return desktop wallpaper color.

Image screen_get_image_rect(rect: Rect2i) const

Returns screenshot of the screen `rect`.

Note: This method is implemented on macOS and Windows.

Note: On macOS, this method requires "Screen Recording" permission, if
permission is not granted it will return desktop wallpaper color.

float screen_get_max_scale() const

Returns the greatest scale factor of all screens.

Note: On macOS returned value is `2.0` if there is at least one hiDPI (Retina)
screen in the system, and `1.0` in all other cases.

Note: This method is implemented only on macOS.

ScreenOrientation screen_get_orientation(screen: int = -1) const

Returns the `screen`'s current orientation. See also screen_set_orientation().

Note: This method is implemented on Android and iOS.

Color screen_get_pixel(position: Vector2i) const

Returns color of the display pixel at the `position`.

Note: This method is implemented on Linux (X11), macOS, and Windows.

Note: On macOS, this method requires "Screen Recording" permission, if
permission is not granted it will return desktop wallpaper color.

Vector2i screen_get_position(screen: int = -1) const

Returns the screen's top-left corner position in pixels. On multi-monitor
setups, the screen position is relative to the virtual desktop area. On multi-
monitor setups with different screen resolutions or orientations, the origin
may be located outside any display like this:

    
    
    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+
    

See also screen_get_size().

Note: On Linux (Wayland) this method always returns `(0, 0)`.

float screen_get_refresh_rate(screen: int = -1) const

Returns the current refresh rate of the specified screen. If `screen` is
SCREEN_OF_MAIN_WINDOW (the default value), a screen with the main window will
be used.

Note: Returns `-1.0` if the DisplayServer fails to find the refresh rate for
the specified screen. On Web, screen_get_refresh_rate() will always return
`-1.0` as there is no way to retrieve the refresh rate on that platform.

To fallback to a default refresh rate if the method fails, try:

    
    
    var refresh_rate = DisplayServer.screen_get_refresh_rate()
    if refresh_rate < 0:
        refresh_rate = 60.0
    

float screen_get_scale(screen: int = -1) const

Returns the scale factor of the specified screen by index.

Note: On macOS, the returned value is `2.0` for hiDPI (Retina) screens, and
`1.0` for all other cases.

Note: On Linux (Wayland), the returned value is accurate only when `screen` is
SCREEN_OF_MAIN_WINDOW. Due to API limitations, passing a direct index will
return a rounded-up integer, if the screen has a fractional scale (e.g. `1.25`
would get rounded up to `2.0`).

Note: This method is implemented on Android, iOS, Web, macOS, and Linux
(Wayland).

Vector2i screen_get_size(screen: int = -1) const

Returns the screen's size in pixels. See also screen_get_position() and
screen_get_usable_rect().

Rect2i screen_get_usable_rect(screen: int = -1) const

Returns the portion of the screen that is not obstructed by a status bar in
pixels. See also screen_get_size().

bool screen_is_kept_on() const

Returns `true` if the screen should never be turned off by the operating
system's power-saving measures. See also screen_set_keep_on().

void screen_set_keep_on(enable: bool)

Sets whether the screen should never be turned off by the operating system's
power-saving measures. See also screen_is_kept_on().

void screen_set_orientation(orientation: ScreenOrientation, screen: int = -1)

Sets the `screen`'s `orientation`. See also screen_get_orientation().

Note: On iOS, this method has no effect if
ProjectSettings.display/window/handheld/orientation is not set to
SCREEN_SENSOR.

void set_icon(image: Image)

Sets the window icon (usually displayed in the top-left corner) with an Image.
To use icons in the operating system's native format, use set_native_icon()
instead.

Note: Requires support for FEATURE_ICON.

void set_native_icon(filename: String)

Sets the window icon (usually displayed in the top-left corner) in the
operating system's native format. The file at `filename` must be in `.ico`
format on Windows or `.icns` on macOS. By using specially crafted `.ico` or
`.icns` icons, set_native_icon() allows specifying different icons depending
on the size the icon is displayed at. This size is determined by the operating
system and user preferences (including the display scale factor). To use icons
in other formats, use set_icon() instead.

Note: Requires support for FEATURE_NATIVE_ICON.

void set_system_theme_change_callback(callable: Callable)

Sets the `callable` that should be called when system theme settings are
changed. Callback method should have zero arguments.

Note: This method is implemented on Android, iOS, macOS, Windows, and Linux
(X11/Wayland).

void show_emoji_and_symbol_picker() const

Opens system emoji and symbol picker.

Note: This method is implemented on macOS and Windows.

Rect2 status_indicator_get_rect(id: int) const

Returns the rectangle for the given status indicator `id` in screen
coordinates. If the status indicator is not visible, returns an empty Rect2.

Note: This method is implemented on macOS and Windows.

void status_indicator_set_callback(id: int, callback: Callable)

Sets the application status indicator activation callback. `callback` should
take two arguments: int mouse button index (one of MouseButton values) and
Vector2i click position in screen coordinates.

Note: This method is implemented on macOS and Windows.

void status_indicator_set_icon(id: int, icon: Texture2D)

Sets the application status indicator icon.

Note: This method is implemented on macOS and Windows.

void status_indicator_set_menu(id: int, menu_rid: RID)

Sets the application status indicator native popup menu.

Note: On macOS, the menu is activated by any mouse button. Its activation
callback is not triggered.

Note: On Windows, the menu is activated by the right mouse button, selecting
the status icon and pressing ``Shift` + `F10``, or the applications key. The
menu's activation callback for the other mouse buttons is still triggered.

Note: Native popup is only supported if NativeMenu supports the
NativeMenu.FEATURE_POPUP_MENU feature.

void status_indicator_set_tooltip(id: int, tooltip: String)

Sets the application status indicator tooltip.

Note: This method is implemented on macOS and Windows.

String tablet_get_current_driver() const

Returns current active tablet driver name.

Note: This method is implemented only on Windows.

int tablet_get_driver_count() const

Returns the total number of available tablet drivers.

Note: This method is implemented only on Windows.

String tablet_get_driver_name(idx: int) const

Returns the tablet driver name for the given index.

Note: This method is implemented only on Windows.

void tablet_set_current_driver(name: String)

Set active tablet driver name.

Supported drivers:

  * `winink`: Windows Ink API, default (Windows 8.1+ required).

  * `wintab`: Wacom Wintab API (compatible device driver required).

  * `dummy`: Dummy driver, tablet input is disabled.

Note: This method is implemented only on Windows.

Array[Dictionary] tts_get_voices() const

Returns an Array of voice information dictionaries.

Each Dictionary contains two String entries:

  * `name` is voice name.

  * `id` is voice identifier.

  * `language` is language code in `lang_Variant` format. The `lang` part is a 2 or 3-letter code based on the ISO-639 standard, in lowercase. The `Variant` part is an engine-dependent string describing country, region or/and dialect.

Note that Godot depends on system libraries for text-to-speech functionality.
These libraries are installed by default on Windows and macOS, but not on all
Linux distributions. If they are not present, this method will return an empty
list. This applies to both Godot users on Linux, as well as end-users on Linux
running Godot games that use text-to-speech.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

PackedStringArray tts_get_voices_for_language(language: String) const

Returns an PackedStringArray of voice identifiers for the `language`.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

bool tts_is_paused() const

Returns `true` if the synthesizer is in a paused state.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

bool tts_is_speaking() const

Returns `true` if the synthesizer is generating speech, or have utterance
waiting in the queue.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void tts_pause()

Puts the synthesizer into a paused state.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void tts_resume()

Resumes the synthesizer if it was paused.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void tts_set_utterance_callback(event: TTSUtteranceEvent, callable: Callable)

Adds a callback, which is called when the utterance has started, finished,
canceled or reached a text boundary.

  * TTS_UTTERANCE_STARTED, TTS_UTTERANCE_ENDED, and TTS_UTTERANCE_CANCELED callable's method should take one int parameter, the utterance ID.

  * TTS_UTTERANCE_BOUNDARY callable's method should take two int parameters, the index of the character and the utterance ID.

Note: The granularity of the boundary callbacks is engine dependent.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void tts_speak(text: String, voice: String, volume: int = 50, pitch: float =
1.0, rate: float = 1.0, utterance_id: int = 0, interrupt: bool = false)

Adds an utterance to the queue. If `interrupt` is `true`, the queue is cleared
first.

  * `voice` identifier is one of the `"id"` values returned by tts_get_voices() or one of the values returned by tts_get_voices_for_language().

  * `volume` ranges from `0` (lowest) to `100` (highest).

  * `pitch` ranges from `0.0` (lowest) to `2.0` (highest), `1.0` is default pitch for the current voice.

  * `rate` ranges from `0.1` (lowest) to `10.0` (highest), `1.0` is a normal speaking rate. Other values act as a percentage relative.

  * `utterance_id` is passed as a parameter to the callback functions.

Note: On Windows and Linux (X11/Wayland), utterance `text` can use SSML
markup. SSML support is engine and voice dependent. If the engine does not
support SSML, you should strip out all XML markup before calling tts_speak().

Note: The granularity of pitch, rate, and volume is engine and voice
dependent. Values may be truncated.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Wayland),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void tts_stop()

Stops synthesis in progress and removes all utterances from the queue.

Note: This method is implemented on Android, iOS, Web, Linux (X11/Linux),
macOS, and Windows.

Note: ProjectSettings.audio/general/text_to_speech should be `true` to use
text-to-speech.

void unregister_additional_output(object: Object)

Unregisters an Object representing an additional output, that was registered
via register_additional_output().

int virtual_keyboard_get_height() const

Returns the on-screen keyboard's height in pixels. Returns 0 if there is no
keyboard or if it is currently hidden.

void virtual_keyboard_hide()

Hides the virtual keyboard if it is shown, does nothing otherwise.

void virtual_keyboard_show(existing_text: String, position: Rect2 = Rect2(0,
0, 0, 0), type: VirtualKeyboardType = 0, max_length: int = -1, cursor_start:
int = -1, cursor_end: int = -1)

Shows the virtual keyboard if the platform has one.

`existing_text` parameter is useful for implementing your own LineEdit or
TextEdit, as it tells the virtual keyboard what text has already been typed
(the virtual keyboard uses it for auto-correct and predictions).

`position` parameter is the screen space Rect2 of the edited text.

`type` parameter allows configuring which type of virtual keyboard to show.

`max_length` limits the number of characters that can be entered if different
from `-1`.

`cursor_start` can optionally define the current text cursor position if
`cursor_end` is not set.

`cursor_start` and `cursor_end` can optionally define the current text
selection.

Note: This method is implemented on Android, iOS and Web.

void warp_mouse(position: Vector2i)

Sets the mouse cursor position to the given `position` relative to an origin
at the upper left corner of the currently focused game Window Manager window.

Note: warp_mouse() is only supported on Windows, macOS, and Linux
(X11/Wayland). It has no effect on Android, iOS, and Web.

bool window_can_draw(window_id: int = 0) const

Returns `true` if anything can be drawn in the window specified by
`window_id`, `false` otherwise. Using the `--disable-render-loop` command line
argument or a headless build will return `false`.

int window_get_active_popup() const

Returns ID of the active popup window, or INVALID_WINDOW_ID if there is none.

int window_get_attached_instance_id(window_id: int = 0) const

Returns the Object.get_instance_id() of the Window the `window_id` is attached
to.

int window_get_current_screen(window_id: int = 0) const

Returns the screen the window specified by `window_id` is currently positioned
on. If the screen overlaps multiple displays, the screen where the window's
center is located is returned. See also window_set_current_screen().

bool window_get_flag(flag: WindowFlags, window_id: int = 0) const

Returns the current value of the given window's `flag`.

Vector2i window_get_max_size(window_id: int = 0) const

Returns the window's maximum size (in pixels). See also window_set_max_size().

Vector2i window_get_min_size(window_id: int = 0) const

Returns the window's minimum size (in pixels). See also window_set_min_size().

WindowMode window_get_mode(window_id: int = 0) const

Returns the mode of the given window.

int window_get_native_handle(handle_type: HandleType, window_id: int = 0)
const

Returns internal structure pointers for use in plugins.

Note: This method is implemented on Android, Linux (X11/Wayland), macOS, and
Windows.

Rect2i window_get_popup_safe_rect(window: int) const

Returns the bounding box of control, or menu item that was used to open the
popup window, in the screen coordinate system.

Vector2i window_get_position(window_id: int = 0) const

Returns the position of the client area of the given window on the screen.

Vector2i window_get_position_with_decorations(window_id: int = 0) const

Returns the position of the given window on the screen including the borders
drawn by the operating system. See also window_get_position().

Vector3i window_get_safe_title_margins(window_id: int = 0) const

Returns left margins (`x`), right margins (`y`) and height (`z`) of the title
that are safe to use (contains no buttons or other elements) when
WINDOW_FLAG_EXTEND_TO_TITLE flag is set.

Vector2i window_get_size(window_id: int = 0) const

Returns the size of the window specified by `window_id` (in pixels), excluding
the borders drawn by the operating system. This is also called the "client
area". See also window_get_size_with_decorations(), window_set_size() and
window_get_position().

Vector2i window_get_size_with_decorations(window_id: int = 0) const

Returns the size of the window specified by `window_id` (in pixels), including
the borders drawn by the operating system. See also window_get_size().

Vector2i window_get_title_size(title: String, window_id: int = 0) const

Returns the estimated window title bar size (including text and window
buttons) for the window specified by `window_id` (in pixels). This method does
not change the window title.

Note: This method is implemented on macOS and Windows.

VSyncMode window_get_vsync_mode(window_id: int = 0) const

Returns the V-Sync mode of the given window.

bool window_is_focused(window_id: int = 0) const

Returns `true` if the window specified by `window_id` is focused.

bool window_is_maximize_allowed(window_id: int = 0) const

Returns `true` if the given window can be maximized (the maximize button is
enabled).

bool window_maximize_on_title_dbl_click() const

Returns `true`, if double-click on a window title should maximize it.

Note: This method is implemented only on macOS.

bool window_minimize_on_title_dbl_click() const

Returns `true`, if double-click on a window title should minimize it.

Note: This method is implemented only on macOS.

void window_move_to_foreground(window_id: int = 0)

Moves the window specified by `window_id` to the foreground, so that it is
visible over other windows.

void window_request_attention(window_id: int = 0)

Makes the window specified by `window_id` request attention, which is
materialized by the window title and taskbar entry blinking until the window
is focused. This usually has no visible effect if the window is currently
focused. The exact behavior varies depending on the operating system.

void window_set_current_screen(screen: int, window_id: int = 0)

Moves the window specified by `window_id` to the specified `screen`. See also
window_get_current_screen().

void window_set_drop_files_callback(callback: Callable, window_id: int = 0)

Sets the `callback` that should be called when files are dropped from the
operating system's file manager to the window specified by `window_id`.
`callback` should take one PackedStringArray argument, which is the list of
dropped files.

Warning: Advanced users only! Adding such a callback to a Window node will
override its default implementation, which can introduce bugs.

Note: This method is implemented on Windows, macOS, Linux (X11/Wayland), and
Web.

void window_set_exclusive(window_id: int, exclusive: bool)

If set to `true`, this window will always stay on top of its parent window,
parent window will ignore input while this window is opened.

Note: On macOS, exclusive windows are confined to the same space (virtual
desktop or screen) as the parent window.

Note: This method is implemented on macOS and Windows.

void window_set_flag(flag: WindowFlags, enabled: bool, window_id: int = 0)

Enables or disables the given window's given `flag`. See WindowFlags for
possible values and their behavior.

void window_set_ime_active(active: bool, window_id: int = 0)

Sets whether Input Method Editor should be enabled for the window specified by
`window_id`. See also window_set_ime_position().

void window_set_ime_position(position: Vector2i, window_id: int = 0)

Sets the position of the Input Method Editor popup for the specified
`window_id`. Only effective if window_set_ime_active() was set to `true` for
the specified `window_id`.

void window_set_input_event_callback(callback: Callable, window_id: int = 0)

Sets the `callback` that should be called when any InputEvent is sent to the
window specified by `window_id`.

Warning: Advanced users only! Adding such a callback to a Window node will
override its default implementation, which can introduce bugs.

void window_set_input_text_callback(callback: Callable, window_id: int = 0)

Sets the `callback` that should be called when text is entered using the
virtual keyboard to the window specified by `window_id`.

Warning: Advanced users only! Adding such a callback to a Window node will
override its default implementation, which can introduce bugs.

void window_set_max_size(max_size: Vector2i, window_id: int = 0)

Sets the maximum size of the window specified by `window_id` in pixels.
Normally, the user will not be able to drag the window to make it larger than
the specified size. See also window_get_max_size().

Note: It's recommended to change this value using Window.max_size instead.

Note: Using third-party tools, it is possible for users to disable window
geometry restrictions and therefore bypass this limit.

void window_set_min_size(min_size: Vector2i, window_id: int = 0)

Sets the minimum size for the given window to `min_size` in pixels. Normally,
the user will not be able to drag the window to make it smaller than the
specified size. See also window_get_min_size().

Note: It's recommended to change this value using Window.min_size instead.

Note: By default, the main window has a minimum size of `Vector2i(64, 64)`.
This prevents issues that can arise when the window is resized to a near-zero
size.

Note: Using third-party tools, it is possible for users to disable window
geometry restrictions and therefore bypass this limit.

void window_set_mode(mode: WindowMode, window_id: int = 0)

Sets window mode for the given window to `mode`. See WindowMode for possible
values and how each mode behaves.

Note: On Android, setting it to WINDOW_MODE_FULLSCREEN or
WINDOW_MODE_EXCLUSIVE_FULLSCREEN will enable immersive mode.

Note: Setting the window to full screen forcibly sets the borderless flag to
`true`, so make sure to set it back to `false` when not wanted.

void window_set_mouse_passthrough(region: PackedVector2Array, window_id: int =
0)

Sets a polygonal region of the window which accepts mouse events. Mouse events
outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse events will
be intercepted by the window, which is the default behavior).

GDScriptC#

    
    
    # Set region, using Path2D node.
    DisplayServer.window_set_mouse_passthrough($Path2D.curve.get_baked_points())
    
    # Set region, using Polygon2D node.
    DisplayServer.window_set_mouse_passthrough($Polygon2D.polygon)
    
    # Reset region to default.
    DisplayServer.window_set_mouse_passthrough([])
    
    
    
    // Set region, using Path2D node.
    DisplayServer.WindowSetMousePassthrough(GetNode<Path2D>("Path2D").Curve.GetBakedPoints());
    
    // Set region, using Polygon2D node.
    DisplayServer.WindowSetMousePassthrough(GetNode<Polygon2D>("Polygon2D").Polygon);
    
    // Reset region to default.
    DisplayServer.WindowSetMousePassthrough([]);
    

Note: On Windows, the portion of a window that lies outside the region is not
drawn, while on Linux (X11) and macOS it is.

Note: This method is implemented on Linux (X11), macOS and Windows.

void window_set_popup_safe_rect(window: int, rect: Rect2i)

Sets the bounding box of control, or menu item that was used to open the popup
window, in the screen coordinate system. Clicking this area will not auto-
close this popup.

void window_set_position(position: Vector2i, window_id: int = 0)

Sets the position of the given window to `position`. On multi-monitor setups,
the screen position is relative to the virtual desktop area. On multi-monitor
setups with different screen resolutions or orientations, the origin may be
located outside any display like this:

    
    
    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+
    

See also window_get_position() and window_set_size().

Note: It's recommended to change this value using Window.position instead.

Note: On Linux (Wayland): this method is a no-op.

void window_set_rect_changed_callback(callback: Callable, window_id: int = 0)

Sets the `callback` that will be called when the window specified by
`window_id` is moved or resized.

Warning: Advanced users only! Adding such a callback to a Window node will
override its default implementation, which can introduce bugs.

void window_set_size(size: Vector2i, window_id: int = 0)

Sets the size of the given window to `size` (in pixels). See also
window_get_size() and window_get_position().

Note: It's recommended to change this value using Window.size instead.

void window_set_title(title: String, window_id: int = 0)

Sets the title of the given window to `title`.

Note: It's recommended to change this value using Window.title instead.

Note: Avoid changing the window title every frame, as this can cause
performance issues on certain window managers. Try to change the window title
only a few times per second at most.

void window_set_transient(window_id: int, parent_window_id: int)

Sets window transient parent. Transient window will be destroyed with its
transient parent and will return focus to their parent when closed. The
transient window is displayed on top of a non-exclusive full-screen parent
window. Transient windows can't enter full-screen mode.

Note: It's recommended to change this value using Window.transient instead.

Note: The behavior might be different depending on the platform.

void window_set_vsync_mode(vsync_mode: VSyncMode, window_id: int = 0)

Sets the V-Sync mode of the given window. See also
ProjectSettings.display/window/vsync/vsync_mode.

See VSyncMode for possible values and how they affect the behavior of your
application.

Depending on the platform and used renderer, the engine will fall back to
VSYNC_ENABLED if the desired mode is not supported.

Note: V-Sync modes other than VSYNC_ENABLED are only supported in the Forward+
and Mobile rendering methods, not Compatibility.

void window_set_window_buttons_offset(offset: Vector2i, window_id: int = 0)

When WINDOW_FLAG_EXTEND_TO_TITLE flag is set, set offset to the center of the
first titlebar button.

Note: This flag is implemented only on macOS.

void window_set_window_event_callback(callback: Callable, window_id: int = 0)

Sets the `callback` that will be called when an event occurs in the window
specified by `window_id`.

Warning: Advanced users only! Adding such a callback to a Window node will
override its default implementation, which can introduce bugs.

void window_start_drag(window_id: int = 0)

Starts an interactive drag operation on the window with the given `window_id`,
using the current mouse position. Call this method when handling a mouse
button being pressed to simulate a pressed event on the window's title bar.
Using this method allows the window to participate in space switching, tiling,
and other system features.

Note: This method is implemented on Linux (X11/Wayland), macOS, and Windows.

void window_start_resize(edge: WindowResizeEdge, window_id: int = 0)

Starts an interactive resize operation on the window with the given
`window_id`, using the current mouse position. Call this method when handling
a mouse button being pressed to simulate a pressed event on the window's edge.

Note: This method is implemented on Linux (X11/Wayland), macOS, and Windows.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[BitField]: This value is an integer composed as a bitmask of the following flags.

