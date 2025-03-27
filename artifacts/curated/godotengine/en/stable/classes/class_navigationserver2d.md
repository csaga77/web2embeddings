# NavigationServer2D

Experimental: This class may be changed or removed in future versions.

Inherits: Object

A server interface for low-level 2D navigation access.

## Description

NavigationServer2D is the server that handles navigation maps, regions and
agents. It does not handle A* navigation from AStar2D or AStarGrid2D.

Maps are divided into regions, which are composed of navigation polygons.
Together, they define the traversable areas in the 2D world.

Note: Most NavigationServer2D changes take effect after the next physics frame
and not immediately. This includes all changes made to maps, regions or agents
by navigation-related nodes in the scene tree or made through scripts.

For two regions to be connected to each other, they must share a similar edge.
An edge is considered connected to another if both of its two vertices are at
a distance less than `edge_connection_margin` to the respective other edge's
vertex.

You may assign navigation layers to regions with
region_set_navigation_layers(), which then can be checked upon when requesting
a path with map_get_path(). This can be used to allow or deny certain areas
for some objects.

To use the collision avoidance system, you may use agents. You can set an
agent's target velocity, then the servers will emit a callback with a modified
velocity.

Note: The collision avoidance system ignores regions. Using the modified
velocity directly may move an agent outside of the traversable area. This is a
limitation of the collision avoidance system, any more complex situation may
require the use of the physics engine.

This server keeps tracks of any call and executes them during the sync phase.
This means that you can request any change to the map, using any thread,
without worrying.

## Tutorials

  * Using NavigationServer

  * Navigation Polygon 2D Demo

## Methods

