# Performance

Inherits: Object

Exposes performance-related data.

## Description

This class provides access to a number of different monitors related to
performance, such as memory usage, draw calls, and FPS. These are the same as
the values displayed in the Monitor tab in the editor's Debugger panel. By
using the get_monitor() method of this class, you can access this data from
your code.

You can add custom monitors using the add_custom_monitor() method. Custom
monitors are available in Monitor tab in the editor's Debugger panel together
with built-in monitors.

Note: Some of the built-in monitors are only available in debug mode and will
always return `0` when used in a project exported in release mode.

Note: Some of the built-in monitors are not updated in real-time for
performance reasons, so there may be a delay of up to 1 second between
changes.

Note: Custom monitors do not support negative values. Negative values are
clamped to 0.

## Methods

void | add_custom_monitor(id: StringName, callable: Callable, arguments: Array = [])  
---|---  
Variant | get_custom_monitor(id: StringName)  
Array[StringName] | get_custom_monitor_names()  
float | get_monitor(monitor: Monitor) const  
int | get_monitor_modification_time()  
bool | has_custom_monitor(id: StringName)  
void | remove_custom_monitor(id: StringName)  
  
## Enumerations

enum Monitor:

Monitor TIME_FPS = `0`

The number of frames rendered in the last second. This metric is only updated
once per second, even if queried more often. Higher is better.

Monitor TIME_PROCESS = `1`

Time it took to complete one frame, in seconds. Lower is better.

Monitor TIME_PHYSICS_PROCESS = `2`

Time it took to complete one physics frame, in seconds. Lower is better.

Monitor TIME_NAVIGATION_PROCESS = `3`

Time it took to complete one navigation step, in seconds. This includes
navigation map updates as well as agent avoidance calculations. Lower is
better.

Monitor MEMORY_STATIC = `4`

Static memory currently used, in bytes. Not available in release builds. Lower
is better.

Monitor MEMORY_STATIC_MAX = `5`

Available static memory. Not available in release builds. Lower is better.

Monitor MEMORY_MESSAGE_BUFFER_MAX = `6`

Largest amount of memory the message queue buffer has used, in bytes. The
message queue is used for deferred functions calls and notifications. Lower is
better.

Monitor OBJECT_COUNT = `7`

Number of objects currently instantiated (including nodes). Lower is better.

Monitor OBJECT_RESOURCE_COUNT = `8`

Number of resources currently used. Lower is better.

Monitor OBJECT_NODE_COUNT = `9`

Number of nodes currently instantiated in the scene tree. This also includes
the root node. Lower is better.

Monitor OBJECT_ORPHAN_NODE_COUNT = `10`

Number of orphan nodes, i.e. nodes which are not parented to a node of the
scene tree. Lower is better.

Monitor RENDER_TOTAL_OBJECTS_IN_FRAME = `11`

The total number of objects in the last rendered frame. This metric doesn't
include culled objects (either via hiding nodes, frustum culling or occlusion
culling). Lower is better.

Monitor RENDER_TOTAL_PRIMITIVES_IN_FRAME = `12`

The total number of vertices or indices rendered in the last rendered frame.
This metric doesn't include primitives from culled objects (either via hiding
nodes, frustum culling or occlusion culling). Due to the depth prepass and
shadow passes, the number of primitives is always higher than the actual
number of vertices in the scene (typically double or triple the original
vertex count). Lower is better.

Monitor RENDER_TOTAL_DRAW_CALLS_IN_FRAME = `13`

The total number of draw calls performed in the last rendered frame. This
metric doesn't include culled objects (either via hiding nodes, frustum
culling or occlusion culling), since they do not result in draw calls. Lower
is better.

Monitor RENDER_VIDEO_MEM_USED = `14`

The amount of video memory used (texture and vertex memory combined, in
bytes). Since this metric also includes miscellaneous allocations, this value
is always greater than the sum of RENDER_TEXTURE_MEM_USED and
RENDER_BUFFER_MEM_USED. Lower is better.

