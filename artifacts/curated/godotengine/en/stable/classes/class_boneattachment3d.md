# BoneAttachment3D

Inherits: Node3D < Node < Object

node that dynamically copies or overrides the 3D transform of a bone in its
parent Skeleton3D.

## Description

This node selects a bone in a Skeleton3D and attaches to it. This means that
the BoneAttachment3D node will either dynamically copy or override the 3D
transform of the selected bone.

## Properties

int | bone_idx | `-1`  
---|---|---  
String | bone_name | `""`  
bool | override_pose | `false`  
  
## Methods

NodePath | get_external_skeleton() const  
---|---  
Skeleton3D | get_skeleton()  
bool | get_use_external_skeleton() const  
void | on_skeleton_update()  
void | set_external_skeleton(external_skeleton: NodePath)  
void | set_use_external_skeleton(use_external_skeleton: bool)  
  
## Property Descriptions

int bone_idx = `-1`

  * void set_bone_idx(value: int)

  * int get_bone_idx()

The index of the attached bone.

String bone_name = `""`

  * void set_bone_name(value: String)

  * String get_bone_name()

The name of the attached bone.

bool override_pose = `false`

  * void set_override_pose(value: bool)

  * bool get_override_pose()

Whether the BoneAttachment3D node will override the bone pose of the bone it
is attached to. When set to `true`, the BoneAttachment3D node can change the
pose of the bone. When set to `false`, the BoneAttachment3D will always be set
to the bone's transform.

Note: This override performs interruptively in the skeleton update process
using signals due to the old design. It may cause unintended behavior when
used at the same time with SkeletonModifier3D.

## Method Descriptions

NodePath get_external_skeleton() const

Returns the NodePath to the external Skeleton3D node, if one has been set.

Skeleton3D get_skeleton()

Get parent or external Skeleton3D node if found.

bool get_use_external_skeleton() const

Returns whether the BoneAttachment3D node is using an external Skeleton3D
rather than attempting to use its parent node as the Skeleton3D.

void on_skeleton_update()

A function that is called automatically when the Skeleton3D is updated. This
function is where the BoneAttachment3D node updates its position so it is
correctly bound when it is not set to override the bone pose.

void set_external_skeleton(external_skeleton: NodePath)

Sets the NodePath to the external skeleton that the BoneAttachment3D node
should use. See set_use_external_skeleton() to enable the external Skeleton3D
node.

void set_use_external_skeleton(use_external_skeleton: bool)

Sets whether the BoneAttachment3D node will use an external Skeleton3D node
rather than attempting to use its parent node as the Skeleton3D. When set to
`true`, the BoneAttachment3D node will use the external Skeleton3D node set in
set_external_skeleton().

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

