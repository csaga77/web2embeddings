# MissingNode

Inherits: Node < Object

An internal editor class intended for keeping the data of unrecognized nodes.

## Description

This is an internal editor class intended for keeping data of nodes of unknown
type (most likely this type was supplied by an extension that is no longer
loaded). It can't be manually instantiated or placed in a scene.

Warning: Ignore missing nodes unless you know what you are doing. Existing
properties on a missing node can be freely modified in code, regardless of the
type they are intended to be.

## Properties

String | original_class  
---|---  
String | original_scene  
bool | recording_properties  
  
## Property Descriptions

String original_class

  * void set_original_class(value: String)

  * String get_original_class()

The name of the class this node was supposed to be (see Object.get_class()).

String original_scene

  * void set_original_scene(value: String)

  * String get_original_scene()

Returns the path of the scene this node was instance of originally.

bool recording_properties

  * void set_recording_properties(value: bool)

  * bool is_recording_properties()

If `true`, allows new properties to be set along with existing ones. If
`false`, only existing properties' values can be set, and new properties
cannot be added.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