RID | agent_create()  
---|---  
bool | agent_get_avoidance_enabled(agent: RID) const  
int | agent_get_avoidance_layers(agent: RID) const  
int | agent_get_avoidance_mask(agent: RID) const  
float | agent_get_avoidance_priority(agent: RID) const  
RID | agent_get_map(agent: RID) const  
int | agent_get_max_neighbors(agent: RID) const  
float | agent_get_max_speed(agent: RID) const  
float | agent_get_neighbor_distance(agent: RID) const  
bool | agent_get_paused(agent: RID) const  
Vector2 | agent_get_position(agent: RID) const  
float | agent_get_radius(agent: RID) const  
float | agent_get_time_horizon_agents(agent: RID) const  
float | agent_get_time_horizon_obstacles(agent: RID) const  
Vector2 | agent_get_velocity(agent: RID) const  
bool | agent_has_avoidance_callback(agent: RID) const  
bool | agent_is_map_changed(agent: RID) const  
void | agent_set_avoidance_callback(agent: RID, callback: Callable)  
void | agent_set_avoidance_enabled(agent: RID, enabled: bool)  
void | agent_set_avoidance_layers(agent: RID, layers: int)  
void | agent_set_avoidance_mask(agent: RID, mask: int)  
void | agent_set_avoidance_priority(agent: RID, priority: float)  
void | agent_set_map(agent: RID, map: RID)  
void | agent_set_max_neighbors(agent: RID, count: int)  
void | agent_set_max_speed(agent: RID, max_speed: float)  
void | agent_set_neighbor_distance(agent: RID, distance: float)  
void | agent_set_paused(agent: RID, paused: bool)  
void | agent_set_position(agent: RID, position: Vector2)  
void | agent_set_radius(agent: RID, radius: float)  
void | agent_set_time_horizon_agents(agent: RID, time_horizon: float)  
void | agent_set_time_horizon_obstacles(agent: RID, time_horizon: float)  
void | agent_set_velocity(agent: RID, velocity: Vector2)  
void | agent_set_velocity_forced(agent: RID, velocity: Vector2)  
void | bake_from_source_geometry_data(navigation_polygon: NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D, callback: Callable = Callable())  
void | bake_from_source_geometry_data_async(navigation_polygon: NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D, callback: Callable = Callable())  
void | free_rid(rid: RID)  
bool | get_debug_enabled() const  
Array[RID] | get_maps() const  
bool | is_baking_navigation_polygon(navigation_polygon: NavigationPolygon) const  
RID | link_create()  
bool | link_get_enabled(link: RID) const  
Vector2 | link_get_end_position(link: RID) const  
float | link_get_enter_cost(link: RID) const  
RID | link_get_map(link: RID) const  
int | link_get_navigation_layers(link: RID) const  
int | link_get_owner_id(link: RID) const  
Vector2 | link_get_start_position(link: RID) const  
float | link_get_travel_cost(link: RID) const  
bool | link_is_bidirectional(link: RID) const  
void | link_set_bidirectional(link: RID, bidirectional: bool)  
void | link_set_enabled(link: RID, enabled: bool)  
void | link_set_end_position(link: RID, position: Vector2)  
void | link_set_enter_cost(link: RID, enter_cost: float)  
void | link_set_map(link: RID, map: RID)  
void | link_set_navigation_layers(link: RID, navigation_layers: int)  
void | link_set_owner_id(link: RID, owner_id: int)  
void | link_set_start_position(link: RID, position: Vector2)  
void | link_set_travel_cost(link: RID, travel_cost: float)  
RID | map_create()  
void | map_force_update(map: RID)  
Array[RID] | map_get_agents(map: RID) const  
float | map_get_cell_size(map: RID) const  
Vector2 | map_get_closest_point(map: RID, to_point: Vector2) const  
RID | map_get_closest_point_owner(map: RID, to_point: Vector2) const  
float | map_get_edge_connection_margin(map: RID) const  
int | map_get_iteration_id(map: RID) const  
float | map_get_link_connection_radius(map: RID) const  
Array[RID] | map_get_links(map: RID) const  
Array[RID] | map_get_obstacles(map: RID) const  
PackedVector2Array | map_get_path(map: RID, origin: Vector2, destination: Vector2, optimize: bool, navigation_layers: int = 1)  
Vector2 | map_get_random_point(map: RID, navigation_layers: int, uniformly: bool) const  
Array[RID] | map_get_regions(map: RID) const  
bool | map_get_use_async_iterations(map: RID) const  
bool | map_get_use_edge_connections(map: RID) const  
bool | map_is_active(map: RID) const  
void | map_set_active(map: RID, active: bool)  
void | map_set_cell_size(map: RID, cell_size: float)  
void | map_set_edge_connection_margin(map: RID, margin: float)  
void | map_set_link_connection_radius(map: RID, radius: float)  
void | map_set_use_async_iterations(map: RID, enabled: bool)  
void | map_set_use_edge_connections(map: RID, enabled: bool)  
RID | obstacle_create()  
bool | obstacle_get_avoidance_enabled(obstacle: RID) const  
int | obstacle_get_avoidance_layers(obstacle: RID) const  
RID | obstacle_get_map(obstacle: RID) const  
bool | obstacle_get_paused(obstacle: RID) const  
Vector2 | obstacle_get_position(obstacle: RID) const  
float | obstacle_get_radius(obstacle: RID) const  
Vector2 | obstacle_get_velocity(obstacle: RID) const  
PackedVector2Array | obstacle_get_vertices(obstacle: RID) const  
void | obstacle_set_avoidance_enabled(obstacle: RID, enabled: bool)  
void | obstacle_set_avoidance_layers(obstacle: RID, layers: int)  
void | obstacle_set_map(obstacle: RID, map: RID)  
void | obstacle_set_paused(obstacle: RID, paused: bool)  
void | obstacle_set_position(obstacle: RID, position: Vector2)  
void | obstacle_set_radius(obstacle: RID, radius: float)  
void | obstacle_set_velocity(obstacle: RID, velocity: Vector2)  
void | obstacle_set_vertices(obstacle: RID, vertices: PackedVector2Array)  
void | parse_source_geometry_data(navigation_polygon: NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D, root_node: Node, callback: Callable = Callable())  
void | query_path(parameters: NavigationPathQueryParameters2D, result: NavigationPathQueryResult2D, callback: Callable = Callable())  
RID | region_create()  
Rect2 | region_get_bounds(region: RID) const  
Vector2 | region_get_closest_point(region: RID, to_point: Vector2) const  
Vector2 | region_get_connection_pathway_end(region: RID, connection: int) const  
Vector2 | region_get_connection_pathway_start(region: RID, connection: int) const  
int | region_get_connections_count(region: RID) const  
bool | region_get_enabled(region: RID) const  
float | region_get_enter_cost(region: RID) const  
RID | region_get_map(region: RID) const  
int | region_get_navigation_layers(region: RID) const  
int | region_get_owner_id(region: RID) const  
Vector2 | region_get_random_point(region: RID, navigation_layers: int, uniformly: bool) const  
Transform2D | region_get_transform(region: RID) const  
float | region_get_travel_cost(region: RID) const  
bool | region_get_use_edge_connections(region: RID) const  
bool | region_owns_point(region: RID, point: Vector2) const  
void | region_set_enabled(region: RID, enabled: bool)  
void | region_set_enter_cost(region: RID, enter_cost: float)  
void | region_set_map(region: RID, map: RID)  
void | region_set_navigation_layers(region: RID, navigation_layers: int)  
void | region_set_navigation_polygon(region: RID, navigation_polygon: NavigationPolygon)  
void | region_set_owner_id(region: RID, owner_id: int)  
void | region_set_transform(region: RID, transform: Transform2D)  
void | region_set_travel_cost(region: RID, travel_cost: float)  
void | region_set_use_edge_connections(region: RID, enabled: bool)  
void | set_debug_enabled(enabled: bool)  
PackedVector2Array | simplify_path(path: PackedVector2Array, epsilon: float)  
RID | source_geometry_parser_create()  
void | source_geometry_parser_set_callback(parser: RID, callback: Callable)  
  
