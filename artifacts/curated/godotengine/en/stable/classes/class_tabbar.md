# TabBar

Inherits: Control < CanvasItem < Node < Object

A control that provides a horizontal bar with tabs.

## Description

A control that provides a horizontal bar with tabs. Similar to TabContainer
but is only in charge of drawing tabs, not interacting with children.

## Properties

bool | clip_tabs | `true`  
---|---|---  
int | current_tab | `-1`  
bool | deselect_enabled | `false`  
bool | drag_to_rearrange_enabled | `false`  
FocusMode | focus_mode | `2` (overrides Control)  
int | max_tab_width | `0`  
bool | scroll_to_selected | `true`  
bool | scrolling_enabled | `true`  
bool | select_with_rmb | `false`  
AlignmentMode | tab_alignment | `0`  
CloseButtonDisplayPolicy | tab_close_display_policy | `0`  
int | tab_count | `0`  
int | tabs_rearrange_group | `-1`  
  
## Methods

void | add_tab(title: String = "", icon: Texture2D = null)  
---|---  
void | clear_tabs()  
void | ensure_tab_visible(idx: int)  
bool | get_offset_buttons_visible() const  
int | get_previous_tab() const  
Texture2D | get_tab_button_icon(tab_idx: int) const  
Texture2D | get_tab_icon(tab_idx: int) const  
int | get_tab_icon_max_width(tab_idx: int) const  
int | get_tab_idx_at_point(point: Vector2) const  
String | get_tab_language(tab_idx: int) const  
Variant | get_tab_metadata(tab_idx: int) const  
int | get_tab_offset() const  
Rect2 | get_tab_rect(tab_idx: int) const  
TextDirection | get_tab_text_direction(tab_idx: int) const  
String | get_tab_title(tab_idx: int) const  
String | get_tab_tooltip(tab_idx: int) const  
bool | is_tab_disabled(tab_idx: int) const  
bool | is_tab_hidden(tab_idx: int) const  
void | move_tab(from: int, to: int)  
void | remove_tab(tab_idx: int)  
bool | select_next_available()  
bool | select_previous_available()  
void | set_tab_button_icon(tab_idx: int, icon: Texture2D)  
void | set_tab_disabled(tab_idx: int, disabled: bool)  
void | set_tab_hidden(tab_idx: int, hidden: bool)  
void | set_tab_icon(tab_idx: int, icon: Texture2D)  
void | set_tab_icon_max_width(tab_idx: int, width: int)  
void | set_tab_language(tab_idx: int, language: String)  
void | set_tab_metadata(tab_idx: int, metadata: Variant)  
void | set_tab_text_direction(tab_idx: int, direction: TextDirection)  
void | set_tab_title(tab_idx: int, title: String)  
void | set_tab_tooltip(tab_idx: int, tooltip: String)  
  
## Theme Properties

Color | drop_mark_color | `Color(1, 1, 1, 1)`  
---|---|---  
Color | font_disabled_color | `Color(0.875, 0.875, 0.875, 0.5)`  
Color | font_hovered_color | `Color(0.95, 0.95, 0.95, 1)`  
Color | font_outline_color | `Color(0, 0, 0, 1)`  
Color | font_selected_color | `Color(0.95, 0.95, 0.95, 1)`  
Color | font_unselected_color | `Color(0.7, 0.7, 0.7, 1)`  
int | h_separation | `4`  
int | icon_max_width | `0`  
int | outline_size | `0`  
Font | font  
int | font_size  
Texture2D | close  
Texture2D | decrement  
Texture2D | decrement_highlight  
Texture2D | drop_mark  
Texture2D | increment  
Texture2D | increment_highlight  
StyleBox | button_highlight  
StyleBox | button_pressed  
StyleBox | tab_disabled  
StyleBox | tab_focus  
StyleBox | tab_hovered  
StyleBox | tab_selected  
StyleBox | tab_unselected  
  
## Signals

active_tab_rearranged(idx_to: int)

Emitted when the active tab is rearranged via mouse drag. See
drag_to_rearrange_enabled.

