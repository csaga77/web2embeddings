# SplitContainer

Inherits: Container < Control < CanvasItem < Node < Object

Inherited By: HSplitContainer, VSplitContainer

A container that splits two child controls horizontally or vertically and
provides a grabber for adjusting the split ratio.

## Description

A container that accepts only two child controls, then arranges them
horizontally or vertically and creates a divisor between them. The divisor can
be dragged around to change the size relation between the child controls.

## Tutorials

  * Using Containers

## Properties

bool | collapsed | `false`  
---|---|---  
bool | drag_area_highlight_in_editor | `false`  
int | drag_area_margin_begin | `0`  
int | drag_area_margin_end | `0`  
int | drag_area_offset | `0`  
DraggerVisibility | dragger_visibility | `0`  
bool | dragging_enabled | `true`  
int | split_offset | `0`  
bool | vertical | `false`  
  
## Methods

void | clamp_split_offset()  
---|---  
Control | get_drag_area_control()  
  
## Theme Properties

int | autohide | `1`  
---|---|---  
int | minimum_grab_thickness | `6`  
int | separation | `12`  
Texture2D | grabber  
Texture2D | h_grabber  
Texture2D | v_grabber  
StyleBox | split_bar_background  
  
## Signals

drag_ended()

Emitted when the user ends dragging.

drag_started()

Emitted when the user starts dragging.

dragged(offset: int)

Emitted when the dragger is dragged by user.

## Enumerations

enum DraggerVisibility:

DraggerVisibility DRAGGER_VISIBLE = `0`

The split dragger icon is always visible when autohide is `false`, otherwise
visible only when the cursor hovers it.

The size of the grabber icon determines the minimum separation.

The dragger icon is automatically hidden if the length of the grabber icon is
longer than the split bar.

DraggerVisibility DRAGGER_HIDDEN = `1`

The split dragger icon is never visible regardless of the value of autohide.

The size of the grabber icon determines the minimum separation.

DraggerVisibility DRAGGER_HIDDEN_COLLAPSED = `2`

The split dragger icon is not visible, and the split bar is collapsed to zero
thickness.

## Property Descriptions

bool collapsed = `false`

  * void set_collapsed(value: bool)

  * bool is_collapsed()

If `true`, the dragger will be disabled and the children will be sized as if
the split_offset was `0`.

bool drag_area_highlight_in_editor = `false`

  * void set_drag_area_highlight_in_editor(value: bool)

  * bool is_drag_area_highlight_in_editor_enabled()

Highlights the drag area Rect2 so you can see where it is during development.
The drag area is gold if dragging_enabled is `true`, and red if `false`.

int drag_area_margin_begin = `0`

  * void set_drag_area_margin_begin(value: int)

  * int get_drag_area_margin_begin()

Reduces the size of the drag area and split bar split_bar_background at the
beginning of the container.

int drag_area_margin_end = `0`

  * void set_drag_area_margin_end(value: int)

  * int get_drag_area_margin_end()

Reduces the size of the drag area and split bar split_bar_background at the
end of the container.

int drag_area_offset = `0`

  * void set_drag_area_offset(value: int)

  * int get_drag_area_offset()

Shifts the drag area in the axis of the container to prevent the drag area
from overlapping the ScrollBar or other selectable Control of a child node.

DraggerVisibility dragger_visibility = `0`

  * void set_dragger_visibility(value: DraggerVisibility)

  * DraggerVisibility get_dragger_visibility()

Determines the dragger's visibility. See DraggerVisibility for details. This
property does not determine whether dragging is enabled or not. Use
dragging_enabled for that.

bool dragging_enabled = `true`

  * void set_dragging_enabled(value: bool)

  * bool is_dragging_enabled()

Enables or disables split dragging.

int split_offset = `0`

  * void set_split_offset(value: int)

  * int get_split_offset()

The initial offset of the splitting between the two Controls, with `0` being
at the end of the first Control.

bool vertical = `false`

  * void set_vertical(value: bool)

  * bool is_vertical()

If `true`, the SplitContainer will arrange its children vertically, rather
than horizontally.

Can't be changed when using HSplitContainer and VSplitContainer.

## Method Descriptions

void clamp_split_offset()

Clamps the split_offset value to not go outside the currently possible minimal
and maximum values.

Control get_drag_area_control()

Returns the drag area Control. For example, you can move a pre-configured
button into the drag area Control so that it rides along with the split bar.
Try setting the Button anchors to `center` prior to the `reparent()` call.

    
    
    $BarnacleButton.reparent($SplitContainer.get_drag_area_control())
    

Note: The drag area Control is drawn over the SplitContainer's children, so
CanvasItem draw objects called from the Control and children added to the
Control will also appear over the SplitContainer's children. Try setting
Control.mouse_filter of custom children to Control.MOUSE_FILTER_IGNORE to
prevent blocking the mouse from dragging if desired.

Warning: This is a required internal node, removing and freeing it may cause a
crash.

## Theme Property Descriptions

int autohide = `1`

Boolean value. If `1` (`true`), the grabber will hide automatically when it
isn't under the cursor. If `0` (`false`), it's always visible. The
dragger_visibility must be DRAGGER_VISIBLE.

int minimum_grab_thickness = `6`

The minimum thickness of the area users can click on to grab the split bar.
This ensures that the split bar can still be dragged if separation or
h_grabber / v_grabber's size is too narrow to easily select.

int separation = `12`

The split bar thickness, i.e., the gap between the two children of the
container. This is overridden by the size of the grabber icon if
dragger_visibility is set to DRAGGER_VISIBLE, or DRAGGER_HIDDEN, and
separation is smaller than the size of the grabber icon in the same axis.

Note: To obtain separation values less than the size of the grabber icon, for
example a `1 px` hairline, set h_grabber or v_grabber to a new ImageTexture,
which effectively sets the grabber icon size to `0 px`.

Texture2D grabber

The icon used for the grabber drawn in the middle area.

Texture2D h_grabber

The icon used for the grabber drawn in the middle area when vertical is
`false`.

Texture2D v_grabber

The icon used for the grabber drawn in the middle area when vertical is
`true`.

StyleBox split_bar_background

Determines the background of the split bar if its thickness is greater than
zero.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

