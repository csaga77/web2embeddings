# OpenXRBindingModifierEditor

Inherits: PanelContainer < Container < Control < CanvasItem < Node < Object

Binding modifier editor.

## Description

This is the default binding modifier editor used in the OpenXR action map.

## Properties

BitField[SizeFlags] | size_flags_horizontal | `3` (overrides Control)  
---|---|---  
  
## Methods

OpenXRBindingModifier | get_binding_modifier() const  
---|---  
void | setup(action_map: OpenXRActionMap, binding_modifier: OpenXRBindingModifier)  
  
## Signals

binding_modifier_removed(binding_modifier_editor: Object)

Signal emitted when the user presses the delete binding modifier button for
this modifier.

## Method Descriptions

OpenXRBindingModifier get_binding_modifier() const

Returns the OpenXRBindingModifier currently being edited.

void setup(action_map: OpenXRActionMap, binding_modifier:
OpenXRBindingModifier)

Setup this editor for the provided `action_map` and `binding_modifier`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[BitField]: This value is an integer composed as a bitmask of the following flags.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