## Signals

map_changed(map: RID)

Emitted when a navigation map is updated, when a region moves or is modified.

navigation_debug_changed()

Emitted when navigation debug settings are changed. Only available in debug
builds.

## Method Descriptions

RID agent_create()

Creates the agent.

bool agent_get_avoidance_enabled(agent: RID) const

Return `true` if the specified `agent` uses avoidance.

int agent_get_avoidance_layers(agent: RID) const

Returns the `avoidance_layers` bitmask of the specified `agent`.

int agent_get_avoidance_mask(agent: RID) const

Returns the `avoidance_mask` bitmask of the specified `agent`.

float agent_get_avoidance_priority(agent: RID) const

Returns the `avoidance_priority` of the specified `agent`.

RID agent_get_map(agent: RID) const

Returns the navigation map RID the requested `agent` is currently assigned to.

int agent_get_max_neighbors(agent: RID) const

Returns the maximum number of other agents the specified `agent` takes into
account in the navigation.

float agent_get_max_speed(agent: RID) const

Returns the maximum speed of the specified `agent`.

float agent_get_neighbor_distance(agent: RID) const

Returns the maximum distance to other agents the specified `agent` takes into
account in the navigation.

bool agent_get_paused(agent: RID) const

Returns `true` if the specified `agent` is paused.

Vector2 agent_get_position(agent: RID) const

Returns the position of the specified `agent` in world space.

float agent_get_radius(agent: RID) const

Returns the radius of the specified `agent`.

float agent_get_time_horizon_agents(agent: RID) const

Returns the minimal amount of time for which the specified `agent`'s
velocities that are computed by the simulation are safe with respect to other
agents.

float agent_get_time_horizon_obstacles(agent: RID) const

Returns the minimal amount of time for which the specified `agent`'s
velocities that are computed by the simulation are safe with respect to static
avoidance obstacles.

Vector2 agent_get_velocity(agent: RID) const

Returns the velocity of the specified `agent`.

bool agent_has_avoidance_callback(agent: RID) const

