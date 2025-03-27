# AudioEffectChorus

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a chorus audio effect.

## Description

Adds a chorus audio effect. The effect applies a filter with voices to
duplicate the audio source and manipulate it through the filter.

## Tutorials

  * Audio buses

## Properties

float | dry | `1.0`  
---|---|---  
float | voice/1/cutoff_hz | `8000.0`  
float | voice/1/delay_ms | `15.0`  
float | voice/1/depth_ms | `2.0`  
float | voice/1/level_db | `0.0`  
float | voice/1/pan | `-0.5`  
float | voice/1/rate_hz | `0.8`  
float | voice/2/cutoff_hz | `8000.0`  
float | voice/2/delay_ms | `20.0`  
float | voice/2/depth_ms | `3.0`  
float | voice/2/level_db | `0.0`  
float | voice/2/pan | `0.5`  
float | voice/2/rate_hz | `1.2`  
float | voice/3/cutoff_hz  
float | voice/3/delay_ms  
float | voice/3/depth_ms  
float | voice/3/level_db  
float | voice/3/pan  
float | voice/3/rate_hz  
float | voice/4/cutoff_hz  
float | voice/4/delay_ms  
float | voice/4/depth_ms  
float | voice/4/level_db  
float | voice/4/pan  
float | voice/4/rate_hz  
int | voice_count | `2`  
float | wet | `0.5`  
  
## Methods

float | get_voice_cutoff_hz(voice_idx: int) const  
---|---  
float | get_voice_delay_ms(voice_idx: int) const  
float | get_voice_depth_ms(voice_idx: int) const  
float | get_voice_level_db(voice_idx: int) const  
float | get_voice_pan(voice_idx: int) const  
float | get_voice_rate_hz(voice_idx: int) const  
void | set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)  
void | set_voice_delay_ms(voice_idx: int, delay_ms: float)  
void | set_voice_depth_ms(voice_idx: int, depth_ms: float)  
void | set_voice_level_db(voice_idx: int, level_db: float)  
void | set_voice_pan(voice_idx: int, pan: float)  
void | set_voice_rate_hz(voice_idx: int, rate_hz: float)  
  
## Property Descriptions

float dry = `1.0`

  * void set_dry(value: float)

  * float get_dry()

The effect's raw signal.

float voice/1/cutoff_hz = `8000.0`

  * void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)

  * float get_voice_cutoff_hz(voice_idx: int) const

The voice's cutoff frequency.

float voice/1/delay_ms = `15.0`

  * void set_voice_delay_ms(voice_idx: int, delay_ms: float)

  * float get_voice_delay_ms(voice_idx: int) const

The voice's signal delay.

float voice/1/depth_ms = `2.0`

  * void set_voice_depth_ms(voice_idx: int, depth_ms: float)

  * float get_voice_depth_ms(voice_idx: int) const

The voice filter's depth.

float voice/1/level_db = `0.0`

  * void set_voice_level_db(voice_idx: int, level_db: float)

  * float get_voice_level_db(voice_idx: int) const

The voice's volume.

float voice/1/pan = `-0.5`

  * void set_voice_pan(voice_idx: int, pan: float)

  * float get_voice_pan(voice_idx: int) const

The voice's pan level.

float voice/1/rate_hz = `0.8`

  * void set_voice_rate_hz(voice_idx: int, rate_hz: float)

  * float get_voice_rate_hz(voice_idx: int) const

The voice's filter rate.

float voice/2/cutoff_hz = `8000.0`

  * void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)

  * float get_voice_cutoff_hz(voice_idx: int) const

The voice's cutoff frequency.

float voice/2/delay_ms = `20.0`

  * void set_voice_delay_ms(voice_idx: int, delay_ms: float)

  * float get_voice_delay_ms(voice_idx: int) const

The voice's signal delay.

float voice/2/depth_ms = `3.0`

  * void set_voice_depth_ms(voice_idx: int, depth_ms: float)

  * float get_voice_depth_ms(voice_idx: int) const

