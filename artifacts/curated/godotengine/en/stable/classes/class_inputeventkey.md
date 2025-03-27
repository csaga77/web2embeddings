# InputEventKey

Inherits: InputEventWithModifiers < InputEventFromWindow < InputEvent <
Resource < RefCounted < Object

Represents a key on a keyboard being pressed or released.

## Description

An input event for keys on a keyboard. Supports key presses, key releases and
echo events. It can also be received in Node._unhandled_key_input().

Note: Events received from the keyboard usually have all properties set. Event
mappings should have only one of the keycode, physical_keycode or unicode set.

When events are compared, properties are checked in the following priority -
keycode, physical_keycode and unicode. Events with the first matching value
will be considered equal.

## Tutorials

  * Using InputEvent

## Properties

bool | echo | `false`  
---|---|---  
Key | key_label | `0`  
Key | keycode | `0`  
KeyLocation | location | `0`  
Key | physical_keycode | `0`  
bool | pressed | `false`  
int | unicode | `0`  
  
## Methods

String | as_text_key_label() const  
---|---  
String | as_text_keycode() const  
String | as_text_location() const  
String | as_text_physical_keycode() const  
Key | get_key_label_with_modifiers() const  
Key | get_keycode_with_modifiers() const  
Key | get_physical_keycode_with_modifiers() const  
  
## Property Descriptions

bool echo = `false`

  * void set_echo(value: bool)

  * bool is_echo()

If `true`, the key was already pressed before this event. An echo event is a
repeated key event sent when the user is holding down the key.

Note: The rate at which echo events are sent is typically around 20 events per
second (after holding down the key for roughly half a second). However, the
key repeat delay/speed can be changed by the user or disabled entirely in the
operating system settings. To ensure your project works correctly on all
configurations, do not assume the user has a specific key repeat configuration
in your project's behavior.

Key key_label = `0`

  * void set_key_label(value: Key)

  * Key get_key_label()

Represents the localized label printed on the key in the current keyboard
layout, which corresponds to one of the Key constants or any valid Unicode
character.

For keyboard layouts with a single label on the key, it is equivalent to
keycode.

To get a human-readable representation of the InputEventKey, use
`OS.get_keycode_string(event.key_label)` where `event` is the InputEventKey.

    
    
    +-----+ +-----+
    | Q   | | Q   | - "Q" - keycode
    |    | |   | - "" and "" - key_label
    +-----+ +-----+
    

Key keycode = `0`

  * void set_keycode(value: Key)

  * Key get_keycode()

Latin label printed on the key in the current keyboard layout, which
corresponds to one of the Key constants.

To get a human-readable representation of the InputEventKey, use
`OS.get_keycode_string(event.keycode)` where `event` is the InputEventKey.

    
    
    +-----+ +-----+
    | Q   | | Q   | - "Q" - keycode
    |    | |   | - "" and "" - key_label
    +-----+ +-----+
    

KeyLocation location = `0`

  * void set_location(value: KeyLocation)

  * KeyLocation get_location()

Represents the location of a key which has both left and right versions, such
as `Shift` or `Alt`.

Key physical_keycode = `0`

  * void set_physical_keycode(value: Key)

  * Key get_physical_keycode()

Represents the physical location of a key on the 101/102-key US QWERTY
keyboard, which corresponds to one of the Key constants.

To get a human-readable representation of the InputEventKey, use
OS.get_keycode_string() in combination with
DisplayServer.keyboard_get_keycode_from_physical():

GDScriptC#

    
    
    func _input(event):
        if event is InputEventKey:
            var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
            print(OS.get_keycode_string(keycode))
    
    
    
    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey inputEventKey)
        {
            var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
            GD.Print(OS.GetKeycodeString(keycode));
        }
    }
    

bool pressed = `false`

  * void set_pressed(value: bool)

  * bool is_pressed()

If `true`, the key's state is pressed. If `false`, the key's state is
released.

int unicode = `0`

  * void set_unicode(value: int)

  * int get_unicode()

The key Unicode character code (when relevant), shifted by modifier keys.
Unicode character codes for composite characters and complex scripts may not
be available unless IME input mode is active. See Window.set_ime_active() for
more information.

## Method Descriptions

String as_text_key_label() const

Returns a String representation of the event's key_label and modifiers.

String as_text_keycode() const

Returns a String representation of the event's keycode and modifiers.

String as_text_location() const

Returns a String representation of the event's location. This will be a blank
string if the event is not specific to a location.

String as_text_physical_keycode() const

Returns a String representation of the event's physical_keycode and modifiers.

Key get_key_label_with_modifiers() const

Returns the localized key label combined with modifier keys such as `Shift` or
`Alt`. See also InputEventWithModifiers.

To get a human-readable representation of the InputEventKey with modifiers,
use `OS.get_keycode_string(event.get_key_label_with_modifiers())` where
`event` is the InputEventKey.

Key get_keycode_with_modifiers() const

Returns the Latin keycode combined with modifier keys such as `Shift` or
`Alt`. See also InputEventWithModifiers.

To get a human-readable representation of the InputEventKey with modifiers,
use `OS.get_keycode_string(event.get_keycode_with_modifiers())` where `event`
is the InputEventKey.

Key get_physical_keycode_with_modifiers() const

Returns the physical keycode combined with modifier keys such as `Shift` or
`Alt`. See also InputEventWithModifiers.

To get a human-readable representation of the InputEventKey with modifiers,
use `OS.get_keycode_string(event.get_physical_keycode_with_modifiers())` where
`event` is the InputEventKey.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

