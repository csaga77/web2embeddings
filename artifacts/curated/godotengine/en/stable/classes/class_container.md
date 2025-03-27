# Container

Inherits: Control < CanvasItem < Node < Object

Inherited By: AspectRatioContainer, BoxContainer, CenterContainer,
EditorProperty, FlowContainer, GraphElement, GridContainer, MarginContainer,
PanelContainer, ScrollContainer, SplitContainer, SubViewportContainer,
TabContainer

Base class for all GUI containers.

## Description

Base class for all GUI containers. A Container automatically arranges its
child controls in a certain way. This class can be inherited to make custom
container types.

## Tutorials

  * Using Containers

## Properties

MouseFilter | mouse_filter | `1` (overrides Control)  
---|---|---  
  
## Methods

PackedInt32Array | _get_allowed_size_flags_horizontal() virtual const  
---|---  
PackedInt32Array | _get_allowed_size_flags_vertical() virtual const  
void | fit_child_in_rect(child: Control, rect: Rect2)  
void | queue_sort()  
  
## Signals

pre_sort_children()

Emitted when children are going to be sorted.

sort_children()

Emitted when sorting the children is needed.

## Constants

NOTIFICATION_PRE_SORT_CHILDREN = `50`

Notification just before children are going to be sorted, in case there's
something to process beforehand.

NOTIFICATION_SORT_CHILDREN = `51`

Notification for when sorting the children, it must be obeyed immediately.

## Method Descriptions

PackedInt32Array _get_allowed_size_flags_horizontal() virtual const

Implement to return a list of allowed horizontal SizeFlags for child nodes.
This doesn't technically prevent the usages of any other size flags, if your
implementation requires that. This only limits the options available to the
user in the Inspector dock.

Note: Having no size flags is equal to having Control.SIZE_SHRINK_BEGIN. As
such, this value is always implicitly allowed.

PackedInt32Array _get_allowed_size_flags_vertical() virtual const

Implement to return a list of allowed vertical SizeFlags for child nodes. This
doesn't technically prevent the usages of any other size flags, if your
implementation requires that. This only limits the options available to the
user in the Inspector dock.

Note: Having no size flags is equal to having Control.SIZE_SHRINK_BEGIN. As
such, this value is always implicitly allowed.

void fit_child_in_rect(child: Control, rect: Rect2)

Fit a child control in a given rect. This is mainly a helper for creating
custom container classes.

void queue_sort()

Queue resort of the contained children. This is called automatically anyway,
but can be called upon request.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

