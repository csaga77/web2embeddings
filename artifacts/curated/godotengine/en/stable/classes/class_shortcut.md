# Shortcut

Inherits: Resource < RefCounted < Object

A shortcut for binding input.

## Description

Shortcuts are commonly used for interacting with a Control element from an
InputEvent (also known as hotkeys).

One shortcut can contain multiple InputEvents, allowing the possibility of
triggering one action with multiple different inputs.

## Properties

Array | events | `[]`  
---|---|---  
  
## Methods

String | get_as_text() const  
---|---  
bool | has_valid_event() const  
bool | matches_event(event: InputEvent) const  
  
## Property Descriptions

Array events = `[]`

  * void set_events(value: Array)

  * Array get_events()

The shortcut's InputEvent array.

Generally the InputEvent used is an InputEventKey, though it can be any
InputEvent, including an InputEventAction.

## Method Descriptions

String get_as_text() const

Returns the shortcut's first valid InputEvent as a String.

bool has_valid_event() const

Returns whether events contains an InputEvent which is valid.

bool matches_event(event: InputEvent) const

Returns whether any InputEvent in events equals `event`. This uses
InputEvent.is_match() to compare events.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

