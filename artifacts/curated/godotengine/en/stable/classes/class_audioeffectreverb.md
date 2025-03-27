# AudioEffectReverb

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a reverberation audio effect to an Audio bus.

## Description

Simulates the sound of acoustic environments such as rooms, concert halls,
caverns, or an open spaces.

## Tutorials

  * Audio buses

  * Third Person Shooter (TPS) Demo

## Properties

float | damping | `0.5`  
---|---|---  
float | dry | `1.0`  
float | hipass | `0.0`  
float | predelay_feedback | `0.4`  
float | predelay_msec | `150.0`  
float | room_size | `0.8`  
float | spread | `1.0`  
float | wet | `0.5`  
  
## Property Descriptions

float damping = `0.5`

  * void set_damping(value: float)

  * float get_damping()

Defines how reflective the imaginary room's walls are. Value can range from 0
to 1.

float dry = `1.0`

  * void set_dry(value: float)

  * float get_dry()

Output percent of original sound. At 0, only modified sound is outputted.
Value can range from 0 to 1.

float hipass = `0.0`

  * void set_hpf(value: float)

  * float get_hpf()

High-pass filter passes signals with a frequency higher than a certain cutoff
frequency and attenuates signals with frequencies lower than the cutoff
frequency. Value can range from 0 to 1.

float predelay_feedback = `0.4`

  * void set_predelay_feedback(value: float)

  * float get_predelay_feedback()

Output percent of predelay. Value can range from 0 to 1.

float predelay_msec = `150.0`

  * void set_predelay_msec(value: float)

  * float get_predelay_msec()

Time between the original signal and the early reflections of the reverb
signal, in milliseconds.

float room_size = `0.8`

  * void set_room_size(value: float)

  * float get_room_size()

Dimensions of simulated room. Bigger means more echoes. Value can range from 0
to 1.

float spread = `1.0`

  * void set_spread(value: float)

  * float get_spread()

Widens or narrows the stereo image of the reverb tail. 1 means fully widens.
Value can range from 0 to 1.

float wet = `0.5`

  * void set_wet(value: float)

  * float get_wet()

Output percent of modified sound. At 0, only original sound is outputted.
Value can range from 0 to 1.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