Return `true` if the specified `agent` has an avoidance callback.

bool agent_is_map_changed(agent: RID) const

Returns `true` if the map got changed the previous frame.

void agent_set_avoidance_callback(agent: RID, callback: Callable)

Sets the callback Callable that gets called after each avoidance processing
step for the `agent`. The calculated `safe_velocity` will be dispatched with a
signal to the object just before the physics calculations.

Note: Created callbacks are always processed independently of the SceneTree
state as long as the agent is on a navigation map and not freed. To disable
the dispatch of a callback from an agent use agent_set_avoidance_callback()
again with an empty Callable.

void agent_set_avoidance_enabled(agent: RID, enabled: bool)

If `enabled` is `true`, the specified `agent` uses avoidance.

void agent_set_avoidance_layers(agent: RID, layers: int)

Set the agent's `avoidance_layers` bitmask.

void agent_set_avoidance_mask(agent: RID, mask: int)

Set the agent's `avoidance_mask` bitmask.

void agent_set_avoidance_priority(agent: RID, priority: float)

Set the agent's `avoidance_priority` with a `priority` between 0.0 (lowest
priority) to 1.0 (highest priority).

The specified `agent` does not adjust the velocity for other agents that would
match the `avoidance_mask` but have a lower `avoidance_priority`. This in turn
makes the other agents with lower priority adjust their velocities even more
to avoid collision with this agent.

void agent_set_map(agent: RID, map: RID)

Puts the agent in the map.

void agent_set_max_neighbors(agent: RID, count: int)

Sets the maximum number of other agents the agent takes into account in the
navigation. The larger this number, the longer the running time of the
simulation. If the number is too low, the simulation will not be safe.

void agent_set_max_speed(agent: RID, max_speed: float)

Sets the maximum speed of the agent. Must be positive.

void agent_set_neighbor_distance(agent: RID, distance: float)

Sets the maximum distance to other agents this agent takes into account in the
navigation. The larger this number, the longer the running time of the
simulation. If the number is too low, the simulation will not be safe.

void agent_set_paused(agent: RID, paused: bool)

If `paused` is `true` the specified `agent` will not be processed, e.g.
calculate avoidance velocities or receive avoidance callbacks.

void agent_set_position(agent: RID, position: Vector2)

Sets the position of the agent in world space.

void agent_set_radius(agent: RID, radius: float)

Sets the radius of the agent.

void agent_set_time_horizon_agents(agent: RID, time_horizon: float)

The minimal amount of time for which the agent's velocities that are computed
by the simulation are safe with respect to other agents. The larger this
number, the sooner this agent will respond to the presence of other agents,
but the less freedom this agent has in choosing its velocities. A too high
value will slow down agents movement considerably. Must be positive.

void agent_set_time_horizon_obstacles(agent: RID, time_horizon: float)

The minimal amount of time for which the agent's velocities that are computed
by the simulation are safe with respect to static avoidance obstacles. The
larger this number, the sooner this agent will respond to the presence of
static avoidance obstacles, but the less freedom this agent has in choosing
its velocities. A too high value will slow down agents movement considerably.
Must be positive.

void agent_set_velocity(agent: RID, velocity: Vector2)

Sets `velocity` as the new wanted velocity for the specified `agent`. The
avoidance simulation will try to fulfill this velocity if possible but will
modify it to avoid collision with other agent's and obstacles. When an agent
is teleported to a new position far away use agent_set_velocity_forced()
instead to reset the internal velocity state.

void agent_set_velocity_forced(agent: RID, velocity: Vector2)

Replaces the internal velocity in the collision avoidance simulation with
`velocity` for the specified `agent`. When an agent is teleported to a new
position far away this function should be used in the same frame. If called
frequently this function can get agents stuck.

void bake_from_source_geometry_data(navigation_polygon: NavigationPolygon,
source_geometry_data: NavigationMeshSourceGeometryData2D, callback: Callable =
Callable())

