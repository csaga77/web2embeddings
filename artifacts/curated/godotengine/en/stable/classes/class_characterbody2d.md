# CharacterBody2D

Inherits: PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node <
Object

A 2D physics body specialized for characters moved by script.

## Description

CharacterBody2D is a specialized class for physics bodies that are meant to be
user-controlled. They are not affected by physics at all, but they affect
other physics bodies in their path. They are mainly used to provide high-level
API to move objects with wall and slope detection (move_and_slide() method) in
addition to the general collision detection provided by
PhysicsBody2D.move_and_collide(). This makes it useful for highly configurable
physics bodies that must move in specific ways and collide with the world, as
is often the case with user-controlled characters.

For game objects that don't require complex movement or collision detection,
such as moving platforms, AnimatableBody2D is simpler to configure.

## Tutorials

  * Kinematic character (2D)

  * Using CharacterBody2D

  * 2D Kinematic Character Demo

  * 2D Platformer Demo

## Properties

bool | floor_block_on_wall | `true`  
---|---|---  
bool | floor_constant_speed | `false`  
float | floor_max_angle | `0.785398`  
float | floor_snap_length | `1.0`  
bool | floor_stop_on_slope | `true`  
int | max_slides | `4`  
MotionMode | motion_mode | `0`  
int | platform_floor_layers | `4294967295`  
PlatformOnLeave | platform_on_leave | `0`  
int | platform_wall_layers | `0`  
float | safe_margin | `0.08`  
bool | slide_on_ceiling | `true`  
Vector2 | up_direction | `Vector2(0, -1)`  
Vector2 | velocity | `Vector2(0, 0)`  
float | wall_min_slide_angle | `0.261799`  
  
## Methods

void | apply_floor_snap()  
---|---  
float | get_floor_angle(up_direction: Vector2 = Vector2(0, -1)) const  
Vector2 | get_floor_normal() const  
Vector2 | get_last_motion() const  
KinematicCollision2D | get_last_slide_collision()  
Vector2 | get_platform_velocity() const  
Vector2 | get_position_delta() const  
Vector2 | get_real_velocity() const  
KinematicCollision2D | get_slide_collision(slide_idx: int)  
int | get_slide_collision_count() const  
Vector2 | get_wall_normal() const  
bool | is_on_ceiling() const  
bool | is_on_ceiling_only() const  
bool | is_on_floor() const  
bool | is_on_floor_only() const  
bool | is_on_wall() const  
bool | is_on_wall_only() const  
bool | move_and_slide()  
  
## Enumerations

enum MotionMode:

MotionMode MOTION_MODE_GROUNDED = `0`

Apply when notions of walls, ceiling and floor are relevant. In this mode the
body motion will react to slopes (acceleration/slowdown). This mode is
suitable for sided games like platformers.

MotionMode MOTION_MODE_FLOATING = `1`

Apply when there is no notion of floor or ceiling. All collisions will be
reported as `on_wall`. In this mode, when you slide, the speed will always be
constant. This mode is suitable for top-down games.

enum PlatformOnLeave:

PlatformOnLeave PLATFORM_ON_LEAVE_ADD_VELOCITY = `0`

Add the last platform velocity to the velocity when you leave a moving
platform.

PlatformOnLeave PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY = `1`

Add the last platform velocity to the velocity when you leave a moving
platform, but any downward motion is ignored. It's useful to keep full jump
height even when the platform is moving down.

PlatformOnLeave PLATFORM_ON_LEAVE_DO_NOTHING = `2`

Do nothing when leaving a platform.

## Property Descriptions

bool floor_block_on_wall = `true`

  * void set_floor_block_on_wall_enabled(value: bool)

  * bool is_floor_block_on_wall_enabled()

If `true`, the body will be able to move on the floor only. This option avoids
to be able to walk on walls, it will however allow to slide down along them.

bool floor_constant_speed = `false`

  * void set_floor_constant_speed_enabled(value: bool)

  * bool is_floor_constant_speed_enabled()

If `false` (by default), the body will move faster on downward slopes and
slower on upward slopes.

If `true`, the body will always move at the same speed on the ground no matter
the slope. Note that you need to use floor_snap_length to stick along a
downward slope at constant speed.

