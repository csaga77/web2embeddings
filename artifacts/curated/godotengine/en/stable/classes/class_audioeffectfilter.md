# AudioEffectFilter

Inherits: AudioEffect < Resource < RefCounted < Object

Inherited By: AudioEffectBandLimitFilter, AudioEffectBandPassFilter,
AudioEffectHighPassFilter, AudioEffectHighShelfFilter,
AudioEffectLowPassFilter, AudioEffectLowShelfFilter, AudioEffectNotchFilter

Adds a filter to the audio bus.

## Description

Allows frequencies other than the cutoff_hz to pass.

## Tutorials

  * Audio buses

## Properties

float | cutoff_hz | `2000.0`  
---|---|---  
FilterDB | db | `0`  
float | gain | `1.0`  
float | resonance | `0.5`  
  
## Enumerations

enum FilterDB:

FilterDB FILTER_6DB = `0`

Cutting off at 6dB per octave.

FilterDB FILTER_12DB = `1`

Cutting off at 12dB per octave.

FilterDB FILTER_18DB = `2`

Cutting off at 18dB per octave.

FilterDB FILTER_24DB = `3`

Cutting off at 24dB per octave.

## Property Descriptions

float cutoff_hz = `2000.0`

  * void set_cutoff(value: float)

  * float get_cutoff()

Threshold frequency for the filter, in Hz.

FilterDB db = `0`

  * void set_db(value: FilterDB)

  * FilterDB get_db()

Steepness of the cutoff curve in dB per octave, also known as the order of the
filter. Higher orders have a more aggressive cutoff.

float gain = `1.0`

  * void set_gain(value: float)

  * float get_gain()

Gain amount of the frequencies after the filter.

float resonance = `0.5`

  * void set_resonance(value: float)

  * float get_resonance()

Amount of boost in the frequency range near the cutoff frequency.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

