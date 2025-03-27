# AudioEffectEQ

Inherits: AudioEffect < Resource < RefCounted < Object

Inherited By: AudioEffectEQ10, AudioEffectEQ21, AudioEffectEQ6

Base class for audio equalizers. Gives you control over frequencies.

Use it to create a custom equalizer if AudioEffectEQ6, AudioEffectEQ10 or
AudioEffectEQ21 don't fit your needs.

## Description

AudioEffectEQ gives you control over frequencies. Use it to compensate for
existing deficiencies in audio. AudioEffectEQs are useful on the Master bus to
completely master a mix and give it more character. They are also useful when
a game is run on a mobile device, to adjust the mix to that kind of speakers
(it can be added but disabled when headphones are plugged).

## Tutorials

  * Audio buses

## Methods

int | get_band_count() const  
---|---  
float | get_band_gain_db(band_idx: int) const  
void | set_band_gain_db(band_idx: int, volume_db: float)  
  
## Method Descriptions

int get_band_count() const

Returns the number of bands of the equalizer.

float get_band_gain_db(band_idx: int) const

Returns the band's gain at the specified index, in dB.

void set_band_gain_db(band_idx: int, volume_db: float)

Sets band's gain at the specified index, in dB.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