tab_button_pressed(tab: int)

Emitted when a tab's right button is pressed. See set_tab_button_icon().

tab_changed(tab: int)

Emitted when switching to another tab.

tab_clicked(tab: int)

Emitted when a tab is clicked, even if it is the current tab.

tab_close_pressed(tab: int)

Emitted when a tab's close button is pressed.

Note: Tabs are not removed automatically once the close button is pressed,
this behavior needs to be programmed manually. For example:

GDScriptC#

    
    
    $TabBar.tab_close_pressed.connect($TabBar.remove_tab)
    
    
    
    GetNode<TabBar>("TabBar").TabClosePressed += GetNode<TabBar>("TabBar").RemoveTab;
    

tab_hovered(tab: int)

Emitted when a tab is hovered by the mouse.

tab_rmb_clicked(tab: int)

Emitted when a tab is right-clicked. select_with_rmb must be enabled.

tab_selected(tab: int)

Emitted when a tab is selected via click, directional input, or script, even
if it is the current tab.

## Enumerations

enum AlignmentMode:

AlignmentMode ALIGNMENT_LEFT = `0`

Places tabs to the left.

AlignmentMode ALIGNMENT_CENTER = `1`

Places tabs in the middle.

AlignmentMode ALIGNMENT_RIGHT = `2`

Places tabs to the right.

AlignmentMode ALIGNMENT_MAX = `3`

Represents the size of the AlignmentMode enum.

enum CloseButtonDisplayPolicy:

CloseButtonDisplayPolicy CLOSE_BUTTON_SHOW_NEVER = `0`

Never show the close buttons.

CloseButtonDisplayPolicy CLOSE_BUTTON_SHOW_ACTIVE_ONLY = `1`

Only show the close button on the currently active tab.

CloseButtonDisplayPolicy CLOSE_BUTTON_SHOW_ALWAYS = `2`

Show the close button on all tabs.

CloseButtonDisplayPolicy CLOSE_BUTTON_MAX = `3`

Represents the size of the CloseButtonDisplayPolicy enum.

## Property Descriptions

bool clip_tabs = `true`

  * void set_clip_tabs(value: bool)

  * bool get_clip_tabs()

If `true`, tabs overflowing this node's width will be hidden, displaying two
navigation buttons instead. Otherwise, this node's minimum size is updated so
that all tabs are visible.

int current_tab = `-1`

  * void set_current_tab(value: int)

  * int get_current_tab()

The index of the current selected tab. A value of `-1` means that no tab is
selected and can only be set when deselect_enabled is `true` or if all tabs
are hidden or disabled.

bool deselect_enabled = `false`

  * void set_deselect_enabled(value: bool)

  * bool get_deselect_enabled()

If `true`, all tabs can be deselected so that no tab is selected. Click on the
current tab to deselect it.

bool drag_to_rearrange_enabled = `false`

  * void set_drag_to_rearrange_enabled(value: bool)

  * bool get_drag_to_rearrange_enabled()

If `true`, tabs can be rearranged with mouse drag.

int max_tab_width = `0`

  * void set_max_tab_width(value: int)

  * int get_max_tab_width()

Sets the maximum width which all tabs should be limited to. Unlimited if set
to `0`.

bool scroll_to_selected = `true`

  * void set_scroll_to_selected(value: bool)

  * bool get_scroll_to_selected()

If `true`, the tab offset will be changed to keep the currently selected tab
visible.

bool scrolling_enabled = `true`

  * void set_scrolling_enabled(value: bool)

  * bool get_scrolling_enabled()

if `true`, the mouse's scroll wheel can be used to navigate the scroll view.

bool select_with_rmb = `false`

  * void set_select_with_rmb(value: bool)

  * bool get_select_with_rmb()

If `true`, enables selecting a tab with the right mouse button.

AlignmentMode tab_alignment = `0`

  * void set_tab_alignment(value: AlignmentMode)

  * AlignmentMode get_tab_alignment()

Sets the position at which tabs will be placed. See AlignmentMode for details.

