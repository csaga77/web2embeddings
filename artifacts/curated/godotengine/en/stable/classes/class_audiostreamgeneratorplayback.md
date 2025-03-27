# AudioStreamGeneratorPlayback

Inherits: AudioStreamPlaybackResampled < AudioStreamPlayback < RefCounted <
Object

Plays back audio generated using AudioStreamGenerator.

## Description

This class is meant to be used with AudioStreamGenerator to play back the
generated audio in real-time.

## Tutorials

  * Audio Generator Demo

  * Godot 3.2 will get new audio features

## Methods

bool | can_push_buffer(amount: int) const  
---|---  
void | clear_buffer()  
int | get_frames_available() const  
int | get_skips() const  
bool | push_buffer(frames: PackedVector2Array)  
bool | push_frame(frame: Vector2)  
  
## Method Descriptions

bool can_push_buffer(amount: int) const

Returns `true` if a buffer of the size `amount` can be pushed to the audio
sample data buffer without overflowing it, `false` otherwise.

void clear_buffer()

Clears the audio sample data buffer.

int get_frames_available() const

Returns the number of frames that can be pushed to the audio sample data
buffer without overflowing it. If the result is `0`, the buffer is full.

int get_skips() const

Returns the number of times the playback skipped due to a buffer underrun in
the audio sample data. This value is reset at the start of the playback.

bool push_buffer(frames: PackedVector2Array)

Pushes several audio data frames to the buffer. This is usually more efficient
than push_frame() in C# and compiled languages via GDExtension, but
push_buffer() may be less efficient in GDScript.

bool push_frame(frame: Vector2)

Pushes a single audio data frame to the buffer. This is usually less efficient
than push_buffer() in C# and compiled languages via GDExtension, but
push_frame() may be more efficient in GDScript.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

