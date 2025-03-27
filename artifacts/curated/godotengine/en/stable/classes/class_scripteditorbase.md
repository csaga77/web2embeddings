# ScriptEditorBase

Inherits: VBoxContainer < BoxContainer < Container < Control < CanvasItem <
Node < Object

Base editor for editing scripts in the ScriptEditor.

## Description

Base editor for editing scripts in the ScriptEditor. This does not include
documentation items.

## Methods

void | add_syntax_highlighter(highlighter: EditorSyntaxHighlighter)  
---|---  
Control | get_base_editor() const  
  
## Signals

edited_script_changed()

Emitted after script validation.

go_to_help(what: String)

Emitted when the user requests a specific documentation page.

go_to_method(script: Object, method: String)

Emitted when the user requests to view a specific method of a script, similar
to request_open_script_at_line.

name_changed()

Emitted after script validation or when the edited resource has changed.

replace_in_files_requested(text: String)

Emitted when the user request to find and replace text in the file system.

request_help(topic: String)

Emitted when the user requests contextual help.

request_open_script_at_line(script: Object, line: int)

Emitted when the user requests to view a specific line of a script, similar to
go_to_method.

request_save_history()

Emitted when the user contextual goto and the item is in the same script.

request_save_previous_state(state: Dictionary)

Emitted when the user changes current script or moves caret by 10 or more
columns within the same script.

search_in_files_requested(text: String)

Emitted when the user request to search text in the file system.

## Method Descriptions

void add_syntax_highlighter(highlighter: EditorSyntaxHighlighter)

Adds a EditorSyntaxHighlighter to the open script.

Control get_base_editor() const

Returns the underlying Control used for editing scripts. For text scripts,
this is a CodeEdit.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

