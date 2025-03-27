# OptimizedTranslation

Inherits: Translation < Resource < RefCounted < Object

An optimized translation, used by default for CSV Translations.

## Description

An optimized translation, used by default for CSV Translations. Uses real-time
compressed translations, which results in very small dictionaries.

## Methods

void | generate(from: Translation)  
---|---  
  
## Method Descriptions

void generate(from: Translation)

Generates and sets an optimized translation from the given Translation
resource.

Note: This method is intended to be used in the editor. It does nothing when
called from an exported project.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

