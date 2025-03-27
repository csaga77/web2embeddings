# ColorPicker

Inherits: VBoxContainer < BoxContainer < Container < Control < CanvasItem <
Node < Object

A widget that provides an interface for selecting or modifying a color.

## Description

A widget that provides an interface for selecting or modifying a color. It can
optionally provide functionalities like a color sampler (eyedropper), color
modes, and presets.

Note: This control is the color picker widget itself. You can use a
ColorPickerButton instead if you need a button that brings up a ColorPicker in
a popup.

## Tutorials

  * Tween Interpolation Demo

## Properties

bool | can_add_swatches | `true`  
---|---|---  
Color | color | `Color(1, 1, 1, 1)`  
ColorModeType | color_mode | `0`  
bool | color_modes_visible | `true`  
bool | deferred_mode | `false`  
bool | edit_alpha | `true`  
bool | hex_visible | `true`  
PickerShapeType | picker_shape | `0`  
bool | presets_visible | `true`  
bool | sampler_visible | `true`  
bool | sliders_visible | `true`  
  
## Methods

void | add_preset(color: Color)  
---|---  
void | add_recent_preset(color: Color)  
void | erase_preset(color: Color)  
void | erase_recent_preset(color: Color)  
PackedColorArray | get_presets() const  
PackedColorArray | get_recent_presets() const  
  
## Theme Properties

int | center_slider_grabbers | `1`  
---|---|---  
int | h_width | `30`  
int | label_width | `10`  
int | margin | `4`  
int | sv_height | `256`  
int | sv_width | `256`  
Texture2D | add_preset  
Texture2D | bar_arrow  
Texture2D | color_hue  
Texture2D | expanded_arrow  
Texture2D | folded_arrow  
Texture2D | menu_option  
Texture2D | overbright_indicator  
Texture2D | picker_cursor  
Texture2D | picker_cursor_bg  
Texture2D | sample_bg  
Texture2D | sample_revert  
Texture2D | screen_picker  
Texture2D | shape_circle  
Texture2D | shape_rect  
Texture2D | shape_rect_wheel  
  
## Signals

color_changed(color: Color)

Emitted when the color is changed.

preset_added(color: Color)

Emitted when a preset is added.

preset_removed(color: Color)

Emitted when a preset is removed.

## Enumerations

enum ColorModeType:

ColorModeType MODE_RGB = `0`

Allows editing the color with Red/Green/Blue sliders.

ColorModeType MODE_HSV = `1`

Allows editing the color with Hue/Saturation/Value sliders.

ColorModeType MODE_RAW = `2`

Allows the color R, G, B component values to go beyond 1.0, which can be used
for certain special operations that require it (like tinting without darkening
or rendering sprites in HDR).

ColorModeType MODE_OKHSL = `3`

Allows editing the color with Hue/Saturation/Lightness sliders.

OKHSL is a new color space similar to HSL but that better match perception by
leveraging the Oklab color space which is designed to be simple to use, while
doing a good job at predicting perceived lightness, chroma and hue.

Okhsv and Okhsl color spaces

enum PickerShapeType:

PickerShapeType SHAPE_HSV_RECTANGLE = `0`

HSV Color Model rectangle color space.

PickerShapeType SHAPE_HSV_WHEEL = `1`

HSV Color Model rectangle color space with a wheel.

PickerShapeType SHAPE_VHS_CIRCLE = `2`

HSV Color Model circle color space. Use Saturation as a radius.

PickerShapeType SHAPE_OKHSL_CIRCLE = `3`

HSL OK Color Model circle color space.

PickerShapeType SHAPE_NONE = `4`

The color space shape and the shape select button are hidden. Can't be
selected from the shapes popup.

## Property Descriptions

bool can_add_swatches = `true`

  * void set_can_add_swatches(value: bool)

  * bool are_swatches_enabled()

If `true`, it's possible to add presets under Swatches. If `false`, the button
to add presets is disabled.

Color color = `Color(1, 1, 1, 1)`

  * void set_pick_color(value: Color)

  * Color get_pick_color()

The currently selected color.

