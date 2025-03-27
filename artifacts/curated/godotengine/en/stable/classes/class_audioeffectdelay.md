# AudioEffectDelay

Inherits: AudioEffect < Resource < RefCounted < Object

Adds a delay audio effect to an audio bus. Plays input signal back after a
period of time.

Two tap delay and feedback options.

## Description

Plays input signal back after a period of time. The delayed signal may be
played back multiple times to create the sound of a repeating, decaying echo.
Delay effects range from a subtle echo effect to a pronounced blending of
previous sounds with new sounds.

## Tutorials

  * Audio buses

## Properties

float | dry | `1.0`  
---|---|---  
bool | feedback_active | `false`  
float | feedback_delay_ms | `340.0`  
float | feedback_level_db | `-6.0`  
float | feedback_lowpass | `16000.0`  
bool | tap1_active | `true`  
float | tap1_delay_ms | `250.0`  
float | tap1_level_db | `-6.0`  
float | tap1_pan | `0.2`  
bool | tap2_active | `true`  
float | tap2_delay_ms | `500.0`  
float | tap2_level_db | `-12.0`  
float | tap2_pan | `-0.4`  
  
## Property Descriptions

float dry = `1.0`

  * void set_dry(value: float)

  * float get_dry()

Output percent of original sound. At 0, only delayed sounds are output. Value
can range from 0 to 1.

bool feedback_active = `false`

  * void set_feedback_active(value: bool)

  * bool is_feedback_active()

If `true`, feedback is enabled.

float feedback_delay_ms = `340.0`

  * void set_feedback_delay_ms(value: float)

  * float get_feedback_delay_ms()

Feedback delay time in milliseconds.

float feedback_level_db = `-6.0`

  * void set_feedback_level_db(value: float)

  * float get_feedback_level_db()

Sound level for feedback.

float feedback_lowpass = `16000.0`

  * void set_feedback_lowpass(value: float)

  * float get_feedback_lowpass()

Low-pass filter for feedback, in Hz. Frequencies below this value are filtered
out of the source signal.

bool tap1_active = `true`

  * void set_tap1_active(value: bool)

  * bool is_tap1_active()

If `true`, the first tap will be enabled.

float tap1_delay_ms = `250.0`

  * void set_tap1_delay_ms(value: float)

  * float get_tap1_delay_ms()

First tap delay time in milliseconds.

float tap1_level_db = `-6.0`

  * void set_tap1_level_db(value: float)

  * float get_tap1_level_db()

Sound level for the first tap.

float tap1_pan = `0.2`

  * void set_tap1_pan(value: float)

  * float get_tap1_pan()

Pan position for the first tap. Value can range from -1 (fully left) to 1
(fully right).

bool tap2_active = `true`

  * void set_tap2_active(value: bool)

  * bool is_tap2_active()

If `true`, the second tap will be enabled.

float tap2_delay_ms = `500.0`

  * void set_tap2_delay_ms(value: float)

  * float get_tap2_delay_ms()

Second tap delay time in milliseconds.

float tap2_level_db = `-12.0`

  * void set_tap2_level_db(value: float)

  * float get_tap2_level_db()

Sound level for the second tap.

float tap2_pan = `-0.4`

  * void set_tap2_pan(value: float)

  * float get_tap2_pan()

Pan position for the second tap. Value can range from -1 (fully left) to 1
(fully right).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

