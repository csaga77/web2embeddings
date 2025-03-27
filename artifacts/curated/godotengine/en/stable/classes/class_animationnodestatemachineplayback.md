# AnimationNodeStateMachinePlayback

Inherits: Resource < RefCounted < Object

Provides playback control for an AnimationNodeStateMachine.

## Description

Allows control of AnimationTree state machines created with
AnimationNodeStateMachine. Retrieve with
`$AnimationTree.get("parameters/playback")`.

GDScriptC#

    
    
    var state_machine = $AnimationTree.get("parameters/playback")
    state_machine.travel("some_state")
    
    
    
    var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
    stateMachine.Travel("some_state");
    

## Tutorials

  * Using AnimationTree

## Properties

bool | resource_local_to_scene | `true` (overrides Resource)  
---|---|---  
  
## Methods

float | get_current_length() const  
---|---  
StringName | get_current_node() const  
float | get_current_play_position() const  
StringName | get_fading_from_node() const  
Array[StringName] | get_travel_path() const  
bool | is_playing() const  
void | next()  
void | start(node: StringName, reset: bool = true)  
void | stop()  
void | travel(to_node: StringName, reset_on_teleport: bool = true)  
  
## Method Descriptions

float get_current_length() const

Returns the current state length.

Note: It is possible that any AnimationRootNode can be nodes as well as
animations. This means that there can be multiple animations within a single
state. Which animation length has priority depends on the nodes connected
inside it. Also, if a transition does not reset, the remaining length at that
point will be returned.

StringName get_current_node() const

Returns the currently playing animation state.

Note: When using a cross-fade, the current state changes to the next state
immediately after the cross-fade begins.

float get_current_play_position() const

Returns the playback position within the current animation state.

StringName get_fading_from_node() const

Returns the starting state of currently fading animation.

Array[StringName] get_travel_path() const

Returns the current travel path as computed internally by the A* algorithm.

bool is_playing() const

Returns `true` if an animation is playing.

void next()

If there is a next path by travel or auto advance, immediately transitions
from the current state to the next state.

void start(node: StringName, reset: bool = true)

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.

void stop()

Stops the currently playing animation.

void travel(to_node: StringName, reset_on_teleport: bool = true)

Transitions from the current state to another one, following the shortest
path.

If the path does not connect from the current state, the animation will play
after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the beginning
when the travel cause a teleportation.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

