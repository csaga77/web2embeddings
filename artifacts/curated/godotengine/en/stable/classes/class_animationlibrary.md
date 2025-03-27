# AnimationLibrary

Inherits: Resource < RefCounted < Object

Container for Animation resources.

## Description

An animation library stores a set of animations accessible through StringName
keys, for use with AnimationPlayer nodes.

## Tutorials

  * Animation tutorial index

## Methods

Error | add_animation(name: StringName, animation: Animation)  
---|---  
Animation | get_animation(name: StringName) const  
Array[StringName] | get_animation_list() const  
int | get_animation_list_size() const  
bool | has_animation(name: StringName) const  
void | remove_animation(name: StringName)  
void | rename_animation(name: StringName, newname: StringName)  
  
## Signals

animation_added(name: StringName)

Emitted when an Animation is added, under the key `name`.

animation_changed(name: StringName)

Emitted when there's a change in one of the animations, e.g. tracks are added,
moved or have changed paths. `name` is the key of the animation that was
changed.

See also Resource.changed, which this acts as a relay for.

animation_removed(name: StringName)

Emitted when an Animation stored with the key `name` is removed.

animation_renamed(name: StringName, to_name: StringName)

Emitted when the key for an Animation is changed, from `name` to `to_name`.

## Method Descriptions

Error add_animation(name: StringName, animation: Animation)

Adds the `animation` to the library, accessible by the key `name`.

Animation get_animation(name: StringName) const

Returns the Animation with the key `name`. If the animation does not exist,
`null` is returned and an error is logged.

Array[StringName] get_animation_list() const

Returns the keys for the Animations stored in the library.

int get_animation_list_size() const

Returns the key count for the Animations stored in the library.

bool has_animation(name: StringName) const

Returns `true` if the library stores an Animation with `name` as the key.

void remove_animation(name: StringName)

Removes the Animation with the key `name`.

void rename_animation(name: StringName, newname: StringName)

Changes the key of the Animation associated with the key `name` to `newname`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

