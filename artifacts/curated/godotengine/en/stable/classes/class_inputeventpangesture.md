# InputEventPanGesture

Inherits: InputEventGesture < InputEventWithModifiers < InputEventFromWindow <
InputEvent < Resource < RefCounted < Object

Represents a panning touch gesture.

## Description

Stores information about pan gestures. A pan gesture is performed when the
user swipes the touch screen with two fingers. It's typically used for
panning/scrolling.

Note: On Android, this requires the
ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures
project setting to be enabled.

## Tutorials

  * Using InputEvent

## Properties

Vector2 | delta | `Vector2(0, 0)`  
---|---|---  
  
## Property Descriptions

Vector2 delta = `Vector2(0, 0)`

  * void set_delta(value: Vector2)

  * Vector2 get_delta()

Panning amount since last pan event.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

