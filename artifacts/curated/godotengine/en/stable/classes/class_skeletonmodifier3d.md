# SkeletonModifier3D

Inherits: Node3D < Node < Object

Inherited By: LookAtModifier3D, PhysicalBoneSimulator3D, RetargetModifier3D,
SkeletonIK3D, SpringBoneSimulator3D, XRBodyModifier3D, XRHandModifier3D

A node that may modify Skeleton3D's bone.

## Description

SkeletonModifier3D retrieves a target Skeleton3D by having a Skeleton3D
parent.

If there is AnimationMixer, modification always performs after playback
process of the AnimationMixer.

This node should be used to implement custom IK solvers, constraints, or
skeleton physics.

## Tutorials

  * Design of the Skeleton Modifier 3D

## Properties

bool | active | `true`  
---|---|---  
float | influence | `1.0`  
  
## Methods

void | _process_modification() virtual  
---|---  
Skeleton3D | get_skeleton() const  
  
## Signals

modification_processed()

Notifies when the modification have been finished.

Note: If you want to get the modified bone pose by the modifier, you must use
Skeleton3D.get_bone_pose() or Skeleton3D.get_bone_global_pose() at the moment
this signal is fired.

## Enumerations

enum BoneAxis:

BoneAxis BONE_AXIS_PLUS_X = `0`

Enumerated value for the +X axis.

BoneAxis BONE_AXIS_MINUS_X = `1`

Enumerated value for the -X axis.

BoneAxis BONE_AXIS_PLUS_Y = `2`

Enumerated value for the +Y axis.

BoneAxis BONE_AXIS_MINUS_Y = `3`

Enumerated value for the -Y axis.

BoneAxis BONE_AXIS_PLUS_Z = `4`

Enumerated value for the +Z axis.

BoneAxis BONE_AXIS_MINUS_Z = `5`

Enumerated value for the -Z axis.

## Property Descriptions

bool active = `true`

  * void set_active(value: bool)

  * bool is_active()

If `true`, the SkeletonModifier3D will be processing.

float influence = `1.0`

  * void set_influence(value: float)

  * float get_influence()

Sets the influence of the modification.

Note: This value is used by Skeleton3D to blend, so the SkeletonModifier3D
should always apply only 100% of the result without interpolation.

## Method Descriptions

void _process_modification() virtual

Override this virtual method to implement a custom skeleton modifier. You
should do things like get the Skeleton3D's current pose and apply the pose
here.

_process_modification() must not apply influence to bone poses because the
Skeleton3D automatically applies influence to all bone poses set by the
modifier.

Skeleton3D get_skeleton() const

Get parent Skeleton3D node if found.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

