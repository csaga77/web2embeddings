# NavigationObstacle2D

Experimental: This class may be changed or removed in future versions.

Inherits: Node2D < CanvasItem < Node < Object

2D obstacle used to affect navigation mesh baking or constrain velocities of
avoidance controlled agents.

## Description

An obstacle needs a navigation map and outline vertices defined to work
correctly. The outlines can not cross or overlap.

Obstacles can be included in the navigation mesh baking process when
affect_navigation_mesh is enabled. They do not add walkable geometry, instead
their role is to discard other source geometry inside the shape. This can be
used to prevent navigation mesh from appearing in unwanted places. If
carve_navigation_mesh is enabled the baked shape will not be affected by
offsets of the navigation mesh baking, e.g. the agent radius.

With avoidance_enabled the obstacle can constrain the avoidance velocities of
avoidance using agents. If the obstacle's vertices are wound in clockwise
order, avoidance agents will be pushed in by the obstacle, otherwise,
avoidance agents will be pushed out. Obstacles using vertices and avoidance
can warp to a new position but should not be moved every single frame as each
change requires a rebuild of the avoidance map.

## Tutorials

  * Using NavigationObstacles

## Properties

bool | affect_navigation_mesh | `false`  
---|---|---  
bool | avoidance_enabled | `true`  
int | avoidance_layers | `1`  
bool | carve_navigation_mesh | `false`  
float | radius | `0.0`  
Vector2 | velocity | `Vector2(0, 0)`  
PackedVector2Array | vertices | `PackedVector2Array()`  
  
## Methods

bool | get_avoidance_layer_value(layer_number: int) const  
---|---  
RID | get_navigation_map() const  
RID | get_rid() const  
void | set_avoidance_layer_value(layer_number: int, value: bool)  
void | set_navigation_map(navigation_map: RID)  
  
## Property Descriptions

bool affect_navigation_mesh = `false`

  * void set_affect_navigation_mesh(value: bool)

  * bool get_affect_navigation_mesh()

If enabled and parsed in a navigation mesh baking process the obstacle will
discard source geometry inside its vertices defined shape.

bool avoidance_enabled = `true`

  * void set_avoidance_enabled(value: bool)

  * bool get_avoidance_enabled()

If `true` the obstacle affects avoidance using agents.

int avoidance_layers = `1`

  * void set_avoidance_layers(value: int)

  * int get_avoidance_layers()

A bitfield determining the avoidance layers for this obstacle. Agents with a
matching bit on the their avoidance mask will avoid this obstacle.

bool carve_navigation_mesh = `false`

  * void set_carve_navigation_mesh(value: bool)

  * bool get_carve_navigation_mesh()

If enabled the obstacle vertices will carve into the baked navigation mesh
with the shape unaffected by additional offsets (e.g. agent radius).

It will still be affected by further postprocessing of the baking process,
like edge and polygon simplification.

Requires affect_navigation_mesh to be enabled.

float radius = `0.0`

  * void set_radius(value: float)

  * float get_radius()

Sets the avoidance radius for the obstacle.

Vector2 velocity = `Vector2(0, 0)`

  * void set_velocity(value: Vector2)

  * Vector2 get_velocity()

Sets the wanted velocity for the obstacle so other agent's can better predict
the obstacle if it is moved with a velocity regularly (every frame) instead of
warped to a new position. Does only affect avoidance for the obstacles radius.
Does nothing for the obstacles static vertices.

PackedVector2Array vertices = `PackedVector2Array()`

  * void set_vertices(value: PackedVector2Array)

  * PackedVector2Array get_vertices()

The outline vertices of the obstacle. If the vertices are winded in clockwise
order agents will be pushed in by the obstacle, else they will be pushed out.
Outlines can not be crossed or overlap. Should the vertices using obstacle be
warped to a new position agent's can not predict this movement and may get
trapped inside the obstacle.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedVector2Array for more details.

## Method Descriptions

bool get_avoidance_layer_value(layer_number: int) const

Returns whether or not the specified layer of the avoidance_layers bitmask is
enabled, given a `layer_number` between 1 and 32.

RID get_navigation_map() const

Returns the RID of the navigation map for this NavigationObstacle node. This
function returns always the map set on the NavigationObstacle node and not the
map of the abstract obstacle on the NavigationServer. If the obstacle map is
changed directly with the NavigationServer API the NavigationObstacle node
will not be aware of the map change. Use set_navigation_map() to change the
navigation map for the NavigationObstacle and also update the obstacle on the
NavigationServer.

RID get_rid() const

Returns the RID of this obstacle on the NavigationServer2D.

void set_avoidance_layer_value(layer_number: int, value: bool)

Based on `value`, enables or disables the specified layer in the
avoidance_layers bitmask, given a `layer_number` between 1 and 32.

void set_navigation_map(navigation_map: RID)

Sets the RID of the navigation map this NavigationObstacle node should use and
also updates the `obstacle` on the NavigationServer.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