ColorModeType color_mode = `0`

  * void set_color_mode(value: ColorModeType)

  * ColorModeType get_color_mode()

The currently selected color mode. See ColorModeType.

bool color_modes_visible = `true`

  * void set_modes_visible(value: bool)

  * bool are_modes_visible()

If `true`, the color mode buttons are visible.

bool deferred_mode = `false`

  * void set_deferred_mode(value: bool)

  * bool is_deferred_mode()

If `true`, the color will apply only after the user releases the mouse button,
otherwise it will apply immediately even in mouse motion event (which can
cause performance issues).

bool edit_alpha = `true`

  * void set_edit_alpha(value: bool)

  * bool is_editing_alpha()

If `true`, shows an alpha channel slider (opacity).

bool hex_visible = `true`

  * void set_hex_visible(value: bool)

  * bool is_hex_visible()

If `true`, the hex color code input field is visible.

PickerShapeType picker_shape = `0`

  * void set_picker_shape(value: PickerShapeType)

  * PickerShapeType get_picker_shape()

The shape of the color space view. See PickerShapeType.

bool presets_visible = `true`

  * void set_presets_visible(value: bool)

  * bool are_presets_visible()

If `true`, the Swatches and Recent Colors presets are visible.

bool sampler_visible = `true`

  * void set_sampler_visible(value: bool)

  * bool is_sampler_visible()

If `true`, the color sampler and color preview are visible.

bool sliders_visible = `true`

  * void set_sliders_visible(value: bool)

  * bool are_sliders_visible()

If `true`, the color sliders are visible.

## Method Descriptions

void add_preset(color: Color)

Adds the given color to a list of color presets. The presets are displayed in
the color picker and the user will be able to select them.

Note: The presets list is only for this color picker.

void add_recent_preset(color: Color)

Adds the given color to a list of color recent presets so that it can be
picked later. Recent presets are the colors that were picked recently, a new
preset is automatically created and added to recent presets when you pick a
new color.

Note: The recent presets list is only for this color picker.

void erase_preset(color: Color)

Removes the given color from the list of color presets of this color picker.

void erase_recent_preset(color: Color)

Removes the given color from the list of color recent presets of this color
picker.

PackedColorArray get_presets() const

Returns the list of colors in the presets of the color picker.

PackedColorArray get_recent_presets() const

Returns the list of colors in the recent presets of the color picker.

## Theme Property Descriptions

int center_slider_grabbers = `1`

Overrides the Slider.center_grabber theme property of the sliders.

int h_width = `30`

The width of the hue selection slider.

int label_width = `10`

The minimum width of the color labels next to sliders.

int margin = `4`

The margin around the ColorPicker.

int sv_height = `256`

The height of the saturation-value selection box.

int sv_width = `256`

The width of the saturation-value selection box.

Texture2D add_preset

The icon for the "Add Preset" button.

Texture2D bar_arrow

The texture for the arrow grabber.

Texture2D color_hue

Custom texture for the hue selection slider on the right.

Texture2D expanded_arrow

The icon for color preset drop down menu when expanded.

Texture2D folded_arrow

The icon for color preset drop down menu when folded.

Texture2D menu_option

The icon for color preset option menu.

Texture2D overbright_indicator

The indicator used to signalize that the color value is outside the 0-1 range.

Texture2D picker_cursor

The image displayed over the color box/circle (depending on the picker_shape),
marking the currently selected color.

Texture2D picker_cursor_bg

The fill image displayed behind the picker cursor.

Texture2D sample_bg

Background panel for the color preview box (visible when the color is
translucent).

Texture2D sample_revert

The icon for the revert button (visible on the middle of the "old" color when
it differs from the currently selected color). This icon is modulated with a
dark color if the "old" color is bright enough, so the icon should be bright
to ensure visibility in both scenarios.

Texture2D screen_picker

The icon for the screen color picker button.

Texture2D shape_circle

The icon for circular picker shapes.

Texture2D shape_rect

The icon for rectangular picker shapes.

Texture2D shape_rect_wheel

The icon for rectangular wheel picker shapes.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

