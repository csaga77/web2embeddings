# GPUParticlesCollision3D

Inherits: VisualInstance3D < Node3D < Node < Object

Inherited By: GPUParticlesCollisionBox3D, GPUParticlesCollisionHeightField3D,
GPUParticlesCollisionSDF3D, GPUParticlesCollisionSphere3D

Abstract base class for 3D particle collision shapes affecting GPUParticles3D
nodes.

## Description

Particle collision shapes can be used to make particles stop or bounce against
them.

Particle collision shapes work in real-time and can be moved, rotated and
scaled during gameplay. Unlike attractors, non-uniform scaling of collision
shapes is not supported.

Particle collision shapes can be temporarily disabled by hiding them.

Note: ParticleProcessMaterial.collision_mode must be
ParticleProcessMaterial.COLLISION_RIGID or
ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT on the GPUParticles3D's
process material for collision to work.

Note: Particle collision only affects GPUParticles3D, not CPUParticles3D.

Note: Particles pushed by a collider that is being moved will not be
interpolated, which can result in visible stuttering. This can be alleviated
by setting GPUParticles3D.fixed_fps to `0` or a value that matches or exceeds
the target framerate.

## Properties

int | cull_mask | `4294967295`  
---|---|---  
  
## Property Descriptions

int cull_mask = `4294967295`

  * void set_cull_mask(value: int)

  * int get_cull_mask()

The particle rendering layers (VisualInstance3D.layers) that will be affected
by the collision shape. By default, all particles that have
ParticleProcessMaterial.collision_mode set to
ParticleProcessMaterial.COLLISION_RIGID or
ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT will be affected by a
collision shape.

After configuring particle nodes accordingly, specific layers can be unchecked
to prevent certain particles from being affected by colliders. For example,
this can be used if you're using a collider as part of a spell effect but
don't want the collider to affect unrelated weather particles at the same
position.

Particle collision can also be disabled on a per-process material basis by
setting ParticleProcessMaterial.collision_mode on the GPUParticles3D node.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