Bakes the provided `navigation_polygon` with the data from the provided
`source_geometry_data`. After the process is finished the optional `callback`
will be called.

void bake_from_source_geometry_data_async(navigation_polygon:
NavigationPolygon, source_geometry_data: NavigationMeshSourceGeometryData2D,
callback: Callable = Callable())

Bakes the provided `navigation_polygon` with the data from the provided
`source_geometry_data` as an async task running on a background thread. After
the process is finished the optional `callback` will be called.

void free_rid(rid: RID)

Destroys the given RID.

bool get_debug_enabled() const

Returns `true` when the NavigationServer has debug enabled.

Array[RID] get_maps() const

Returns all created navigation map RIDs on the NavigationServer. This returns
both 2D and 3D created navigation maps as there is technically no distinction
between them.

bool is_baking_navigation_polygon(navigation_polygon: NavigationPolygon) const

Returns `true` when the provided navigation polygon is being baked on a
background thread.

RID link_create()

Create a new link between two positions on a map.

bool link_get_enabled(link: RID) const

Returns `true` if the specified `link` is enabled.

Vector2 link_get_end_position(link: RID) const

Returns the ending position of this `link`.

float link_get_enter_cost(link: RID) const

Returns the enter cost of this `link`.

RID link_get_map(link: RID) const

Returns the navigation map RID the requested `link` is currently assigned to.

int link_get_navigation_layers(link: RID) const

Returns the navigation layers for this `link`.

int link_get_owner_id(link: RID) const

Returns the `ObjectID` of the object which manages this link.

Vector2 link_get_start_position(link: RID) const

Returns the starting position of this `link`.

float link_get_travel_cost(link: RID) const

Returns the travel cost of this `link`.

bool link_is_bidirectional(link: RID) const

Returns whether this `link` can be travelled in both directions.

void link_set_bidirectional(link: RID, bidirectional: bool)

Sets whether this `link` can be travelled in both directions.

void link_set_enabled(link: RID, enabled: bool)

If `enabled` is `true`, the specified `link` will contribute to its current
navigation map.

void link_set_end_position(link: RID, position: Vector2)

Sets the exit position for the `link`.

void link_set_enter_cost(link: RID, enter_cost: float)

Sets the `enter_cost` for this `link`.

void link_set_map(link: RID, map: RID)

Sets the navigation map RID for the link.

void link_set_navigation_layers(link: RID, navigation_layers: int)

Set the links's navigation layers. This allows selecting links from a path
request (when using map_get_path()).

void link_set_owner_id(link: RID, owner_id: int)

Set the `ObjectID` of the object which manages this link.

void link_set_start_position(link: RID, position: Vector2)

Sets the entry position for this `link`.

void link_set_travel_cost(link: RID, travel_cost: float)

Sets the `travel_cost` for this `link`.

RID map_create()

Create a new map.

void map_force_update(map: RID)

This function immediately forces synchronization of the specified navigation
`map` RID. By default navigation maps are only synchronized at the end of each
physics frame. This function can be used to immediately (re)calculate all the
navigation meshes and region connections of the navigation map. This makes it
possible to query a navigation path for a changed map immediately and in the
same frame (multiple times if needed).

Due to technical restrictions the current NavigationServer command queue will
be flushed. This means all already queued update commands for this physics
frame will be executed, even those intended for other maps, regions and agents
not part of the specified map. The expensive computation of the navigation
meshes and region connections of a map will only be done for the specified
map. Other maps will receive the normal synchronization at the end of the
physics frame. Should the specified map receive changes after the forced
update it will update again as well when the other maps receive their update.

Avoidance processing and dispatch of the `safe_velocity` signals is unaffected
by this function and continues to happen for all maps and agents at the end of
the physics frame.

Note: With great power comes great responsibility. This function should only
be used by users that really know what they are doing and have a good reason
for it. Forcing an immediate update of a navigation map requires locking the
NavigationServer and flushing the entire NavigationServer command queue. Not
only can this severely impact the performance of a game but it can also
introduce bugs if used inappropriately without much foresight.

