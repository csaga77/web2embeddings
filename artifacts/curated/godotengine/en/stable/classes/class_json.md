# JSON

Inherits: Resource < RefCounted < Object

Helper class for creating and parsing JSON data.

## Description

The JSON class enables all data types to be converted to and from a JSON
string. This is useful for serializing data, e.g. to save to a file or send
over the network.

stringify() is used to convert any data type into a JSON string.

parse() is used to convert any existing JSON data into a Variant that can be
used within Godot. If successfully parsed, use data to retrieve the Variant,
and use @GlobalScope.typeof() to check if the Variant's type is what you
expect. JSON Objects are converted into a Dictionary, but JSON data can be
used to store Arrays, numbers, Strings and even just a boolean.

    
    
    var data_to_send = ["a", "b", "c"]
    var json_string = JSON.stringify(data_to_send)
    # Save data
    # ...
    # Retrieve data
    var json = JSON.new()
    var error = json.parse(json_string)
    if error == OK:
        var data_received = json.data
        if typeof(data_received) == TYPE_ARRAY:
            print(data_received) # Prints the array.
        else:
            print("Unexpected data")
    else:
        print("JSON Parse Error: ", json.get_error_message(), " in ", json_string, " at line ", json.get_error_line())
    

Alternatively, you can parse strings using the static parse_string() method,
but it doesn't handle errors.

    
    
    var data = JSON.parse_string(json_string) # Returns null if parsing failed.
    

Note: Both parse methods do not fully comply with the JSON specification:

  * Trailing commas in arrays or objects are ignored, instead of causing a parser error.

  * New line and tab characters are accepted in string literals, and are treated like their corresponding escape sequences `\n` and `\t`.

  * Numbers are parsed using String.to_float() which is generally more lax than the JSON specification.

  * Certain errors, such as invalid Unicode sequences, do not cause a parser error. Instead, the string is cleaned up and an error is logged to the console.

## Properties

Variant | data | `null`  
---|---|---  
  
## Methods

Variant | from_native(variant: Variant, full_objects: bool = false) static  
---|---  
int | get_error_line() const  
String | get_error_message() const  
String | get_parsed_text() const  
Error | parse(json_text: String, keep_text: bool = false)  
Variant | parse_string(json_string: String) static  
String | stringify(data: Variant, indent: String = "", sort_keys: bool = true, full_precision: bool = false) static  
Variant | to_native(json: Variant, allow_objects: bool = false) static  
  
## Property Descriptions

Variant data = `null`

  * void set_data(value: Variant)

  * Variant get_data()

Contains the parsed JSON data in Variant form.

## Method Descriptions

Variant from_native(variant: Variant, full_objects: bool = false) static

Converts a native engine type to a JSON-compliant value.

By default, objects are ignored for security reasons, unless `full_objects` is
`true`.

You can convert a native value to a JSON string like this:

    
    
    func encode_data(value, full_objects = false):
        return JSON.stringify(JSON.from_native(value, full_objects))
    

int get_error_line() const

Returns `0` if the last call to parse() was successful, or the line number
where the parse failed.

String get_error_message() const

Returns an empty string if the last call to parse() was successful, or the
error message if it failed.

String get_parsed_text() const

Return the text parsed by parse() (requires passing `keep_text` to parse()).

Error parse(json_text: String, keep_text: bool = false)

Attempts to parse the `json_text` provided.

Returns an Error. If the parse was successful, it returns @GlobalScope.OK and
the result can be retrieved using data. If unsuccessful, use get_error_line()
and get_error_message() to identify the source of the failure.

Non-static variant of parse_string(), if you want custom error handling.

The optional `keep_text` argument instructs the parser to keep a copy of the
original text. This text can be obtained later by using the get_parsed_text()
function and is used when saving the resource (instead of generating new text
from data).

Variant parse_string(json_string: String) static

Attempts to parse the `json_string` provided and returns the parsed data.
Returns `null` if parse failed.

String stringify(data: Variant, indent: String = "", sort_keys: bool = true,
full_precision: bool = false) static

Converts a Variant var to JSON text and returns the result. Useful for
serializing data to store or send over the network.

Note: The JSON specification does not define integer or float types, but only
a number type. Therefore, converting a Variant to JSON text will convert all
numerical values to float types.

Note: If `full_precision` is `true`, when stringifying floats, the unreliable
digits are stringified in addition to the reliable digits to guarantee exact
decoding.

The `indent` parameter controls if and how something is indented; its contents
will be used where there should be an indent in the output. Even spaces like
`" "` will work. `\t` and `\n` can also be used for a tab indent, or to make a
newline for each indent respectively.

Example output:

    
    
    ## JSON.stringify(my_dictionary)
    {"name":"my_dictionary","version":"1.0.0","entities":[{"name":"entity_0","value":"value_0"},{"name":"entity_1","value":"value_1"}]}
    
    ## JSON.stringify(my_dictionary, "\t")
    {
        "name": "my_dictionary",
        "version": "1.0.0",
        "entities": [
            {
                "name": "entity_0",
                "value": "value_0"
            },
            {
                "name": "entity_1",
                "value": "value_1"
            }
        ]
    }
    
    ## JSON.stringify(my_dictionary, "...")
    {
    ..."name": "my_dictionary",
    ..."version": "1.0.0",
    ..."entities": [
    ......{
    ........."name": "entity_0",
    ........."value": "value_0"
    ......},
    ......{
    ........."name": "entity_1",
    ........."value": "value_1"
    ......}
    ...]
    }
    

Variant to_native(json: Variant, allow_objects: bool = false) static

Converts a JSON-compliant value that was created with from_native() back to
native engine types.

By default, objects are ignored for security reasons, unless `allow_objects`
is `true`.

You can convert a JSON string back to a native value like this:

    
    
    func decode_data(string, allow_objects = false):
        return JSON.to_native(JSON.parse_string(string), allow_objects)
    

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

