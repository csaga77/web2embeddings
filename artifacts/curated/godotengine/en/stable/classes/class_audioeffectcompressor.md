# AudioEffectCompressor

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a compressor audio effect to an audio bus.

Reduces sounds that exceed a certain threshold level, smooths out the dynamics
and increases the overall volume.

## Description

Dynamic range compressor reduces the level of the sound when the amplitude
goes over a certain threshold in Decibels. One of the main uses of a
compressor is to increase the dynamic range by clipping as little as possible
(when sound goes over 0dB).

Compressor has many uses in the mix:

  * In the Master bus to compress the whole output (although an AudioEffectLimiter is probably better).

  * In voice channels to ensure they sound as balanced as possible.

  * Sidechained. This can reduce the sound level sidechained with another audio bus for threshold detection. This technique is common in video game mixing to the level of music and SFX while voices are being heard.

  * Accentuates transients by using a wider attack, making effects sound more punchy.

## Tutorials

  * Audio buses

## Properties

float | attack_us | `20.0`  
---|---|---  
float | gain | `0.0`  
float | mix | `1.0`  
float | ratio | `4.0`  
float | release_ms | `250.0`  
StringName | sidechain | `&""`  
float | threshold | `0.0`  
  
## Property Descriptions

float attack_us = `20.0`

  * void set_attack_us(value: float)

  * float get_attack_us()

Compressor's reaction time when the signal exceeds the threshold, in
microseconds. Value can range from 20 to 2000.

float gain = `0.0`

  * void set_gain(value: float)

  * float get_gain()

Gain applied to the output signal.

float mix = `1.0`

  * void set_mix(value: float)

  * float get_mix()

Balance between original signal and effect signal. Value can range from 0
(totally dry) to 1 (totally wet).

float ratio = `4.0`

  * void set_ratio(value: float)

  * float get_ratio()

Amount of compression applied to the audio once it passes the threshold level.
The higher the ratio, the more the loud parts of the audio will be compressed.
Value can range from 1 to 48.

float release_ms = `250.0`

  * void set_release_ms(value: float)

  * float get_release_ms()

Compressor's delay time to stop reducing the signal after the signal level
falls below the threshold, in milliseconds. Value can range from 20 to 2000.

StringName sidechain = `&""`

  * void set_sidechain(value: StringName)

  * StringName get_sidechain()

Reduce the sound level using another audio bus for threshold detection.

float threshold = `0.0`

  * void set_threshold(value: float)

  * float get_threshold()

The level above which compression is applied to the audio. Value can range
from -60 to 0.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

