# PhysicsServer3DRenderingServerHandler

Inherits: Object

A class used to provide
PhysicsServer3DExtension._soft_body_update_rendering_server() with a rendering
handler for soft bodies.

## Methods

void | _set_aabb(aabb: AABB) virtual  
---|---  
void | _set_normal(vertex_id: int, normal: Vector3) virtual  
void | _set_vertex(vertex_id: int, vertex: Vector3) virtual  
void | set_aabb(aabb: AABB)  
void | set_normal(vertex_id: int, normal: Vector3)  
void | set_vertex(vertex_id: int, vertex: Vector3)  
  
## Method Descriptions

void _set_aabb(aabb: AABB) virtual

Called by the PhysicsServer3D to set the bounding box for the SoftBody3D.

void _set_normal(vertex_id: int, normal: Vector3) virtual

Called by the PhysicsServer3D to set the normal for the SoftBody3D vertex at
the index specified by `vertex_id`.

Note: The `normal` parameter used to be of type `const void*` prior to Godot
4.2.

void _set_vertex(vertex_id: int, vertex: Vector3) virtual

Called by the PhysicsServer3D to set the position for the SoftBody3D vertex at
the index specified by `vertex_id`.

Note: The `vertex` parameter used to be of type `const void*` prior to Godot
4.2.

void set_aabb(aabb: AABB)

Sets the bounding box for the SoftBody3D.

void set_normal(vertex_id: int, normal: Vector3)

Sets the normal for the SoftBody3D vertex at the index specified by
`vertex_id`.

void set_vertex(vertex_id: int, vertex: Vector3)

Sets the position for the SoftBody3D vertex at the index specified by
`vertex_id`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.

