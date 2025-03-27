# Slider

Inherits: Range < Control < CanvasItem < Node < Object

Inherited By: HSlider, VSlider

Abstract base class for sliders.

## Description

Abstract base class for sliders, used to adjust a value by moving a grabber
along a horizontal or vertical axis. Sliders are Range-based controls.

## Properties

bool | editable | `true`  
---|---|---  
FocusMode | focus_mode | `2` (overrides Control)  
bool | scrollable | `true`  
float | step | `1.0` (overrides Range)  
int | tick_count | `0`  
bool | ticks_on_borders | `false`  
  
## Theme Properties

int | center_grabber | `0`  
---|---|---  
int | grabber_offset | `0`  
Texture2D | grabber  
Texture2D | grabber_disabled  
Texture2D | grabber_highlight  
Texture2D | tick  
StyleBox | grabber_area  
StyleBox | grabber_area_highlight  
StyleBox | slider  
  
## Signals

drag_ended(value_changed: bool)

Emitted when the grabber stops being dragged. If `value_changed` is `true`,
Range.value is different from the value when the dragging was started.

drag_started()

Emitted when the grabber starts being dragged. This is emitted before the
corresponding Range.value_changed signal.

## Property Descriptions

bool editable = `true`

  * void set_editable(value: bool)

  * bool is_editable()

If `true`, the slider can be interacted with. If `false`, the value can be
changed only by code.

bool scrollable = `true`

  * void set_scrollable(value: bool)

  * bool is_scrollable()

If `true`, the value can be changed using the mouse wheel.

int tick_count = `0`

  * void set_ticks(value: int)

  * int get_ticks()

Number of ticks displayed on the slider, including border ticks. Ticks are
uniformly-distributed value markers.

bool ticks_on_borders = `false`

  * void set_ticks_on_borders(value: bool)

  * bool get_ticks_on_borders()

If `true`, the slider will display ticks for minimum and maximum values.

## Theme Property Descriptions

int center_grabber = `0`

Boolean constant. If `1`, the grabber texture size will be ignored and it will
fit within slider's bounds based only on its center position.

int grabber_offset = `0`

Vertical or horizontal offset of the grabber.

Texture2D grabber

The texture for the grabber (the draggable element).

Texture2D grabber_disabled

The texture for the grabber when it's disabled.

Texture2D grabber_highlight

The texture for the grabber when it's focused.

Texture2D tick

The texture for the ticks, visible when tick_count is greater than 0.

StyleBox grabber_area

The background of the area to the left or bottom of the grabber.

StyleBox grabber_area_highlight

The background of the area to the left or bottom of the grabber that displays
when it's being hovered or focused.

StyleBox slider

The background for the whole slider. Affects the height or width of the
grabber_area.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