The voice filter's depth.

float voice/2/level_db = `0.0`

  * void set_voice_level_db(voice_idx: int, level_db: float)

  * float get_voice_level_db(voice_idx: int) const

The voice's volume.

float voice/2/pan = `0.5`

  * void set_voice_pan(voice_idx: int, pan: float)

  * float get_voice_pan(voice_idx: int) const

The voice's pan level.

float voice/2/rate_hz = `1.2`

  * void set_voice_rate_hz(voice_idx: int, rate_hz: float)

  * float get_voice_rate_hz(voice_idx: int) const

The voice's filter rate.

float voice/3/cutoff_hz

  * void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)

  * float get_voice_cutoff_hz(voice_idx: int) const

The voice's cutoff frequency.

float voice/3/delay_ms

  * void set_voice_delay_ms(voice_idx: int, delay_ms: float)

  * float get_voice_delay_ms(voice_idx: int) const

The voice's signal delay.

float voice/3/depth_ms

  * void set_voice_depth_ms(voice_idx: int, depth_ms: float)

  * float get_voice_depth_ms(voice_idx: int) const

The voice filter's depth.

float voice/3/level_db

  * void set_voice_level_db(voice_idx: int, level_db: float)

  * float get_voice_level_db(voice_idx: int) const

The voice's volume.

float voice/3/pan

  * void set_voice_pan(voice_idx: int, pan: float)

  * float get_voice_pan(voice_idx: int) const

The voice's pan level.

float voice/3/rate_hz

  * void set_voice_rate_hz(voice_idx: int, rate_hz: float)

  * float get_voice_rate_hz(voice_idx: int) const

The voice's filter rate.

float voice/4/cutoff_hz

  * void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)

  * float get_voice_cutoff_hz(voice_idx: int) const

The voice's cutoff frequency.

float voice/4/delay_ms

  * void set_voice_delay_ms(voice_idx: int, delay_ms: float)

  * float get_voice_delay_ms(voice_idx: int) const

The voice's signal delay.

float voice/4/depth_ms

  * void set_voice_depth_ms(voice_idx: int, depth_ms: float)

  * float get_voice_depth_ms(voice_idx: int) const

The voice filter's depth.

float voice/4/level_db

  * void set_voice_level_db(voice_idx: int, level_db: float)

  * float get_voice_level_db(voice_idx: int) const

The voice's volume.

float voice/4/pan

  * void set_voice_pan(voice_idx: int, pan: float)

  * float get_voice_pan(voice_idx: int) const

The voice's pan level.

float voice/4/rate_hz

  * void set_voice_rate_hz(voice_idx: int, rate_hz: float)

  * float get_voice_rate_hz(voice_idx: int) const

The voice's filter rate.

int voice_count = `2`

  * void set_voice_count(value: int)

  * int get_voice_count()

The number of voices in the effect.

float wet = `0.5`

  * void set_wet(value: float)

  * float get_wet()

The effect's processed signal.

## Method Descriptions

float get_voice_cutoff_hz(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

float get_voice_delay_ms(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

float get_voice_depth_ms(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

float get_voice_level_db(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

float get_voice_pan(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

float get_voice_rate_hz(voice_idx: int) const

There is currently no description for this method. Please help us by
contributing one!

void set_voice_cutoff_hz(voice_idx: int, cutoff_hz: float)

There is currently no description for this method. Please help us by
contributing one!

void set_voice_delay_ms(voice_idx: int, delay_ms: float)

There is currently no description for this method. Please help us by
contributing one!

void set_voice_depth_ms(voice_idx: int, depth_ms: float)

There is currently no description for this method. Please help us by
contributing one!

void set_voice_level_db(voice_idx: int, level_db: float)

There is currently no description for this method. Please help us by
contributing one!

void set_voice_pan(voice_idx: int, pan: float)

There is currently no description for this method. Please help us by
contributing one!

void set_voice_rate_hz(voice_idx: int, rate_hz: float)

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