float floor_max_angle = `0.785398`

  * void set_floor_max_angle(value: float)

  * float get_floor_max_angle()

Maximum angle (in radians) where a slope is still considered a floor (or a
ceiling), rather than a wall, when calling move_and_slide(). The default value
equals 45 degrees.

float floor_snap_length = `1.0`

  * void set_floor_snap_length(value: float)

  * float get_floor_snap_length()

Sets a snapping distance. When set to a value different from `0.0`, the body
is kept attached to slopes when calling move_and_slide(). The snapping vector
is determined by the given distance along the opposite direction of the
up_direction.

As long as the snapping vector is in contact with the ground and the body
moves against up_direction, the body will remain attached to the surface.
Snapping is not applied if the body moves along up_direction, meaning it
contains vertical rising velocity, so it will be able to detach from the
ground when jumping or when the body is pushed up by something. If you want to
apply a snap without taking into account the velocity, use apply_floor_snap().

bool floor_stop_on_slope = `true`

  * void set_floor_stop_on_slope_enabled(value: bool)

  * bool is_floor_stop_on_slope_enabled()

If `true`, the body will not slide on slopes when calling move_and_slide()
when the body is standing still.

If `false`, the body will slide on floor's slopes when velocity applies a
downward force.

int max_slides = `4`

  * void set_max_slides(value: int)

  * int get_max_slides()

Maximum number of times the body can change direction before it stops when
calling move_and_slide().

MotionMode motion_mode = `0`

  * void set_motion_mode(value: MotionMode)

  * MotionMode get_motion_mode()

Sets the motion mode which defines the behavior of move_and_slide(). See
MotionMode constants for available modes.

int platform_floor_layers = `4294967295`

  * void set_platform_floor_layers(value: int)

  * int get_platform_floor_layers()

Collision layers that will be included for detecting floor bodies that will
act as moving platforms to be followed by the CharacterBody2D. By default, all
floor bodies are detected and propagate their velocity.

PlatformOnLeave platform_on_leave = `0`

  * void set_platform_on_leave(value: PlatformOnLeave)

  * PlatformOnLeave get_platform_on_leave()

Sets the behavior to apply when you leave a moving platform. By default, to be
physically accurate, when you leave the last platform velocity is applied. See
PlatformOnLeave constants for available behavior.

int platform_wall_layers = `0`

  * void set_platform_wall_layers(value: int)

  * int get_platform_wall_layers()

Collision layers that will be included for detecting wall bodies that will act
as moving platforms to be followed by the CharacterBody2D. By default, all
wall bodies are ignored.

float safe_margin = `0.08`

  * void set_safe_margin(value: float)

  * float get_safe_margin()

Extra margin used for collision recovery when calling move_and_slide().

If the body is at least this close to another body, it will consider them to
be colliding and will be pushed away before performing the actual motion.

A higher value means it's more flexible for detecting collision, which helps
with consistently detecting walls and floors.

A lower value forces the collision algorithm to use more exact detection, so
it can be used in cases that specifically require precision, e.g at very low
scale to avoid visible jittering, or for stability with a stack of character
bodies.

bool slide_on_ceiling = `true`

  * void set_slide_on_ceiling_enabled(value: bool)

  * bool is_slide_on_ceiling_enabled()

If `true`, during a jump against the ceiling, the body will slide, if `false`
it will be stopped and will fall vertically.

Vector2 up_direction = `Vector2(0, -1)`

  * void set_up_direction(value: Vector2)

  * Vector2 get_up_direction()

Vector pointing upwards, used to determine what is a wall and what is a floor
(or a ceiling) when calling move_and_slide(). Defaults to Vector2.UP. As the
vector will be normalized it can't be equal to Vector2.ZERO, if you want all
collisions to be reported as walls, consider using MOTION_MODE_FLOATING as
motion_mode.

Vector2 velocity = `Vector2(0, 0)`

  * void set_velocity(value: Vector2)

  * Vector2 get_velocity()

Current velocity vector in pixels per second, used and modified during calls
to move_and_slide().

float wall_min_slide_angle = `0.261799`

  * void set_wall_min_slide_angle(value: float)

  * float get_wall_min_slide_angle()

