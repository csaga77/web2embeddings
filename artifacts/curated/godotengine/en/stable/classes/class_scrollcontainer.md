# ScrollContainer

Inherits: Container < Control < CanvasItem < Node < Object

Inherited By: EditorInspector

A container used to provide scrollbars to a child control when needed.

## Description

A container used to provide a child control with scrollbars when needed.
Scrollbars will automatically be drawn at the right (for vertical) or bottom
(for horizontal) and will enable dragging to move the viewable Control (and
its children) within the ScrollContainer. Scrollbars will also automatically
resize the grabber based on the Control.custom_minimum_size of the Control
relative to the ScrollContainer.

## Tutorials

  * Using Containers

## Properties

bool | clip_contents | `true` (overrides Control)  
---|---|---  
bool | draw_focus_border | `false`  
bool | follow_focus | `false`  
ScrollMode | horizontal_scroll_mode | `1`  
int | scroll_deadzone | `0`  
int | scroll_horizontal | `0`  
float | scroll_horizontal_custom_step | `-1.0`  
int | scroll_vertical | `0`  
float | scroll_vertical_custom_step | `-1.0`  
ScrollMode | vertical_scroll_mode | `1`  
  
## Methods

void | ensure_control_visible(control: Control)  
---|---  
HScrollBar | get_h_scroll_bar()  
VScrollBar | get_v_scroll_bar()  
  
## Theme Properties

StyleBox | focus  
---|---  
StyleBox | panel  
  
## Signals

scroll_ended()

Emitted when scrolling stops when dragging the scrollable area with a touch
event. This signal is not emitted when scrolling by dragging the scrollbar,
scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

Note: This signal is only emitted on Android or iOS, or on desktop/web
platforms when ProjectSettings.input_devices/pointing/emulate_touch_from_mouse
is enabled.

scroll_started()

Emitted when scrolling starts when dragging the scrollable area with a touch
event. This signal is not emitted when scrolling by dragging the scrollbar,
scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

Note: This signal is only emitted on Android or iOS, or on desktop/web
platforms when ProjectSettings.input_devices/pointing/emulate_touch_from_mouse
is enabled.

## Enumerations

enum ScrollMode:

ScrollMode SCROLL_MODE_DISABLED = `0`

Scrolling disabled, scrollbar will be invisible.

ScrollMode SCROLL_MODE_AUTO = `1`

Scrolling enabled, scrollbar will be visible only if necessary, i.e.
container's content is bigger than the container.

ScrollMode SCROLL_MODE_SHOW_ALWAYS = `2`

Scrolling enabled, scrollbar will be always visible.

ScrollMode SCROLL_MODE_SHOW_NEVER = `3`

Scrolling enabled, scrollbar will be hidden.

ScrollMode SCROLL_MODE_RESERVE = `4`

Combines SCROLL_MODE_AUTO and SCROLL_MODE_SHOW_ALWAYS. The scrollbar is only
visible if necessary, but the content size is adjusted as if it was always
visible. It's useful for ensuring that content size stays the same regardless
if the scrollbar is visible.

## Property Descriptions

bool draw_focus_border = `false`

  * void set_draw_focus_border(value: bool)

  * bool get_draw_focus_border()

If `true`, focus is drawn when the ScrollContainer or one of its descendant
nodes is focused.

bool follow_focus = `false`

  * void set_follow_focus(value: bool)

  * bool is_following_focus()

If `true`, the ScrollContainer will automatically scroll to focused children
(including indirect children) to make sure they are fully visible.

ScrollMode horizontal_scroll_mode = `1`

  * void set_horizontal_scroll_mode(value: ScrollMode)

  * ScrollMode get_horizontal_scroll_mode()

Controls whether horizontal scrollbar can be used and when it should be
visible. See ScrollMode for options.

int scroll_deadzone = `0`

  * void set_deadzone(value: int)

  * int get_deadzone()

Deadzone for touch scrolling. Lower deadzone makes the scrolling more
sensitive.

int scroll_horizontal = `0`

  * void set_h_scroll(value: int)

  * int get_h_scroll()

The current horizontal scroll value.

Note: If you are setting this value in the Node._ready() function or earlier,
it needs to be wrapped with Object.set_deferred(), since scroll bar's
Range.max_value is not initialized yet.

    
    
    func _ready():
        set_deferred("scroll_horizontal", 600)
    

float scroll_horizontal_custom_step = `-1.0`

  * void set_horizontal_custom_step(value: float)

  * float get_horizontal_custom_step()

Overrides the ScrollBar.custom_step used when clicking the internal scroll
bar's horizontal increment and decrement buttons or when using arrow keys when
the ScrollBar is focused.

int scroll_vertical = `0`

  * void set_v_scroll(value: int)

  * int get_v_scroll()

The current vertical scroll value.

Note: Setting it early needs to be deferred, just like in scroll_horizontal.

    
    
    func _ready():
        set_deferred("scroll_vertical", 600)
    

float scroll_vertical_custom_step = `-1.0`

  * void set_vertical_custom_step(value: float)

  * float get_vertical_custom_step()

Overrides the ScrollBar.custom_step used when clicking the internal scroll
bar's vertical increment and decrement buttons or when using arrow keys when
the ScrollBar is focused.

ScrollMode vertical_scroll_mode = `1`

  * void set_vertical_scroll_mode(value: ScrollMode)

  * ScrollMode get_vertical_scroll_mode()

Controls whether vertical scrollbar can be used and when it should be visible.
See ScrollMode for options.

## Method Descriptions

void ensure_control_visible(control: Control)

Ensures the given `control` is visible (must be a direct or indirect child of
the ScrollContainer). Used by follow_focus.

Note: This will not work on a node that was just added during the same frame.
If you want to scroll to a newly added child, you must wait until the next
frame using SceneTree.process_frame:

    
    
    add_child(child_node)
    await get_tree().process_frame
    ensure_control_visible(child_node)
    

HScrollBar get_h_scroll_bar()

Returns the horizontal scrollbar HScrollBar of this ScrollContainer.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to disable or hide a scrollbar, you can use
horizontal_scroll_mode.

VScrollBar get_v_scroll_bar()

Returns the vertical scrollbar VScrollBar of this ScrollContainer.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to disable or hide a scrollbar, you can use
vertical_scroll_mode.

## Theme Property Descriptions

StyleBox focus

The focus border StyleBox of the ScrollContainer. Only used if
draw_focus_border is `true`.

StyleBox panel

The background StyleBox of the ScrollContainer.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

