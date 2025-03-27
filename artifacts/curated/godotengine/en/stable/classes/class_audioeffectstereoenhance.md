# AudioEffectStereoEnhance

Inherits: AudioEffect < Resource < RefCounted < Object

An audio effect that can be used to adjust the intensity of stereo panning.

## Description

An audio effect that can be used to adjust the intensity of stereo panning.

## Tutorials

  * Audio buses

## Properties

float | pan_pullout | `1.0`  
---|---|---  
float | surround | `0.0`  
float | time_pullout_ms | `0.0`  
  
## Property Descriptions

float pan_pullout = `1.0`

  * void set_pan_pullout(value: float)

  * float get_pan_pullout()

Amplifies the difference between stereo channels, increasing or decreasing
existing panning. A value of 0.0 will downmix stereo to mono. Does not affect
a mono signal.

float surround = `0.0`

  * void set_surround(value: float)

  * float get_surround()

Widens sound stage through phase shifting in conjunction with time_pullout_ms.
Just pans sound to the left channel if time_pullout_ms is 0.

float time_pullout_ms = `0.0`

  * void set_time_pullout(value: float)

  * float get_time_pullout()

Widens sound stage through phase shifting in conjunction with surround. Just
delays the right channel if surround is 0.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