CloseButtonDisplayPolicy tab_close_display_policy = `0`

  * void set_tab_close_display_policy(value: CloseButtonDisplayPolicy)

  * CloseButtonDisplayPolicy get_tab_close_display_policy()

Sets when the close button will appear on the tabs. See
CloseButtonDisplayPolicy for details.

int tab_count = `0`

  * void set_tab_count(value: int)

  * int get_tab_count()

The number of tabs currently in the bar.

int tabs_rearrange_group = `-1`

  * void set_tabs_rearrange_group(value: int)

  * int get_tabs_rearrange_group()

TabBars with the same rearrange group ID will allow dragging the tabs between
them. Enable drag with drag_to_rearrange_enabled.

Setting this to `-1` will disable rearranging between TabBars.

## Method Descriptions

void add_tab(title: String = "", icon: Texture2D = null)

Adds a new tab.

void clear_tabs()

Clears all tabs.

void ensure_tab_visible(idx: int)

Moves the scroll view to make the tab visible.

bool get_offset_buttons_visible() const

Returns `true` if the offset buttons (the ones that appear when there's not
enough space for all tabs) are visible.

int get_previous_tab() const

Returns the previously active tab index.

Texture2D get_tab_button_icon(tab_idx: int) const

Returns the icon for the right button of the tab at index `tab_idx` or `null`
if the right button has no icon.

Texture2D get_tab_icon(tab_idx: int) const

Returns the icon for the tab at index `tab_idx` or `null` if the tab has no
icon.

int get_tab_icon_max_width(tab_idx: int) const

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

int get_tab_idx_at_point(point: Vector2) const

Returns the index of the tab at local coordinates `point`. Returns `-1` if the
point is outside the control boundaries or if there's no tab at the queried
position.

String get_tab_language(tab_idx: int) const

Returns tab title language code.

Variant get_tab_metadata(tab_idx: int) const

Returns the metadata value set to the tab at index `tab_idx` using
set_tab_metadata(). If no metadata was previously set, returns `null` by
default.

int get_tab_offset() const

Returns the number of hidden tabs offsetted to the left.

Rect2 get_tab_rect(tab_idx: int) const

Returns tab Rect2 with local position and size.

TextDirection get_tab_text_direction(tab_idx: int) const

Returns tab title text base writing direction.

String get_tab_title(tab_idx: int) const

Returns the title of the tab at index `tab_idx`.

String get_tab_tooltip(tab_idx: int) const

Returns the tooltip text of the tab at index `tab_idx`.

bool is_tab_disabled(tab_idx: int) const

Returns `true` if the tab at index `tab_idx` is disabled.

bool is_tab_hidden(tab_idx: int) const

Returns `true` if the tab at index `tab_idx` is hidden.

void move_tab(from: int, to: int)

Moves a tab from `from` to `to`.

void remove_tab(tab_idx: int)

Removes the tab at index `tab_idx`.

bool select_next_available()

Selects the first available tab with greater index than the currently
selected. Returns `true` if tab selection changed.

bool select_previous_available()

Selects the first available tab with lower index than the currently selected.
Returns `true` if tab selection changed.

void set_tab_button_icon(tab_idx: int, icon: Texture2D)

Sets an `icon` for the button of the tab at index `tab_idx` (located to the
right, before the close button), making it visible and clickable (See
tab_button_pressed). Giving it a `null` value will hide the button.

void set_tab_disabled(tab_idx: int, disabled: bool)

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-
interactable.

void set_tab_hidden(tab_idx: int, hidden: bool)

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear
from the tab area.

void set_tab_icon(tab_idx: int, icon: Texture2D)

Sets an `icon` for the tab at index `tab_idx`.

void set_tab_icon_max_width(tab_idx: int, width: int)

Sets the maximum allowed width of the icon for the tab at index `tab_idx`.
This limit is applied on top of the default size of the icon and on top of
icon_max_width. The height is adjusted according to the icon's ratio.

void set_tab_language(tab_idx: int, language: String)

