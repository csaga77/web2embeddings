# Tweener

Inherits: RefCounted < Object

Inherited By: CallbackTweener, IntervalTweener, MethodTweener,
PropertyTweener, SubtweenTweener

Abstract class for all Tweeners used by Tween.

## Description

Tweeners are objects that perform a specific animating task, e.g.
interpolating a property or calling a method at a given time. A Tweener can't
be created manually, you need to use a dedicated method from Tween.

## Signals

finished()

Emitted when the Tweener has just finished its job or became invalid (e.g. due
to a freed object).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

