# VisibleOnScreenNotifier2D

Inherits: Node2D < CanvasItem < Node < Object

Inherited By: VisibleOnScreenEnabler2D

A rectangular region of 2D space that detects whether it is visible on screen.

## Description

VisibleOnScreenNotifier2D represents a rectangular region of 2D space. When
any part of this region becomes visible on screen or in a viewport, it will
emit a screen_entered signal, and likewise it will emit a screen_exited signal
when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on
screen, use VisibleOnScreenEnabler2D.

Note: VisibleOnScreenNotifier2D uses the render culling code to determine
whether it's visible on screen, so it won't function unless CanvasItem.visible
is set to `true`.

## Tutorials

  * 2D Dodge The Creeps Demo

## Properties

Rect2 | rect | `Rect2(-10, -10, 20, 20)`  
---|---|---  
  
## Methods

bool | is_on_screen() const  
---|---  
  
## Signals

screen_entered()

Emitted when the VisibleOnScreenNotifier2D enters the screen.

screen_exited()

Emitted when the VisibleOnScreenNotifier2D exits the screen.

## Property Descriptions

Rect2 rect = `Rect2(-10, -10, 20, 20)`

  * void set_rect(value: Rect2)

  * Rect2 get_rect()

The VisibleOnScreenNotifier2D's bounding rectangle.

## Method Descriptions

bool is_on_screen() const

If `true`, the bounding rectangle is on the screen.

Note: It takes one frame for the VisibleOnScreenNotifier2D's visibility to be
determined once added to the scene tree, so this method will always return
`false` right after it is instantiated, before the draw pass.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

