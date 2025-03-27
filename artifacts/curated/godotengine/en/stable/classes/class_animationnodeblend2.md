# AnimationNodeBlend2

Inherits: AnimationNodeSync < AnimationNode < Resource < RefCounted < Object

Blends two animations linearly inside of an AnimationNodeBlendTree.

## Description

A resource to add to an AnimationNodeBlendTree. Blends two animations linearly
based on the amount value.

In general, the blend value should be in the `[0.0, 1.0]` range. Values
outside of this range can blend amplified or inverted animations, however,
AnimationNodeAdd2 works better for this purpose.

## Tutorials

  * Using AnimationTree

  * 3D Platformer Demo

  * Third Person Shooter (TPS) Demo

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

