# NavigationMeshSourceGeometryData3D

Experimental: This class may be changed or removed in future versions.

Inherits: Resource < RefCounted < Object

Container for parsed source geometry data used in navigation mesh baking.

## Description

Container for parsed source geometry data used in navigation mesh baking.

## Methods

void | add_faces(faces: PackedVector3Array, xform: Transform3D)  
---|---  
void | add_mesh(mesh: Mesh, xform: Transform3D)  
void | add_mesh_array(mesh_array: Array, xform: Transform3D)  
void | add_projected_obstruction(vertices: PackedVector3Array, elevation: float, height: float, carve: bool)  
void | append_arrays(vertices: PackedFloat32Array, indices: PackedInt32Array)  
void | clear()  
void | clear_projected_obstructions()  
AABB | get_bounds()  
PackedInt32Array | get_indices() const  
Array | get_projected_obstructions() const  
PackedFloat32Array | get_vertices() const  
bool | has_data()  
void | merge(other_geometry: NavigationMeshSourceGeometryData3D)  
void | set_indices(indices: PackedInt32Array)  
void | set_projected_obstructions(projected_obstructions: Array)  
void | set_vertices(vertices: PackedFloat32Array)  
  
## Method Descriptions

void add_faces(faces: PackedVector3Array, xform: Transform3D)

Adds an array of vertex positions to the geometry data for navigation mesh
baking to form triangulated faces. For each face the array must have three
vertex positions in clockwise winding order. Since NavigationMesh resources
have no transform, all vertex positions need to be offset by the node's
transform using `xform`.

void add_mesh(mesh: Mesh, xform: Transform3D)

Adds the geometry data of a Mesh resource to the navigation mesh baking data.
The mesh must have valid triangulated mesh data to be considered. Since
NavigationMesh resources have no transform, all vertex positions need to be
offset by the node's transform using `xform`.

void add_mesh_array(mesh_array: Array, xform: Transform3D)

Adds an Array the size of Mesh.ARRAY_MAX and with vertices at index
Mesh.ARRAY_VERTEX and indices at index Mesh.ARRAY_INDEX to the navigation mesh
baking data. The array must have valid triangulated mesh data to be
considered. Since NavigationMesh resources have no transform, all vertex
positions need to be offset by the node's transform using `xform`.

void add_projected_obstruction(vertices: PackedVector3Array, elevation: float,
height: float, carve: bool)

Adds a projected obstruction shape to the source geometry. The `vertices` are
considered projected on a xz-axes plane, placed at the global y-axis
`elevation` and extruded by `height`. If `carve` is `true` the carved shape
will not be affected by additional offsets (e.g. agent radius) of the
navigation mesh baking process.

void append_arrays(vertices: PackedFloat32Array, indices: PackedInt32Array)

Appends arrays of `vertices` and `indices` at the end of the existing arrays.
Adds the existing index as an offset to the appended indices.

void clear()

Clears the internal data.

void clear_projected_obstructions()

Clears all projected obstructions.

AABB get_bounds()

Returns an axis-aligned bounding box that covers all the stored geometry data.
The bounds are calculated when calling this function with the result cached
until further geometry changes are made.

PackedInt32Array get_indices() const

Returns the parsed source geometry data indices array.

Array get_projected_obstructions() const

Returns the projected obstructions as an Array of dictionaries. Each
Dictionary contains the following entries:

  * `vertices` \- A PackedFloat32Array that defines the outline points of the projected shape.

  * `elevation` \- A float that defines the projected shape placement on the y-axis.

  * `height` \- A float that defines how much the projected shape is extruded along the y-axis.

  * `carve` \- A bool that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

PackedFloat32Array get_vertices() const

Returns the parsed source geometry data vertices array.

bool has_data()

Returns `true` when parsed source geometry data exists.

void merge(other_geometry: NavigationMeshSourceGeometryData3D)

Adds the geometry data of another NavigationMeshSourceGeometryData3D to the
navigation mesh baking data.

void set_indices(indices: PackedInt32Array)

Sets the parsed source geometry data indices. The indices need to be matched
with appropriated vertices.

Warning: Inappropriate data can crash the baking process of the involved
third-party libraries.

void set_projected_obstructions(projected_obstructions: Array)

Sets the projected obstructions with an Array of Dictionaries with the
following key value pairs:

GDScript

    
    
    "vertices" : PackedFloat32Array
    "elevation" : float
    "height" : float
    "carve" : bool
    

void set_vertices(vertices: PackedFloat32Array)

Sets the parsed source geometry data vertices. The vertices need to be matched
with appropriated indices.

Warning: Inappropriate data can crash the baking process of the involved
third-party libraries.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

