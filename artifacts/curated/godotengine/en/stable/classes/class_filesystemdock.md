# FileSystemDock

Inherits: VBoxContainer < BoxContainer < Container < Control < CanvasItem <
Node < Object

Godot editor's dock for managing files in the project.

## Description

This class is available only in EditorPlugins and can't be instantiated. You
can access it using EditorInterface.get_file_system_dock().

While FileSystemDock doesn't expose any methods for file manipulation, it can
listen for various file-related signals.

## Methods

void | add_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)  
---|---  
void | navigate_to_path(path: String)  
void | remove_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)  
  
## Signals

display_mode_changed()

Emitted when the user switches file display mode or split mode.

file_removed(file: String)

Emitted when the given `file` was removed.

files_moved(old_file: String, new_file: String)

Emitted when a file is moved from `old_file` path to `new_file` path.

folder_color_changed()

Emitted when folders change color.

folder_moved(old_folder: String, new_folder: String)

Emitted when a folder is moved from `old_folder` path to `new_folder` path.

folder_removed(folder: String)

Emitted when the given `folder` was removed.

inherit(file: String)

Emitted when a new scene is created that inherits the scene at `file` path.

instantiate(files: PackedStringArray)

Emitted when the given scenes are being instantiated in the editor.

resource_removed(resource: Resource)

Emitted when an external `resource` had its file removed.

## Method Descriptions

void add_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)

Registers a new EditorResourceTooltipPlugin.

void navigate_to_path(path: String)

Sets the given `path` as currently selected, ensuring that the selected
file/directory is visible.

void remove_resource_tooltip_plugin(plugin: EditorResourceTooltipPlugin)

Removes an EditorResourceTooltipPlugin. Fails if the plugin wasn't previously
added.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

