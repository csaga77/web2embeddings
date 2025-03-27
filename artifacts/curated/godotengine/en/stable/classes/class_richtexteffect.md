# RichTextEffect

Inherits: Resource < RefCounted < Object

A custom effect for a RichTextLabel.

## Description

A custom effect for a RichTextLabel, which can be loaded in the RichTextLabel
inspector or using RichTextLabel.install_effect().

Note: For a RichTextEffect to be usable, a BBCode tag must be defined as a
member variable called `bbcode` in the script.

GDScriptC#

    
    
    # The RichTextEffect will be usable like this: `[example]Some text[/example]`
    var bbcode = "example"
    
    
    
    // The RichTextEffect will be usable like this: `[example]Some text[/example]`
    string bbcode = "example";
    

Note: As soon as a RichTextLabel contains at least one RichTextEffect, it will
continuously process the effect unless the project is paused. This may impact
battery life negatively.

## Tutorials

  * BBCode in RichTextLabel

  * RichTextEffect test project (third-party)

## Methods

bool | _process_custom_fx(char_fx: CharFXTransform) virtual const  
---|---  
  
## Method Descriptions

bool _process_custom_fx(char_fx: CharFXTransform) virtual const

Override this method to modify properties in `char_fx`. The method must return
`true` if the character could be transformed successfully. If the method
returns `false`, it will skip transformation to avoid displaying broken text.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