Sets language code of tab title used for line-breaking and text shaping
algorithms, if left empty current locale is used instead.

void set_tab_metadata(tab_idx: int, metadata: Variant)

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved
later using get_tab_metadata().

void set_tab_text_direction(tab_idx: int, direction: TextDirection)

Sets tab title base writing direction.

void set_tab_title(tab_idx: int, title: String)

Sets a `title` for the tab at index `tab_idx`.

void set_tab_tooltip(tab_idx: int, tooltip: String)

Sets a `tooltip` for tab at index `tab_idx`.

Note: By default, if the `tooltip` is empty and the tab text is truncated (not
all characters fit into the tab), the title will be displayed as a tooltip. To
hide the tooltip, assign `" "` as the `tooltip` text.

## Theme Property Descriptions

Color drop_mark_color = `Color(1, 1, 1, 1)`

Modulation color for the drop_mark icon.

Color font_disabled_color = `Color(0.875, 0.875, 0.875, 0.5)`

Font color of disabled tabs.

Color font_hovered_color = `Color(0.95, 0.95, 0.95, 1)`

Font color of the currently hovered tab. Does not apply to the selected tab.

Color font_outline_color = `Color(0, 0, 0, 1)`

The tint of text outline of the tab name.

Color font_selected_color = `Color(0.95, 0.95, 0.95, 1)`

Font color of the currently selected tab.

Color font_unselected_color = `Color(0.7, 0.7, 0.7, 1)`

Font color of the other, unselected tabs.

int h_separation = `4`

The horizontal separation between the elements inside tabs.

int icon_max_width = `0`

The maximum allowed width of the tab's icon. This limit is applied on top of
the default size of the icon, but before the value set with
set_tab_icon_max_width(). The height is adjusted according to the icon's
ratio.

int outline_size = `0`

The size of the tab text outline.

Note: If using a font with FontFile.multichannel_signed_distance_field
enabled, its FontFile.msdf_pixel_range must be set to at least twice the value
of outline_size for outline rendering to look correct. Otherwise, the outline
may appear to be cut off earlier than intended.

Font font

The font used to draw tab names.

int font_size

Font size of the tab names.

Texture2D close

The icon for the close button (see tab_close_display_policy).

Texture2D decrement

Icon for the left arrow button that appears when there are too many tabs to
fit in the container width. When the button is disabled (i.e. the first tab is
visible), it appears semi-transparent.

Texture2D decrement_highlight

Icon for the left arrow button that appears when there are too many tabs to
fit in the container width. Used when the button is being hovered with the
cursor.

Texture2D drop_mark

Icon shown to indicate where a dragged tab is gonna be dropped (see
drag_to_rearrange_enabled).

Texture2D increment

Icon for the right arrow button that appears when there are too many tabs to
fit in the container width. When the button is disabled (i.e. the last tab is
visible) it appears semi-transparent.

Texture2D increment_highlight

Icon for the right arrow button that appears when there are too many tabs to
fit in the container width. Used when the button is being hovered with the
cursor.

StyleBox button_highlight

Background of the tab and close buttons when they're being hovered with the
cursor.

StyleBox button_pressed

Background of the tab and close buttons when it's being pressed.

StyleBox tab_disabled

The style of disabled tabs.

StyleBox tab_focus

StyleBox used when the TabBar is focused. The tab_focus StyleBox is displayed
over the base StyleBox of the selected tab, so a partially transparent
StyleBox should be used to ensure the base StyleBox remains visible. A
StyleBox that represents an outline or an underline works well for this
purpose. To disable the focus visual effect, assign a StyleBoxEmpty resource.
Note that disabling the focus visual effect will harm keyboard/controller
navigation usability, so this is not recommended for accessibility reasons.

StyleBox tab_hovered

The style of the currently hovered tab. Does not apply to the selected tab.

Note: This style will be drawn with the same width as tab_unselected at
minimum.

StyleBox tab_selected

The style of the currently selected tab.

StyleBox tab_unselected

The style of the other, unselected tabs.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