Array[RID] map_get_agents(map: RID) const

Returns all navigation agents RIDs that are currently assigned to the
requested navigation `map`.

float map_get_cell_size(map: RID) const

Returns the map cell size used to rasterize the navigation mesh vertices.

Vector2 map_get_closest_point(map: RID, to_point: Vector2) const

Returns the navigation mesh surface point closest to the provided `to_point`
on the navigation `map`.

RID map_get_closest_point_owner(map: RID, to_point: Vector2) const

Returns the owner region RID for the navigation mesh surface point closest to
the provided `to_point` on the navigation `map`.

float map_get_edge_connection_margin(map: RID) const

Returns the edge connection margin of the map. The edge connection margin is a
distance used to connect two regions.

int map_get_iteration_id(map: RID) const

Returns the current iteration id of the navigation map. Every time the
navigation map changes and synchronizes the iteration id increases. An
iteration id of 0 means the navigation map has never synchronized.

Note: The iteration id will wrap back to 1 after reaching its range limit.

float map_get_link_connection_radius(map: RID) const

Returns the link connection radius of the map. This distance is the maximum
range any link will search for navigation mesh polygons to connect to.

Array[RID] map_get_links(map: RID) const

Returns all navigation link RIDs that are currently assigned to the requested
navigation `map`.

Array[RID] map_get_obstacles(map: RID) const

Returns all navigation obstacle RIDs that are currently assigned to the
requested navigation `map`.

PackedVector2Array map_get_path(map: RID, origin: Vector2, destination:
Vector2, optimize: bool, navigation_layers: int = 1)

Returns the navigation path to reach the destination from the origin.
`navigation_layers` is a bitmask of all region navigation layers that are
allowed to be in the path.

Vector2 map_get_random_point(map: RID, navigation_layers: int, uniformly:
bool) const

Returns a random position picked from all map region polygons with matching
`navigation_layers`.

If `uniformly` is `true`, all map regions, polygons, and faces are weighted by
their surface area (slower).

If `uniformly` is `false`, just a random region and a random polygon are
picked (faster).

Array[RID] map_get_regions(map: RID) const

Returns all navigation regions RIDs that are currently assigned to the
requested navigation `map`.

bool map_get_use_async_iterations(map: RID) const

Returns `true` if the `map` synchronization uses an async process that runs on
a background thread.

bool map_get_use_edge_connections(map: RID) const

Returns whether the navigation `map` allows navigation regions to use edge
connections to connect with other navigation regions within proximity of the
navigation map edge connection margin.

bool map_is_active(map: RID) const

Returns `true` if the map is active.

void map_set_active(map: RID, active: bool)

Sets the map active.

void map_set_cell_size(map: RID, cell_size: float)

Sets the map cell size used to rasterize the navigation mesh vertices. Must
match with the cell size of the used navigation meshes.

void map_set_edge_connection_margin(map: RID, margin: float)

Set the map edge connection margin used to weld the compatible region edges.

void map_set_link_connection_radius(map: RID, radius: float)

Set the map's link connection radius used to connect links to navigation
polygons.

void map_set_use_async_iterations(map: RID, enabled: bool)

If `enabled` is `true` the `map` synchronization uses an async process that
runs on a background thread.

void map_set_use_edge_connections(map: RID, enabled: bool)

Set the navigation `map` edge connection use. If `enabled` is `true`, the
navigation map allows navigation regions to use edge connections to connect
with other navigation regions within proximity of the navigation map edge
connection margin.

RID obstacle_create()

Creates a new navigation obstacle.

bool obstacle_get_avoidance_enabled(obstacle: RID) const

Returns `true` if the provided `obstacle` has avoidance enabled.

int obstacle_get_avoidance_layers(obstacle: RID) const

Returns the `avoidance_layers` bitmask of the specified `obstacle`.

RID obstacle_get_map(obstacle: RID) const