Monitor RENDER_TEXTURE_MEM_USED = `15`

The amount of texture memory used (in bytes). Lower is better.

Monitor RENDER_BUFFER_MEM_USED = `16`

The amount of render buffer memory used (in bytes). Lower is better.

Monitor PHYSICS_2D_ACTIVE_OBJECTS = `17`

Number of active RigidBody2D nodes in the game. Lower is better.

Monitor PHYSICS_2D_COLLISION_PAIRS = `18`

Number of collision pairs in the 2D physics engine. Lower is better.

Monitor PHYSICS_2D_ISLAND_COUNT = `19`

Number of islands in the 2D physics engine. Lower is better.

Monitor PHYSICS_3D_ACTIVE_OBJECTS = `20`

Number of active RigidBody3D and VehicleBody3D nodes in the game. Lower is
better.

Monitor PHYSICS_3D_COLLISION_PAIRS = `21`

Number of collision pairs in the 3D physics engine. Lower is better.

Monitor PHYSICS_3D_ISLAND_COUNT = `22`

Number of islands in the 3D physics engine. Lower is better.

Monitor AUDIO_OUTPUT_LATENCY = `23`

Output latency of the AudioServer. Equivalent to calling
AudioServer.get_output_latency(), it is not recommended to call this every
frame.

Monitor NAVIGATION_ACTIVE_MAPS = `24`

Number of active navigation maps in the NavigationServer3D. This also includes
the two empty default navigation maps created by World2D and World3D.

Monitor NAVIGATION_REGION_COUNT = `25`

Number of active navigation regions in the NavigationServer3D.

Monitor NAVIGATION_AGENT_COUNT = `26`

Number of active navigation agents processing avoidance in the
NavigationServer3D.

Monitor NAVIGATION_LINK_COUNT = `27`

Number of active navigation links in the NavigationServer3D.

Monitor NAVIGATION_POLYGON_COUNT = `28`

Number of navigation mesh polygons in the NavigationServer3D.

Monitor NAVIGATION_EDGE_COUNT = `29`

Number of navigation mesh polygon edges in the NavigationServer3D.

Monitor NAVIGATION_EDGE_MERGE_COUNT = `30`

Number of navigation mesh polygon edges that were merged due to edge key
overlap in the NavigationServer3D.

Monitor NAVIGATION_EDGE_CONNECTION_COUNT = `31`

Number of polygon edges that are considered connected by edge proximity
NavigationServer3D.

Monitor NAVIGATION_EDGE_FREE_COUNT = `32`

Number of navigation mesh polygon edges that could not be merged in the
NavigationServer3D. The edges still may be connected by edge proximity or with
links.

Monitor NAVIGATION_OBSTACLE_COUNT = `33`

Number of active navigation obstacles in the NavigationServer3D.

Monitor PIPELINE_COMPILATIONS_CANVAS = `34`

Number of pipeline compilations that were triggered by the 2D canvas renderer.

Monitor PIPELINE_COMPILATIONS_MESH = `35`

Number of pipeline compilations that were triggered by loading meshes. These
compilations will show up as longer loading times the first time a user runs
the game and the pipeline is required.

Monitor PIPELINE_COMPILATIONS_SURFACE = `36`

Number of pipeline compilations that were triggered by building the surface
cache before rendering the scene. These compilations will show up as a stutter
when loading an scene the first time a user runs the game and the pipeline is
required.

Monitor PIPELINE_COMPILATIONS_DRAW = `37`

Number of pipeline compilations that were triggered while drawing the scene.
These compilations will show up as stutters during gameplay the first time a
user runs the game and the pipeline is required.

Monitor PIPELINE_COMPILATIONS_SPECIALIZATION = `38`

Number of pipeline compilations that were triggered to optimize the current
scene. These compilations are done in the background and should not cause any
stutters whatsoever.

Monitor MONITOR_MAX = `39`

Represents the size of the Monitor enum.

