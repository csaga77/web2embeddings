# AudioStreamPlaybackInteractive

Inherits: AudioStreamPlayback < RefCounted < Object

Playback component of AudioStreamInteractive.

## Description

Playback component of AudioStreamInteractive. Contains functions to change the
currently played clip.

## Methods

int | get_current_clip_index() const  
---|---  
void | switch_to_clip(clip_index: int)  
void | switch_to_clip_by_name(clip_name: StringName)  
  
## Method Descriptions

int get_current_clip_index() const

Return the index of the currently playing clip. You can use this to get the
name of the currently playing clip with
AudioStreamInteractive.get_clip_name().

Example: Get the currently playing clip name from inside an AudioStreamPlayer
node.

GDScript

    
    
    var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())
    

void switch_to_clip(clip_index: int)

Switch to a clip (by index).

void switch_to_clip_by_name(clip_name: StringName)

Switch to a clip (by name).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

