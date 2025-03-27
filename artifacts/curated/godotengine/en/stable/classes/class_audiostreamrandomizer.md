# AudioStreamRandomizer

Inherits: AudioStream < Resource < RefCounted < Object

Wraps a pool of audio streams with pitch and volume shifting.

## Description

Picks a random AudioStream from the pool, depending on the playback mode, and
applies random pitch shifting and volume shifting during playback.

## Properties

PlaybackMode | playback_mode | `0`  
---|---|---  
float | random_pitch | `1.0`  
float | random_volume_offset_db | `0.0`  
int | streams_count | `0`  
  
## Methods

void | add_stream(index: int, stream: AudioStream, weight: float = 1.0)  
---|---  
AudioStream | get_stream(index: int) const  
float | get_stream_probability_weight(index: int) const  
void | move_stream(index_from: int, index_to: int)  
void | remove_stream(index: int)  
void | set_stream(index: int, stream: AudioStream)  
void | set_stream_probability_weight(index: int, weight: float)  
  
## Enumerations

enum PlaybackMode:

PlaybackMode PLAYBACK_RANDOM_NO_REPEATS = `0`

Pick a stream at random according to the probability weights chosen for each
stream, but avoid playing the same stream twice in a row whenever possible. If
only 1 sound is present in the pool, the same sound will always play,
effectively allowing repeats to occur.

PlaybackMode PLAYBACK_RANDOM = `1`

Pick a stream at random according to the probability weights chosen for each
stream. If only 1 sound is present in the pool, the same sound will always
play.

PlaybackMode PLAYBACK_SEQUENTIAL = `2`

Play streams in the order they appear in the stream pool. If only 1 sound is
present in the pool, the same sound will always play.

## Property Descriptions

PlaybackMode playback_mode = `0`

  * void set_playback_mode(value: PlaybackMode)

  * PlaybackMode get_playback_mode()

Controls how this AudioStreamRandomizer picks which AudioStream to play next.

float random_pitch = `1.0`

  * void set_random_pitch(value: float)

  * float get_random_pitch()

The intensity of random pitch variation. A value of 1 means no variation.

float random_volume_offset_db = `0.0`

  * void set_random_volume_offset_db(value: float)

  * float get_random_volume_offset_db()

The intensity of random volume variation. A value of 0 means no variation.

int streams_count = `0`

  * void set_streams_count(value: int)

  * int get_streams_count()

The number of streams in the stream pool.

## Method Descriptions

void add_stream(index: int, stream: AudioStream, weight: float = 1.0)

Insert a stream at the specified index. If the index is less than zero, the
insertion occurs at the end of the underlying pool.

AudioStream get_stream(index: int) const

Returns the stream at the specified index.

float get_stream_probability_weight(index: int) const

Returns the probability weight associated with the stream at the given index.

void move_stream(index_from: int, index_to: int)

Move a stream from one index to another.

void remove_stream(index: int)

Remove the stream at the specified index.

void set_stream(index: int, stream: AudioStream)

Set the AudioStream at the specified index.

void set_stream_probability_weight(index: int, weight: float)

Set the probability weight of the stream at the specified index. The higher
this value, the more likely that the randomizer will choose this stream during
random playback modes.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

