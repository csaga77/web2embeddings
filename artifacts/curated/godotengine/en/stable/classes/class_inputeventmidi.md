# InputEventMIDI

Inherits: InputEvent < Resource < RefCounted < Object

Represents a MIDI message from a MIDI device, such as a musical keyboard.

## Description

InputEventMIDI stores information about messages from MIDI (Musical Instrument
Digital Interface) devices. These may include musical keyboards, synthesizers,
and drum machines.

MIDI messages can be received over a 5-pin MIDI connector or over USB. If your
device supports both be sure to check the settings in the device to see which
output it is using.

By default, Godot does not detect MIDI devices. You need to call
OS.open_midi_inputs(), first. You can check which devices are detected with
OS.get_connected_midi_inputs(), and close the connection with
OS.close_midi_inputs().

GDScriptC#

    
    
    func _ready():
        OS.open_midi_inputs()
        print(OS.get_connected_midi_inputs())
    
    func _input(input_event):
        if input_event is InputEventMIDI:
            _print_midi_info(input_event)
    
    func _print_midi_info(midi_event):
        print(midi_event)
        print("Channel ", midi_event.channel)
        print("Message ", midi_event.message)
        print("Pitch ", midi_event.pitch)
        print("Velocity ", midi_event.velocity)
        print("Instrument ", midi_event.instrument)
        print("Pressure ", midi_event.pressure)
        print("Controller number: ", midi_event.controller_number)
        print("Controller value: ", midi_event.controller_value)
    
    
    
    public override void _Ready()
    {
        OS.OpenMidiInputs();
        GD.Print(OS.GetConnectedMidiInputs());
    }
    
    public override void _Input(InputEvent inputEvent)
    {
        if (inputEvent is InputEventMidi midiEvent)
        {
            PrintMIDIInfo(midiEvent);
        }
    }
    
    private void PrintMIDIInfo(InputEventMidi midiEvent)
    {
        GD.Print(midiEvent);
        GD.Print($"Channel {midiEvent.Channel}");
        GD.Print($"Message {midiEvent.Message}");
        GD.Print($"Pitch {midiEvent.Pitch}");
        GD.Print($"Velocity {midiEvent.Velocity}");
        GD.Print($"Instrument {midiEvent.Instrument}");
        GD.Print($"Pressure {midiEvent.Pressure}");
        GD.Print($"Controller number: {midiEvent.ControllerNumber}");
        GD.Print($"Controller value: {midiEvent.ControllerValue}");
    }
    

Note: Godot does not support MIDI output, so there is no way to emit MIDI
messages from Godot. Only MIDI input is supported.

Note: On the Web platform, using MIDI input requires a browser permission to
be granted first. This permission request is performed when calling
OS.open_midi_inputs(). MIDI input will not work until the user accepts the
permission request.

## Tutorials

  * MIDI Message Status Byte List

  * Wikipedia General MIDI Instrument List

  * Wikipedia Piano Key Frequencies List

## Properties

int | channel | `0`  
---|---|---  
int | controller_number | `0`  
int | controller_value | `0`  
int | instrument | `0`  
MIDIMessage | message | `0`  
int | pitch | `0`  
int | pressure | `0`  
int | velocity | `0`  
  
## Property Descriptions

int channel = `0`

  * void set_channel(value: int)

  * int get_channel()

The MIDI channel of this message, ranging from `0` to `15`. MIDI channel `9`
is reserved for percussion instruments.

int controller_number = `0`

  * void set_controller_number(value: int)

  * int get_controller_number()

The unique number of the controller, if message is
@GlobalScope.MIDI_MESSAGE_CONTROL_CHANGE, otherwise this is `0`. This value
can be used to identify sliders for volume, balance, and panning, as well as
switches and pedals on the MIDI device. See the General MIDI specification for
a small list.

int controller_value = `0`

  * void set_controller_value(value: int)

  * int get_controller_value()

The value applied to the controller. If message is
@GlobalScope.MIDI_MESSAGE_CONTROL_CHANGE, this value ranges from `0` to `127`,
otherwise it is `0`. See also controller_value.

int instrument = `0`

  * void set_instrument(value: int)

  * int get_instrument()

The instrument (also called program or preset) used on this MIDI message. This
value ranges from `0` to `127`.

To see what each value means, refer to the General MIDI's instrument list.
Keep in mind that the list is off by 1 because it does not begin from 0. A
value of `0` corresponds to the acoustic grand piano.

MIDIMessage message = `0`

  * void set_message(value: MIDIMessage)

  * MIDIMessage get_message()

Represents the type of MIDI message (see the MIDIMessage enum).

For more information, see the MIDI message status byte list chart.

int pitch = `0`

  * void set_pitch(value: int)

  * int get_pitch()

The pitch index number of this MIDI message. This value ranges from `0` to
`127`.

On a piano, the middle C is `60`, followed by a C-sharp (`61`), then a D
(`62`), and so on. Each octave is split in offsets of 12. See the "MIDI note
number" column of the piano key frequency chart a full list.

int pressure = `0`

  * void set_pressure(value: int)

  * int get_pressure()

The strength of the key being pressed. This value ranges from `0` to `127`.

Note: For many devices, this value is always `0`. Other devices such as
musical keyboards may simulate pressure by changing the velocity, instead.

int velocity = `0`

  * void set_velocity(value: int)

  * int get_velocity()

The velocity of the MIDI message. This value ranges from `0` to `127`. For a
musical keyboard, this corresponds to how quickly the key was pressed, and is
rarely above `110` in practice.

Note: Some MIDI devices may send a @GlobalScope.MIDI_MESSAGE_NOTE_ON message
with `0` velocity and expect it to be treated the same as a
@GlobalScope.MIDI_MESSAGE_NOTE_OFF message. If necessary, this can be handled
with a few lines of code:

    
    
    func _input(event):
        if event is InputEventMIDI:
            if event.message == MIDI_MESSAGE_NOTE_ON and event.velocity > 0:
                print("Note pressed!")
    

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

