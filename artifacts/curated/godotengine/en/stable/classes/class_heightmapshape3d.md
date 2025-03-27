# HeightMapShape3D

Inherits: Shape3D < Resource < RefCounted < Object

A 3D height map shape used for physics collision.

## Description

A 3D heightmap shape, intended for use in physics. Usually used to provide a
shape for a CollisionShape3D. This is useful for terrain, but it is limited as
overhangs (such as caves) cannot be stored. Holes in a HeightMapShape3D are
created by assigning very low values to points in the desired area.

Performance: HeightMapShape3D is faster to check collisions against than
ConcavePolygonShape3D, but it is significantly slower than primitive shapes
like BoxShape3D.

A heightmap collision shape can also be build by using an Image reference:

GDScript

    
    
    var heightmap_texture = ResourceLoader.load("res://heightmap_image.exr")
    var heightmap_image = heightmap_texture.get_image()
    heightmap_image.convert(Image.FORMAT_RF)
    
    var height_min = 0.0
    var height_max = 10.0
    
    update_map_data_from_image(heightmap_image, height_min, height_max)
    

## Properties

PackedFloat32Array | map_data | `PackedFloat32Array(0, 0, 0, 0)`  
---|---|---  
int | map_depth | `2`  
int | map_width | `2`  
  
## Methods

float | get_max_height() const  
---|---  
float | get_min_height() const  
void | update_map_data_from_image(image: Image, height_min: float, height_max: float)  
  
## Property Descriptions

PackedFloat32Array map_data = `PackedFloat32Array(0, 0, 0, 0)`

  * void set_map_data(value: PackedFloat32Array)

  * PackedFloat32Array get_map_data()

Height map data. The array's size must be equal to map_width multiplied by
map_depth.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedFloat32Array for more details.

int map_depth = `2`

  * void set_map_depth(value: int)

  * int get_map_depth()

Number of vertices in the depth of the height map. Changing this will resize
the map_data.

int map_width = `2`

  * void set_map_width(value: int)

  * int get_map_width()

Number of vertices in the width of the height map. Changing this will resize
the map_data.

## Method Descriptions

float get_max_height() const

Returns the largest height value found in map_data. Recalculates only when
map_data changes.

float get_min_height() const

Returns the smallest height value found in map_data. Recalculates only when
map_data changes.

void update_map_data_from_image(image: Image, height_min: float, height_max:
float)

Updates map_data with data read from an Image reference. Automatically resizes
heightmap map_width and map_depth to fit the full image width and height.

The image needs to be in either Image.FORMAT_RF (32 bit), Image.FORMAT_RH (16
bit), or Image.FORMAT_R8 (8 bit).

Each image pixel is read in as a float on the range from `0.0` (black pixel)
to `1.0` (white pixel). This range value gets remapped to `height_min` and
`height_max` to form the final height value.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

