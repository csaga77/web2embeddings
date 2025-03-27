# AudioEffectLimiter

Deprecated: Use AudioEffectHardLimiter instead.

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a soft-clip limiter audio effect to an Audio bus.

## Description

A limiter is similar to a compressor, but it's less flexible and designed to
disallow sound going over a given dB threshold. Adding one in the Master bus
is always recommended to reduce the effects of clipping.

Soft clipping starts to reduce the peaks a little below the threshold level
and progressively increases its effect as the input level increases such that
the threshold is never exceeded.

## Tutorials

  * Audio buses

## Properties

float | ceiling_db | `-0.1`  
---|---|---  
float | soft_clip_db | `2.0`  
float | soft_clip_ratio | `10.0`  
float | threshold_db | `0.0`  
  
## Property Descriptions

float ceiling_db = `-0.1`

  * void set_ceiling_db(value: float)

  * float get_ceiling_db()

The waveform's maximum allowed value, in decibels. Value can range from -20 to
-0.1.

float soft_clip_db = `2.0`

  * void set_soft_clip_db(value: float)

  * float get_soft_clip_db()

Applies a gain to the limited waves, in decibels. Value can range from 0 to 6.

float soft_clip_ratio = `10.0`

  * void set_soft_clip_ratio(value: float)

  * float get_soft_clip_ratio()

There is currently no description for this property. Please help us by
contributing one!

float threshold_db = `0.0`

  * void set_threshold_db(value: float)

  * float get_threshold_db()

Threshold from which the limiter begins to be active, in decibels. Value can
range from -30 to 0.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

