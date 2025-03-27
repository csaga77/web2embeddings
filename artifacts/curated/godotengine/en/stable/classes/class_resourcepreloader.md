# ResourcePreloader

Inherits: Node < Object

A node used to preload sub-resources inside a scene.

## Description

This node is used to preload sub-resources inside a scene, so when the scene
is loaded, all the resources are ready to use and can be retrieved from the
preloader. You can add the resources using the ResourcePreloader tab when the
node is selected.

GDScript has a simplified @GDScript.preload() built-in method which can be
used in most situations, leaving the use of ResourcePreloader for more
advanced scenarios.

## Methods

void | add_resource(name: StringName, resource: Resource)  
---|---  
Resource | get_resource(name: StringName) const  
PackedStringArray | get_resource_list() const  
bool | has_resource(name: StringName) const  
void | remove_resource(name: StringName)  
void | rename_resource(name: StringName, newname: StringName)  
  
## Method Descriptions

void add_resource(name: StringName, resource: Resource)

Adds a resource to the preloader with the given `name`. If a resource with the
given `name` already exists, the new resource will be renamed to "`name` N"
where N is an incrementing number starting from 2.

Resource get_resource(name: StringName) const

Returns the resource associated to `name`.

PackedStringArray get_resource_list() const

Returns the list of resources inside the preloader.

bool has_resource(name: StringName) const

Returns `true` if the preloader contains a resource associated to `name`.

void remove_resource(name: StringName)

Removes the resource associated to `name` from the preloader.

void rename_resource(name: StringName, newname: StringName)

Renames a resource inside the preloader from `name` to `newname`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

