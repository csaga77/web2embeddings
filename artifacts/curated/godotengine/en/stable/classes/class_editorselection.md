# EditorSelection

Inherits: Object

Manages the SceneTree selection in the editor.

## Description

This object manages the SceneTree selection in the editor.

Note: This class shouldn't be instantiated directly. Instead, access the
singleton using EditorInterface.get_selection().

## Methods

void | add_node(node: Node)  
---|---  
void | clear()  
Array[Node] | get_selected_nodes()  
Array[Node] | get_transformable_selected_nodes()  
void | remove_node(node: Node)  
  
## Signals

selection_changed()

Emitted when the selection changes.

## Method Descriptions

void add_node(node: Node)

Adds a node to the selection.

Note: The newly selected node will not be automatically edited in the
inspector. If you want to edit a node, use EditorInterface.edit_node().

void clear()

Clear the selection.

Array[Node] get_selected_nodes()

Returns the list of selected nodes.

Array[Node] get_transformable_selected_nodes()

Returns the list of selected nodes, optimized for transform operations (i.e.
moving them, rotating, etc.). This list can be used to avoid situations where
a node is selected and is also a child/grandchild.

void remove_node(node: Node)

Removes a node from the selection.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

