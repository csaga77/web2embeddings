# AudioListener2D

Inherits: Node2D < CanvasItem < Node < Object

Overrides the location sounds are heard from.

## Description

Once added to the scene tree and enabled using make_current(), this node will
override the location sounds are heard from. Only one AudioListener2D can be
current. Using make_current() will disable the previous AudioListener2D.

If there is no active AudioListener2D in the current Viewport, center of the
screen will be used as a hearing point for the audio. AudioListener2D needs to
be inside SceneTree to function.

## Methods

void | clear_current()  
---|---  
bool | is_current() const  
void | make_current()  
  
## Method Descriptions

void clear_current()

Disables the AudioListener2D. If it's not set as current, this method will
have no effect.

bool is_current() const

Returns `true` if this AudioListener2D is currently active.

void make_current()

Makes the AudioListener2D active, setting it as the hearing point for the
sounds. If there is already another active AudioListener2D, it will be
disabled.

This method will have no effect if the AudioListener2D is not added to
SceneTree.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

