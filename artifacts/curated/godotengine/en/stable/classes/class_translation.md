# Translation

Inherits: Resource < RefCounted < Object

Inherited By: OptimizedTranslation

A language translation that maps a collection of strings to their individual
translations.

## Description

Translations are resources that can be loaded and unloaded on demand. They map
a collection of strings to their individual translations, and they also
provide convenience methods for pluralization.

## Tutorials

  * Internationalizing games

  * Locales

## Properties

String | locale | `"en"`  
---|---|---  
  
## Methods

StringName | _get_message(src_message: StringName, context: StringName) virtual const  
---|---  
StringName | _get_plural_message(src_message: StringName, src_plural_message: StringName, n: int, context: StringName) virtual const  
void | add_message(src_message: StringName, xlated_message: StringName, context: StringName = &"")  
void | add_plural_message(src_message: StringName, xlated_messages: PackedStringArray, context: StringName = &"")  
void | erase_message(src_message: StringName, context: StringName = &"")  
StringName | get_message(src_message: StringName, context: StringName = &"") const  
int | get_message_count() const  
PackedStringArray | get_message_list() const  
StringName | get_plural_message(src_message: StringName, src_plural_message: StringName, n: int, context: StringName = &"") const  
PackedStringArray | get_translated_message_list() const  
  
## Property Descriptions

String locale = `"en"`

  * void set_locale(value: String)

  * String get_locale()

The locale of the translation.

## Method Descriptions

StringName _get_message(src_message: StringName, context: StringName) virtual
const

Virtual method to override get_message().

StringName _get_plural_message(src_message: StringName, src_plural_message:
StringName, n: int, context: StringName) virtual const

Virtual method to override get_plural_message().

void add_message(src_message: StringName, xlated_message: StringName, context:
StringName = &"")

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or
differentiate polysemic words.

void add_plural_message(src_message: StringName, xlated_messages:
PackedStringArray, context: StringName = &"")

Adds a message involving plural translation if nonexistent, followed by its
translation.

An additional context could be used to specify the translation context or
differentiate polysemic words.

void erase_message(src_message: StringName, context: StringName = &"")

Erases a message.

StringName get_message(src_message: StringName, context: StringName = &"")
const

Returns a message's translation.

int get_message_count() const

Returns the number of existing messages.

PackedStringArray get_message_list() const

Returns all the messages (keys).

StringName get_plural_message(src_message: StringName, src_plural_message:
StringName, n: int, context: StringName = &"") const

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used
to guide the translation system to fetch the correct plural form for the
selected language.

PackedStringArray get_translated_message_list() const

Returns all the messages (translated text).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

