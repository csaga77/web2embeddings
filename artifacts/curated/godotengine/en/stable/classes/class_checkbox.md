# CheckBox

Inherits: Button < BaseButton < Control < CanvasItem < Node < Object

A button that represents a binary choice.

## Description

CheckBox allows the user to choose one of only two possible options. It's
similar to CheckButton in functionality, but it has a different appearance. To
follow established UX patterns, it's recommended to use CheckBox when toggling
it has no immediate effect on something. For example, it could be used when
toggling it will only do something once a confirmation button is pressed.

See also BaseButton which contains common properties and methods associated
with this node.

When BaseButton.button_group specifies a ButtonGroup, CheckBox changes its
appearance to that of a radio button and uses the various `radio_*` theme
properties.

## Properties

HorizontalAlignment | alignment | `0` (overrides Button)  
---|---|---  
bool | toggle_mode | `true` (overrides BaseButton)  
  
## Theme Properties

int | check_v_offset | `0`  
---|---|---  
Texture2D | checked  
Texture2D | checked_disabled  
Texture2D | radio_checked  
Texture2D | radio_checked_disabled  
Texture2D | radio_unchecked  
Texture2D | radio_unchecked_disabled  
Texture2D | unchecked  
Texture2D | unchecked_disabled  
  
## Theme Property Descriptions

int check_v_offset = `0`

The vertical offset used when rendering the check icons (in pixels).

Texture2D checked

The check icon to display when the CheckBox is checked.

Texture2D checked_disabled

The check icon to display when the CheckBox is checked and is disabled.

Texture2D radio_checked

The check icon to display when the CheckBox is configured as a radio button
and is checked.

Texture2D radio_checked_disabled

The check icon to display when the CheckBox is configured as a radio button,
is disabled, and is unchecked.

Texture2D radio_unchecked

The check icon to display when the CheckBox is configured as a radio button
and is unchecked.

Texture2D radio_unchecked_disabled

The check icon to display when the CheckBox is configured as a radio button,
is disabled, and is unchecked.

Texture2D unchecked

The check icon to display when the CheckBox is unchecked.

Texture2D unchecked_disabled

The check icon to display when the CheckBox is unchecked and is disabled.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