Minimum angle (in radians) where the body is allowed to slide when it
encounters a slope. The default value equals 15 degrees. This property only
affects movement when motion_mode is MOTION_MODE_FLOATING.

## Method Descriptions

void apply_floor_snap()

Allows to manually apply a snap to the floor regardless of the body's
velocity. This function does nothing when is_on_floor() returns `true`.

float get_floor_angle(up_direction: Vector2 = Vector2(0, -1)) const

Returns the floor's collision angle at the last collision point according to
`up_direction`, which is Vector2.UP by default. This value is always positive
and only valid after calling move_and_slide() and when is_on_floor() returns
`true`.

Vector2 get_floor_normal() const

Returns the collision normal of the floor at the last collision point. Only
valid after calling move_and_slide() and when is_on_floor() returns `true`.

Warning: The collision normal is not always the same as the surface normal.

Vector2 get_last_motion() const

Returns the last motion applied to the CharacterBody2D during the last call to
move_and_slide(). The movement can be split into multiple motions when sliding
occurs, and this method return the last one, which is useful to retrieve the
current direction of the movement.

KinematicCollision2D get_last_slide_collision()

Returns a KinematicCollision2D, which contains information about the latest
collision that occurred during the last call to move_and_slide().

Vector2 get_platform_velocity() const

Returns the linear velocity of the platform at the last collision point. Only
valid after calling move_and_slide().

Vector2 get_position_delta() const

Returns the travel (position delta) that occurred during the last call to
move_and_slide().

Vector2 get_real_velocity() const

Returns the current real velocity since the last call to move_and_slide(). For
example, when you climb a slope, you will move diagonally even though the
velocity is horizontal. This method returns the diagonal movement, as opposed
to velocity which returns the requested velocity.

KinematicCollision2D get_slide_collision(slide_idx: int)

Returns a KinematicCollision2D, which contains information about a collision
that occurred during the last call to move_and_slide(). Since the body can
collide several times in a single call to move_and_slide(), you must specify
the index of the collision in the range 0 to (get_slide_collision_count() \-
1).

Example: Iterate through the collisions with a `for` loop:

GDScriptC#

    
    
    for i in get_slide_collision_count():
        var collision = get_slide_collision(i)
        print("Collided with: ", collision.get_collider().name)
    
    
    
    for (int i = 0; i < GetSlideCollisionCount(); i++)
    {
        KinematicCollision2D collision = GetSlideCollision(i);
        GD.Print("Collided with: ", (collision.GetCollider() as Node).Name);
    }
    

int get_slide_collision_count() const

Returns the number of times the body collided and changed direction during the
last call to move_and_slide().

Vector2 get_wall_normal() const

Returns the collision normal of the wall at the last collision point. Only
valid after calling move_and_slide() and when is_on_wall() returns `true`.

Warning: The collision normal is not always the same as the surface normal.

bool is_on_ceiling() const

Returns `true` if the body collided with the ceiling on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "ceiling" or not.

bool is_on_ceiling_only() const

Returns `true` if the body collided only with the ceiling on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "ceiling" or not.

bool is_on_floor() const

Returns `true` if the body collided with the floor on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "floor" or not.

bool is_on_floor_only() const

Returns `true` if the body collided only with the floor on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "floor" or not.

bool is_on_wall() const

Returns `true` if the body collided with a wall on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "wall" or not.

bool is_on_wall_only() const

Returns `true` if the body collided only with a wall on the last call of
move_and_slide(). Otherwise, returns `false`. The up_direction and
floor_max_angle are used to determine whether a surface is "wall" or not.

bool move_and_slide()

Moves the body based on velocity. If the body collides with another, it will
slide along the other body (by default only on floor) rather than stop
immediately. If the other body is a CharacterBody2D or RigidBody2D, it will
also be affected by the motion of the other body. You can use this to make
moving and rotating platforms, or to make nodes push other nodes.

Modifies velocity if a slide collision occurred. To get the latest collision
call get_last_slide_collision(), for detailed information about collisions
that occurred, use get_slide_collision().

When the body touches a moving platform, the platform's velocity is
automatically added to the body motion. If a collision occurs due to the
platform's motion, it will always be first in the slide collisions.

The general behavior and available properties change according to the
motion_mode.

Returns `true` if the body collided, otherwise, returns `false`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

