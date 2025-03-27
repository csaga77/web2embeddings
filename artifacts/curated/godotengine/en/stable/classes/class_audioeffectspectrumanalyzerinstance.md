# AudioEffectSpectrumAnalyzerInstance

Inherits: AudioEffectInstance < RefCounted < Object

Queryable instance of an AudioEffectSpectrumAnalyzer.

## Description

The runtime part of an AudioEffectSpectrumAnalyzer, which can be used to query
the magnitude of a frequency range on its host bus.

An instance of this class can be obtained with
AudioServer.get_bus_effect_instance().

## Tutorials

  * Audio Spectrum Visualizer Demo

## Methods

Vector2 | get_magnitude_for_frequency_range(from_hz: float, to_hz: float, mode: MagnitudeMode = 1) const  
---|---  
  
## Enumerations

enum MagnitudeMode:

MagnitudeMode MAGNITUDE_AVERAGE = `0`

Use the average value across the frequency range as magnitude.

MagnitudeMode MAGNITUDE_MAX = `1`

Use the maximum value of the frequency range as magnitude.

## Method Descriptions

Vector2 get_magnitude_for_frequency_range(from_hz: float, to_hz: float, mode:
MagnitudeMode = 1) const

Returns the magnitude of the frequencies from `from_hz` to `to_hz` in linear
energy as a Vector2. The `x` component of the return value represents the left
stereo channel, and `y` represents the right channel.

`mode` determines how the frequency range will be processed. See
MagnitudeMode.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

