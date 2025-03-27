# InputEventGesture

Inherits: InputEventWithModifiers < InputEventFromWindow < InputEvent <
Resource < RefCounted < Object

Inherited By: InputEventMagnifyGesture, InputEventPanGesture

Abstract base class for touch gestures.

## Description

InputEventGestures are sent when a user performs a supported gesture on a
touch screen. Gestures can't be emulated using mouse, because they typically
require multi-touch.

## Tutorials

  * Using InputEvent

## Properties

Vector2 | position | `Vector2(0, 0)`  
---|---|---  
  
## Property Descriptions

Vector2 position = `Vector2(0, 0)`

  * void set_position(value: Vector2)

  * Vector2 get_position()

The local gesture position relative to the Viewport. If used in
Control._gui_input(), the position is relative to the current Control that
received this gesture.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

