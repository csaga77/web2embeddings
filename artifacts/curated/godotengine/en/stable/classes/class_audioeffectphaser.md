# AudioEffectPhaser

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a phaser audio effect to an audio bus.

Combines the original signal with a copy that is slightly out of phase with
the original.

## Description

Combines phase-shifted signals with the original signal. The movement of the
phase-shifted signals is controlled using a low-frequency oscillator.

## Tutorials

  * Audio buses

## Properties

float | depth | `1.0`  
---|---|---  
float | feedback | `0.7`  
float | range_max_hz | `1600.0`  
float | range_min_hz | `440.0`  
float | rate_hz | `0.5`  
  
## Property Descriptions

float depth = `1.0`

  * void set_depth(value: float)

  * float get_depth()

Governs how high the filter frequencies sweep. Low value will primarily affect
bass frequencies. High value can sweep high into the treble. Value can range
from 0.1 to 4.

float feedback = `0.7`

  * void set_feedback(value: float)

  * float get_feedback()

Output percent of modified sound. Value can range from 0.1 to 0.9.

float range_max_hz = `1600.0`

  * void set_range_max_hz(value: float)

  * float get_range_max_hz()

Determines the maximum frequency affected by the LFO modulations, in Hz. Value
can range from 10 to 10000.

float range_min_hz = `440.0`

  * void set_range_min_hz(value: float)

  * float get_range_min_hz()

Determines the minimum frequency affected by the LFO modulations, in Hz. Value
can range from 10 to 10000.

float rate_hz = `0.5`

  * void set_rate_hz(value: float)

  * float get_rate_hz()

Adjusts the rate in Hz at which the effect sweeps up and down across the
frequency range.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

