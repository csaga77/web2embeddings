# XRCamera3D

Inherits: Camera3D < Node3D < Node < Object

A camera node with a few overrules for AR/VR applied, such as location
tracking.

## Description

This is a helper 3D node for our camera. Note that, if stereoscopic rendering
is applicable (VR-HMD), most of the camera properties are ignored, as the HMD
information overrides them. The only properties that can be trusted are the
near and far planes.

The position and orientation of this node is automatically updated by the XR
Server to represent the location of the HMD if such tracking is available and
can thus be used by game logic. Note that, in contrast to the XR Controller,
the render thread has access to the most up-to-date tracking data of the HMD
and the location of the XRCamera3D can lag a few milliseconds behind what is
used for rendering as a result.

## Tutorials

  * XR documentation index

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

