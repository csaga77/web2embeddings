# NavigationPathQueryResult2D

Experimental: This class may be changed or removed in future versions.

Inherits: RefCounted < Object

Represents the result of a 2D pathfinding query.

## Description

This class stores the result of a 2D navigation path query from the
NavigationServer2D.

## Tutorials

  * Using NavigationPathQueryObjects

## Properties

PackedVector2Array | path | `PackedVector2Array()`  
---|---|---  
PackedInt64Array | path_owner_ids | `PackedInt64Array()`  
Array[RID] | path_rids | `[]`  
PackedInt32Array | path_types | `PackedInt32Array()`  
  
## Methods

void | reset()  
---|---  
  
## Enumerations

enum PathSegmentType:

PathSegmentType PATH_SEGMENT_TYPE_REGION = `0`

This segment of the path goes through a region.

PathSegmentType PATH_SEGMENT_TYPE_LINK = `1`

This segment of the path goes through a link.

## Property Descriptions

PackedVector2Array path = `PackedVector2Array()`

  * void set_path(value: PackedVector2Array)

  * PackedVector2Array get_path()

The resulting path array from the navigation query. All path array positions
are in global coordinates. Without customized query parameters this is the
same path as returned by NavigationServer2D.map_get_path().

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedVector2Array for more details.

PackedInt64Array path_owner_ids = `PackedInt64Array()`

  * void set_path_owner_ids(value: PackedInt64Array)

  * PackedInt64Array get_path_owner_ids()

The `ObjectID`s of the Objects which manage the regions and links each point
of the path goes through.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedInt64Array for more details.

Array[RID] path_rids = `[]`

  * void set_path_rids(value: Array[RID])

  * Array[RID] get_path_rids()

The RIDs of the regions and links that each point of the path goes through.

PackedInt32Array path_types = `PackedInt32Array()`

  * void set_path_types(value: PackedInt32Array)

  * PackedInt32Array get_path_types()

The type of navigation primitive (region or link) that each point of the path
goes through.

Note: The returned array is copied and any changes to it will not update the
original property value. See PackedInt32Array for more details.

## Method Descriptions

void reset()

Reset the result object to its initial state. This is useful to reuse the
object across multiple queries.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

