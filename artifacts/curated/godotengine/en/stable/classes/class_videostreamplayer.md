# VideoStreamPlayer

Inherits: Control < CanvasItem < Node < Object

A control used for video playback.

## Description

A control used for playback of VideoStream resources.

Supported video formats are Ogg Theora (`.ogv`, VideoStreamTheora) and any
format exposed via a GDExtension plugin.

Warning: On Web, video playback will perform poorly due to missing
architecture-specific assembly optimizations.

## Tutorials

  * Playing videos

## Properties

int | audio_track | `0`  
---|---|---  
bool | autoplay | `false`  
int | buffering_msec | `500`  
StringName | bus | `&"Master"`  
bool | expand | `false`  
bool | loop | `false`  
bool | paused | `false`  
VideoStream | stream  
float | stream_position  
float | volume  
float | volume_db | `0.0`  
  
## Methods

float | get_stream_length() const  
---|---  
String | get_stream_name() const  
Texture2D | get_video_texture() const  
bool | is_playing() const  
void | play()  
void | stop()  
  
## Signals

finished()

Emitted when playback is finished.

## Property Descriptions

int audio_track = `0`

  * void set_audio_track(value: int)

  * int get_audio_track()

The embedded audio track to play.

bool autoplay = `false`

  * void set_autoplay(value: bool)

  * bool has_autoplay()

If `true`, playback starts when the scene loads.

int buffering_msec = `500`

  * void set_buffering_msec(value: int)

  * int get_buffering_msec()

Amount of time in milliseconds to store in buffer while playing.

StringName bus = `&"Master"`

  * void set_bus(value: StringName)

  * StringName get_bus()

Audio bus to use for sound playback.

bool expand = `false`

  * void set_expand(value: bool)

  * bool has_expand()

If `true`, the video scales to the control size. Otherwise, the control
minimum size will be automatically adjusted to match the video stream's
dimensions.

bool loop = `false`

  * void set_loop(value: bool)

  * bool has_loop()

If `true`, the video restarts when it reaches its end.

bool paused = `false`

  * void set_paused(value: bool)

  * bool is_paused()

If `true`, the video is paused.

VideoStream stream

  * void set_stream(value: VideoStream)

  * VideoStream get_stream()

The assigned video stream. See description for supported formats.

float stream_position

  * void set_stream_position(value: float)

  * float get_stream_position()

The current position of the stream, in seconds.

Note: Changing this value won't have any effect as seeking is not implemented
yet, except in video formats implemented by a GDExtension add-on.

float volume

  * void set_volume(value: float)

  * float get_volume()

Audio volume as a linear value.

float volume_db = `0.0`

  * void set_volume_db(value: float)

  * float get_volume_db()

Audio volume in dB.

## Method Descriptions

float get_stream_length() const

The length of the current stream, in seconds.

Note: For VideoStreamTheora streams (the built-in format supported by Godot),
this value will always be zero, as getting the stream length is not
implemented yet. The feature may be supported by video formats implemented by
a GDExtension add-on.

String get_stream_name() const

Returns the video stream's name, or `"<No Stream>"` if no video stream is
assigned.

Texture2D get_video_texture() const

Returns the current frame as a Texture2D.

bool is_playing() const

Returns `true` if the video is playing.

Note: The video is still considered playing if paused during playback.

void play()

Starts the video playback from the beginning. If the video is paused, this
will not unpause the video.

void stop()

Stops the video playback and sets the stream position to 0.

Note: Although the stream position will be set to 0, the first frame of the
video stream won't become the current frame.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

