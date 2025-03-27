# AudioEffectDistortion

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a distortion audio effect to an Audio bus.

Modifies the sound to make it distorted.

## Description

Different types are available: clip, tan, lo-fi (bit crushing), overdrive, or
waveshape.

By distorting the waveform the frequency content changes, which will often
make the sound "crunchy" or "abrasive". For games, it can simulate sound
coming from some saturated device or speaker very efficiently.

## Tutorials

  * Audio buses

## Properties

float | drive | `0.0`  
---|---|---  
float | keep_hf_hz | `16000.0`  
Mode | mode | `0`  
float | post_gain | `0.0`  
float | pre_gain | `0.0`  
  
## Enumerations

enum Mode:

Mode MODE_CLIP = `0`

Digital distortion effect which cuts off peaks at the top and bottom of the
waveform.

Mode MODE_ATAN = `1`

There is currently no description for this enum. Please help us by
contributing one!

Mode MODE_LOFI = `2`

Low-resolution digital distortion effect (bit depth reduction). You can use it
to emulate the sound of early digital audio devices.

Mode MODE_OVERDRIVE = `3`

Emulates the warm distortion produced by a field effect transistor, which is
commonly used in solid-state musical instrument amplifiers. The drive property
has no effect in this mode.

Mode MODE_WAVESHAPE = `4`

Waveshaper distortions are used mainly by electronic musicians to achieve an
extra-abrasive sound.

## Property Descriptions

float drive = `0.0`

  * void set_drive(value: float)

  * float get_drive()

Distortion power. Value can range from 0 to 1.

float keep_hf_hz = `16000.0`

  * void set_keep_hf_hz(value: float)

  * float get_keep_hf_hz()

High-pass filter, in Hz. Frequencies higher than this value will not be
affected by the distortion. Value can range from 1 to 20000.

Mode mode = `0`

  * void set_mode(value: Mode)

  * Mode get_mode()

Distortion type.

float post_gain = `0.0`

  * void set_post_gain(value: float)

  * float get_post_gain()

Increases or decreases the volume after the effect, in decibels. Value can
range from -80 to 24.

float pre_gain = `0.0`

  * void set_pre_gain(value: float)

  * float get_pre_gain()

Increases or decreases the volume before the effect, in decibels. Value can
range from -60 to 60.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

