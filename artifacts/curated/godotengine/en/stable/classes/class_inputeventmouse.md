# InputEventMouse

Inherits: InputEventWithModifiers < InputEventFromWindow < InputEvent <
Resource < RefCounted < Object

Inherited By: InputEventMouseButton, InputEventMouseMotion

Base input event type for mouse events.

## Description

Stores general information about mouse events.

## Tutorials

  * Using InputEvent

## Properties

BitField[MouseButtonMask] | button_mask | `0`  
---|---|---  
Vector2 | global_position | `Vector2(0, 0)`  
Vector2 | position | `Vector2(0, 0)`  
  
## Property Descriptions

BitField[MouseButtonMask] button_mask = `0`

  * void set_button_mask(value: BitField[MouseButtonMask])

  * BitField[MouseButtonMask] get_button_mask()

The mouse button mask identifier, one of or a bitwise combination of the
MouseButton button masks.

Vector2 global_position = `Vector2(0, 0)`

  * void set_global_position(value: Vector2)

  * Vector2 get_global_position()

When received in Node._input() or Node._unhandled_input(), returns the mouse's
position in the root Viewport using the coordinate system of the root
Viewport.

When received in Control._gui_input(), returns the mouse's position in the
CanvasLayer that the Control is in using the coordinate system of the
CanvasLayer.

Vector2 position = `Vector2(0, 0)`

  * void set_position(value: Vector2)

  * Vector2 get_position()

When received in Node._input() or Node._unhandled_input(), returns the mouse's
position in the Viewport this Node is in using the coordinate system of this
Viewport.

When received in Control._gui_input(), returns the mouse's position in the
Control using the local coordinate system of the Control.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[BitField]: This value is an integer composed as a bitmask of the following flags.
  *[void]: No return value.

