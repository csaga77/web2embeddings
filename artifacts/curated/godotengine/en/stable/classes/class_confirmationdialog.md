# ConfirmationDialog

Inherits: AcceptDialog < Window < Viewport < Node < Object

Inherited By: EditorCommandPalette, EditorFileDialog, FileDialog,
ScriptCreateDialog

A dialog used for confirmation of actions.

## Description

A dialog used for confirmation of actions. This window is similar to
AcceptDialog, but pressing its Cancel button can have a different outcome from
pressing the OK button. The order of the two buttons varies depending on the
host OS.

To get cancel action, you can use:

GDScriptC#

    
    
    get_cancel_button().pressed.connect(_on_canceled)
    
    
    
    GetCancelButton().Pressed += OnCanceled;
    

## Properties

String | cancel_button_text | `"Cancel"`  
---|---|---  
Vector2i | min_size | `Vector2i(200, 70)` (overrides Window)  
Vector2i | size | `Vector2i(200, 100)` (overrides Window)  
String | title | `"Please Confirm..."` (overrides Window)  
  
## Methods

Button | get_cancel_button()  
---|---  
  
## Property Descriptions

String cancel_button_text = `"Cancel"`

  * void set_cancel_button_text(value: String)

  * String get_cancel_button_text()

The text displayed by the cancel button (see get_cancel_button()).

## Method Descriptions

Button get_cancel_button()

Returns the cancel button.

Warning: This is a required internal node, removing and freeing it may cause a
crash. If you wish to hide it or any of its children, use their
CanvasItem.visible property.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

