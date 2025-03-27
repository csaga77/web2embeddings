# XRController3D

Inherits: XRNode3D < Node3D < Node < Object

A 3D node representing a spatially-tracked controller.

## Description

This is a helper 3D node that is linked to the tracking of controllers. It
also offers several handy passthroughs to the state of buttons and such on the
controllers.

Controllers are linked by their ID. You can create controller nodes before the
controllers are available. If your game always uses two controllers (one for
each hand), you can predefine the controllers with ID 1 and 2; they will
become active as soon as the controllers are identified. If you expect
additional controllers to be used, you should react to the signals and add
XRController3D nodes to your scene.

The position of the controller node is automatically updated by the XRServer.
This makes this node ideal to add child nodes to visualize the controller.

As many XR runtimes now use a configurable action map all inputs are named.

## Tutorials

  * XR documentation index

## Methods

float | get_float(name: StringName) const  
---|---  
Variant | get_input(name: StringName) const  
TrackerHand | get_tracker_hand() const  
Vector2 | get_vector2(name: StringName) const  
bool | is_button_pressed(name: StringName) const  
  
## Signals

button_pressed(name: String)

Emitted when a button on this controller is pressed.

button_released(name: String)

Emitted when a button on this controller is released.

input_float_changed(name: String, value: float)

Emitted when a trigger or similar input on this controller changes value.

input_vector2_changed(name: String, value: Vector2)

Emitted when a thumbstick or thumbpad on this controller is moved.

profile_changed(role: String)

Emitted when the interaction profile on this controller is changed.

## Method Descriptions

float get_float(name: StringName) const

Returns a numeric value for the input with the given `name`. This is used for
triggers and grip sensors.

Variant get_input(name: StringName) const

Returns a Variant for the input with the given `name`. This works for any
input type, the variant will be typed according to the actions configuration.

TrackerHand get_tracker_hand() const

Returns the hand holding this controller, if known. See TrackerHand.

Vector2 get_vector2(name: StringName) const

Returns a Vector2 for the input with the given `name`. This is used for
thumbsticks and thumbpads found on many controllers.

bool is_button_pressed(name: StringName) const

Returns `true` if the button with the given `name` is pressed.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