Returns the navigation map RID the requested `obstacle` is currently assigned
to.

bool obstacle_get_paused(obstacle: RID) const

Returns `true` if the specified `obstacle` is paused.

Vector2 obstacle_get_position(obstacle: RID) const

Returns the position of the specified `obstacle` in world space.

float obstacle_get_radius(obstacle: RID) const

Returns the radius of the specified dynamic `obstacle`.

Vector2 obstacle_get_velocity(obstacle: RID) const

Returns the velocity of the specified dynamic `obstacle`.

PackedVector2Array obstacle_get_vertices(obstacle: RID) const

Returns the outline vertices for the specified `obstacle`.

void obstacle_set_avoidance_enabled(obstacle: RID, enabled: bool)

If `enabled` is `true`, the provided `obstacle` affects avoidance using
agents.

void obstacle_set_avoidance_layers(obstacle: RID, layers: int)

Set the obstacles's `avoidance_layers` bitmask.

void obstacle_set_map(obstacle: RID, map: RID)

Sets the navigation map RID for the obstacle.

void obstacle_set_paused(obstacle: RID, paused: bool)

If `paused` is `true` the specified `obstacle` will not be processed, e.g.
affect avoidance velocities.

void obstacle_set_position(obstacle: RID, position: Vector2)

Sets the position of the obstacle in world space.

void obstacle_set_radius(obstacle: RID, radius: float)

Sets the radius of the dynamic obstacle.

void obstacle_set_velocity(obstacle: RID, velocity: Vector2)

Sets `velocity` of the dynamic `obstacle`. Allows other agents to better
predict the movement of the dynamic obstacle. Only works in combination with
the radius of the obstacle.

void obstacle_set_vertices(obstacle: RID, vertices: PackedVector2Array)

Sets the outline vertices for the obstacle. If the vertices are winded in
clockwise order agents will be pushed in by the obstacle, else they will be
pushed out.

void parse_source_geometry_data(navigation_polygon: NavigationPolygon,
source_geometry_data: NavigationMeshSourceGeometryData2D, root_node: Node,
callback: Callable = Callable())

Parses the SceneTree for source geometry according to the properties of
`navigation_polygon`. Updates the provided `source_geometry_data` resource
with the resulting data. The resource can then be used to bake a navigation
mesh with bake_from_source_geometry_data(). After the process is finished the
optional `callback` will be called.

Note: This function needs to run on the main thread or with a deferred call as
the SceneTree is not thread-safe.

Performance: While convenient, reading data arrays from Mesh resources can
affect the frame rate negatively. The data needs to be received from the GPU,
stalling the RenderingServer in the process. For performance prefer the use of
e.g. collision shapes or creating the data arrays entirely in code.

void query_path(parameters: NavigationPathQueryParameters2D, result:
NavigationPathQueryResult2D, callback: Callable = Callable())

Queries a path in a given navigation map. Start and target position and other
parameters are defined through NavigationPathQueryParameters2D. Updates the
provided NavigationPathQueryResult2D result object with the path among other
results requested by the query. After the process is finished the optional
`callback` will be called.

RID region_create()

Creates a new region.

Rect2 region_get_bounds(region: RID) const

Returns the axis-aligned rectangle for the `region`'s transformed navigation
mesh.

Vector2 region_get_closest_point(region: RID, to_point: Vector2) const

Returns the navigation mesh surface point closest to the provided `to_point`
on the navigation `region`.

Vector2 region_get_connection_pathway_end(region: RID, connection: int) const

Returns the ending point of a connection door. `connection` is an index
between 0 and the return value of region_get_connections_count().

Vector2 region_get_connection_pathway_start(region: RID, connection: int)
const

Returns the starting point of a connection door. `connection` is an index
between 0 and the return value of region_get_connections_count().

int region_get_connections_count(region: RID) const

Returns how many connections this `region` has with other regions in the map.

bool region_get_enabled(region: RID) const

Returns `true` if the specified `region` is enabled.

float region_get_enter_cost(region: RID) const

