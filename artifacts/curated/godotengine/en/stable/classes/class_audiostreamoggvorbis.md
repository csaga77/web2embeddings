# AudioStreamOggVorbis

Inherits: AudioStream < Resource < RefCounted < Object

A class representing an Ogg Vorbis audio stream.

## Description

The AudioStreamOggVorbis class is a specialized AudioStream for handling Ogg
Vorbis file formats. It offers functionality for loading and playing back Ogg
Vorbis files, as well as managing looping and other playback properties. This
class is part of the audio stream system, which also supports WAV files
through the AudioStreamWAV class.

## Tutorials

  * Runtime file loading and saving

## Properties

int | bar_beats | `4`  
---|---|---  
int | beat_count | `0`  
float | bpm | `0.0`  
bool | loop | `false`  
float | loop_offset | `0.0`  
OggPacketSequence | packet_sequence  
  
## Methods

AudioStreamOggVorbis | load_from_buffer(stream_data: PackedByteArray) static  
---|---  
AudioStreamOggVorbis | load_from_file(path: String) static  
  
## Property Descriptions

int bar_beats = `4`

  * void set_bar_beats(value: int)

  * int get_bar_beats()

There is currently no description for this property. Please help us by
contributing one!

int beat_count = `0`

  * void set_beat_count(value: int)

  * int get_beat_count()

There is currently no description for this property. Please help us by
contributing one!

float bpm = `0.0`

  * void set_bpm(value: float)

  * float get_bpm()

There is currently no description for this property. Please help us by
contributing one!

bool loop = `false`

  * void set_loop(value: bool)

  * bool has_loop()

If `true`, the audio will play again from the specified loop_offset once it is
done playing. Useful for ambient sounds and background music.

float loop_offset = `0.0`

  * void set_loop_offset(value: float)

  * float get_loop_offset()

Time in seconds at which the stream starts after being looped.

OggPacketSequence packet_sequence

  * void set_packet_sequence(value: OggPacketSequence)

  * OggPacketSequence get_packet_sequence()

Contains the raw Ogg data for this stream.

## Method Descriptions

AudioStreamOggVorbis load_from_buffer(stream_data: PackedByteArray) static

Creates a new AudioStreamOggVorbis instance from the given buffer. The buffer
must contain Ogg Vorbis data.

AudioStreamOggVorbis load_from_file(path: String) static

Creates a new AudioStreamOggVorbis instance from the given file path. The file
must be in Ogg Vorbis format.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.
  *[void]: No return value.