## Method Descriptions

void add_custom_monitor(id: StringName, callable: Callable, arguments: Array =
[])

Adds a custom monitor with the name `id`. You can specify the category of the
monitor using slash delimiters in `id` (for example: `"Game/NumberOfNPCs"`).
If there is more than one slash delimiter, then the default category is used.
The default category is `"Custom"`. Prints an error if given `id` is already
present.

GDScriptC#

    
    
    func _ready():
        var monitor_value = Callable(self, "get_monitor_value")
    
        # Adds monitor with name "MyName" to category "MyCategory".
        Performance.add_custom_monitor("MyCategory/MyMonitor", monitor_value)
    
        # Adds monitor with name "MyName" to category "Custom".
        # Note: "MyCategory/MyMonitor" and "MyMonitor" have same name but different IDs, so the code is valid.
        Performance.add_custom_monitor("MyMonitor", monitor_value)
    
        # Adds monitor with name "MyName" to category "Custom".
        # Note: "MyMonitor" and "Custom/MyMonitor" have same name and same category but different IDs, so the code is valid.
        Performance.add_custom_monitor("Custom/MyMonitor", monitor_value)
    
        # Adds monitor with name "MyCategoryOne/MyCategoryTwo/MyMonitor" to category "Custom".
        Performance.add_custom_monitor("MyCategoryOne/MyCategoryTwo/MyMonitor", monitor_value)
    
    func get_monitor_value():
        return randi() % 25
    
    
    
    public override void _Ready()
    {
        var monitorValue = new Callable(this, MethodName.GetMonitorValue);
    
        // Adds monitor with name "MyName" to category "MyCategory".
        Performance.AddCustomMonitor("MyCategory/MyMonitor", monitorValue);
        // Adds monitor with name "MyName" to category "Custom".
        // Note: "MyCategory/MyMonitor" and "MyMonitor" have same name but different ids so the code is valid.
        Performance.AddCustomMonitor("MyMonitor", monitorValue);
    
        // Adds monitor with name "MyName" to category "Custom".
        // Note: "MyMonitor" and "Custom/MyMonitor" have same name and same category but different ids so the code is valid.
        Performance.AddCustomMonitor("Custom/MyMonitor", monitorValue);
    
        // Adds monitor with name "MyCategoryOne/MyCategoryTwo/MyMonitor" to category "Custom".
        Performance.AddCustomMonitor("MyCategoryOne/MyCategoryTwo/MyMonitor", monitorValue);
    }
    
    public int GetMonitorValue()
    {
        return GD.Randi() % 25;
    }
    

The debugger calls the callable to get the value of custom monitor. The
callable must return a zero or positive integer or floating-point number.

Callables are called with arguments supplied in argument array.

Variant get_custom_monitor(id: StringName)

Returns the value of custom monitor with given `id`. The callable is called to
get the value of custom monitor. See also has_custom_monitor(). Prints an
error if the given `id` is absent.

Array[StringName] get_custom_monitor_names()

Returns the names of active custom monitors in an Array.

float get_monitor(monitor: Monitor) const

Returns the value of one of the available built-in monitors. You should
provide one of the Monitor constants as the argument, like this:

GDScriptC#

    
    
    print(Performance.get_monitor(Performance.TIME_FPS)) # Prints the FPS to the console.
    
    
    
    GD.Print(Performance.GetMonitor(Performance.Monitor.TimeFps)); // Prints the FPS to the console.
    

See get_custom_monitor() to query custom performance monitors' values.

int get_monitor_modification_time()

Returns the last tick in which custom monitor was added/removed (in
microseconds since the engine started). This is set to Time.get_ticks_usec()
when the monitor is updated.

bool has_custom_monitor(id: StringName)

Returns `true` if custom monitor with the given `id` is present, `false`
otherwise.

void remove_custom_monitor(id: StringName)

Removes the custom monitor with given `id`. Prints an error if the given `id`
is already absent.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