Returns the enter cost of this `region`.

RID region_get_map(region: RID) const

Returns the navigation map RID the requested `region` is currently assigned
to.

int region_get_navigation_layers(region: RID) const

Returns the region's navigation layers.

int region_get_owner_id(region: RID) const

Returns the `ObjectID` of the object which manages this region.

Vector2 region_get_random_point(region: RID, navigation_layers: int,
uniformly: bool) const

Returns a random position picked from all region polygons with matching
`navigation_layers`.

If `uniformly` is `true`, all region polygons and faces are weighted by their
surface area (slower).

If `uniformly` is `false`, just a random polygon and face is picked (faster).

Transform2D region_get_transform(region: RID) const

Returns the global transformation of this `region`.

float region_get_travel_cost(region: RID) const

Returns the travel cost of this `region`.

bool region_get_use_edge_connections(region: RID) const

Returns whether the navigation `region` is set to use edge connections to
connect with other navigation regions within proximity of the navigation map
edge connection margin.

bool region_owns_point(region: RID, point: Vector2) const

Returns `true` if the provided `point` in world space is currently owned by
the provided navigation `region`. Owned in this context means that one of the
region's navigation mesh polygon faces has a possible position at the closest
distance to this point compared to all other navigation meshes from other
navigation regions that are also registered on the navigation map of the
provided region.

If multiple navigation meshes have positions at equal distance the navigation
region whose polygons are processed first wins the ownership. Polygons are
processed in the same order that navigation regions were registered on the
NavigationServer.

Note: If navigation meshes from different navigation regions overlap (which
should be avoided in general) the result might not be what is expected.

void region_set_enabled(region: RID, enabled: bool)

If `enabled` is `true` the specified `region` will contribute to its current
navigation map.

void region_set_enter_cost(region: RID, enter_cost: float)

Sets the `enter_cost` for this `region`.

void region_set_map(region: RID, map: RID)

Sets the map for the region.

void region_set_navigation_layers(region: RID, navigation_layers: int)

Set the region's navigation layers. This allows selecting regions from a path
request (when using map_get_path()).

void region_set_navigation_polygon(region: RID, navigation_polygon:
NavigationPolygon)

Sets the `navigation_polygon` for the region.

void region_set_owner_id(region: RID, owner_id: int)

Set the `ObjectID` of the object which manages this region.

void region_set_transform(region: RID, transform: Transform2D)

Sets the global transformation for the region.

void region_set_travel_cost(region: RID, travel_cost: float)

Sets the `travel_cost` for this `region`.

void region_set_use_edge_connections(region: RID, enabled: bool)

If `enabled` is `true`, the navigation `region` will use edge connections to
connect with other navigation regions within proximity of the navigation map
edge connection margin.

void set_debug_enabled(enabled: bool)

If `true` enables debug mode on the NavigationServer.

PackedVector2Array simplify_path(path: PackedVector2Array, epsilon: float)

Returns a simplified version of `path` with less critical path points removed.
The simplification amount is in worlds units and controlled by `epsilon`. The
simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve
point decimation.

Path simplification can be helpful to mitigate various path following issues
that can arise with certain agent types and script behaviors. E.g. "steering"
agents or avoidance in "open fields".

RID source_geometry_parser_create()

Creates a new source geometry parser. If a Callable is set for the parser with
source_geometry_parser_set_callback() the callback will be called for every
single node that gets parsed whenever parse_source_geometry_data() is used.

void source_geometry_parser_set_callback(parser: RID, callback: Callable)

Sets the `callback` Callable for the specific source geometry `parser`. The
Callable will receive a call with the following parameters:

  * `navigation_mesh` \- The NavigationPolygon reference used to define the parse settings. Do NOT edit or add directly to the navigation mesh.

  * `source_geometry_data` \- The NavigationMeshSourceGeometryData2D reference. Add custom source geometry for navigation mesh baking to this object.

  * `node` \- The Node that is parsed.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

