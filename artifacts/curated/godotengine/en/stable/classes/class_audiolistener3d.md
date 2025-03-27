# AudioListener3D

Inherits: Node3D < Node < Object

Overrides the location sounds are heard from.

## Description

Once added to the scene tree and enabled using make_current(), this node will
override the location sounds are heard from. This can be used to listen from a
location different from the Camera3D.

## Methods

void | clear_current()  
---|---  
Transform3D | get_listener_transform() const  
bool | is_current() const  
void | make_current()  
  
## Method Descriptions

void clear_current()

Disables the listener to use the current camera's listener instead.

Transform3D get_listener_transform() const

Returns the listener's global orthonormalized Transform3D.

bool is_current() const

Returns `true` if the listener was made current using make_current(), `false`
otherwise.

Note: There may be more than one AudioListener3D marked as "current" in the
scene tree, but only the one that was made current last will be used.

void make_current()

Enables the listener. This will override the current camera's listener.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

