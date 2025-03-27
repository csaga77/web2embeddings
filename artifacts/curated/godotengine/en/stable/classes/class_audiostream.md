# AudioStream

Inherits: Resource < RefCounted < Object

Inherited By: AudioStreamGenerator, AudioStreamInteractive,
AudioStreamMicrophone, AudioStreamMP3, AudioStreamOggVorbis,
AudioStreamPlaylist, AudioStreamPolyphonic, AudioStreamRandomizer,
AudioStreamSynchronized, AudioStreamWAV

Base class for audio streams.

## Description

Base class for audio streams. Audio streams are used for sound effects and
music playback, and support WAV (via AudioStreamWAV) and Ogg (via
AudioStreamOggVorbis) file formats.

## Tutorials

  * Audio streams

  * Audio Generator Demo

  * Audio Microphone Record Demo

  * Audio Spectrum Visualizer Demo

## Methods

int | _get_bar_beats() virtual const  
---|---  
int | _get_beat_count() virtual const  
float | _get_bpm() virtual const  
float | _get_length() virtual const  
Array[Dictionary] | _get_parameter_list() virtual const  
String | _get_stream_name() virtual const  
bool | _has_loop() virtual const  
AudioStreamPlayback | _instantiate_playback() virtual const  
bool | _is_monophonic() virtual const  
bool | can_be_sampled() const  
AudioSample | generate_sample() const  
float | get_length() const  
AudioStreamPlayback | instantiate_playback()  
bool | is_meta_stream() const  
bool | is_monophonic() const  
  
## Signals

parameter_list_changed()

Signal to be emitted to notify when the parameter list changed.

## Method Descriptions

int _get_bar_beats() virtual const

Override this method to return the bar beats of this stream.

int _get_beat_count() virtual const

Overridable method. Should return the total number of beats of this audio
stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate
(AudioStreamWAV.mix_rate, for example).

float _get_bpm() virtual const

Overridable method. Should return the tempo of this audio stream, in beats per
minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate
(AudioStreamWAV.mix_rate, for example).

float _get_length() virtual const

Override this method to customize the returned value of get_length(). Should
return the length of this audio stream, in seconds.

Array[Dictionary] _get_parameter_list() virtual const

Return the controllable parameters of this stream. This array contains
dictionaries with a property info description format (see
Object.get_property_list()). Additionally, the default value for this
parameter must be added tho each dictionary in "default_value" field.

String _get_stream_name() virtual const

Override this method to customize the name assigned to this audio stream.
Unused by the engine.

bool _has_loop() virtual const

Override this method to return `true` if this stream has a loop.

AudioStreamPlayback _instantiate_playback() virtual const

Override this method to customize the returned value of
instantiate_playback(). Should return a new AudioStreamPlayback created when
the stream is played (such as by an AudioStreamPlayer).

bool _is_monophonic() virtual const

Override this method to customize the returned value of is_monophonic().
Should return `true` if this audio stream only supports one channel.

bool can_be_sampled() const

Experimental: This method may be changed or removed in future versions.

Returns if the current AudioStream can be used as a sample. Only static
streams can be sampled.

AudioSample generate_sample() const

Experimental: This method may be changed or removed in future versions.

Generates an AudioSample based on the current stream.

float get_length() const

Returns the length of the audio stream in seconds.

AudioStreamPlayback instantiate_playback()

Returns a newly created AudioStreamPlayback intended to play this audio
stream. Useful for when you want to extend _instantiate_playback() but call
instantiate_playback() from an internally held AudioStream subresource. An
example of this can be found in the source code for
`AudioStreamRandomPitch::instantiate_playback`.

bool is_meta_stream() const

Returns `true` if the stream is a collection of other streams, `false`
otherwise.

bool is_monophonic() const

Returns `true` if this audio stream only supports one channel (monophony), or
`false` if the audio stream supports two or more channels (polyphony).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

