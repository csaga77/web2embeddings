# FileAccess

Inherits: RefCounted < Object

Provides methods for file reading and writing operations.

## Description

This class can be used to permanently store data in the user device's file
system and to read from it. This is useful for storing game save data or
player configuration files.

Here's a sample on how to write and read from a file:

GDScriptC#

    
    
    func save_to_file(content):
        var file = FileAccess.open("user://save_game.dat", FileAccess.WRITE)
        file.store_string(content)
    
    func load_from_file():
        var file = FileAccess.open("user://save_game.dat", FileAccess.READ)
        var content = file.get_as_text()
        return content
    
    
    
    public void SaveToFile(string content)
    {
        using var file = FileAccess.Open("user://save_game.dat", FileAccess.ModeFlags.Write);
        file.StoreString(content);
    }
    
    public string LoadFromFile()
    {
        using var file = FileAccess.Open("user://save_game.dat", FileAccess.ModeFlags.Read);
        string content = file.GetAsText();
        return content;
    }
    

In the example above, the file will be saved in the user data folder as
specified in the Data paths documentation.

FileAccess will close when it's freed, which happens when it goes out of scope
or when it gets assigned with `null`. close() can be used to close it before
then explicitly. In C# the reference must be disposed manually, which can be
done with the `using` statement or by calling the `Dispose` method directly.

Note: To access project resources once exported, it is recommended to use
ResourceLoader instead of FileAccess, as some files are converted to engine-
specific formats and their original source files might not be present in the
exported PCK package. If using FileAccess, make sure the file is included in
the export by changing its import mode to Keep File (exported as is) in the
Import dock, or, for files where this option is not available, change the non-
resource export filter in the Export dialog to include the file's extension
(e.g. `*.txt`).

Note: Files are automatically closed only if the process exits "normally"
(such as by clicking the window manager's close button or pressing Alt + F4).
If you stop the project execution by pressing F8 while the project is running,
the file won't be closed as the game process will be killed. You can work
around this by calling flush() at regular intervals.

## Tutorials

  * File system

  * Runtime file loading and saving

  * 3D Voxel Demo

## Properties

bool | big_endian  
---|---  
  
## Methods

void | close()  
---|---  
FileAccess | create_temp(mode_flags: int, prefix: String = "", extension: String = "", keep: bool = false) static  
bool | eof_reached() const  
bool | file_exists(path: String) static  
void | flush()  
int | get_8() const  
int | get_16() const  
int | get_32() const  
int | get_64() const  
String | get_as_text(skip_cr: bool = false) const  
PackedByteArray | get_buffer(length: int) const  
PackedStringArray | get_csv_line(delim: String = ",") const  
float | get_double() const  
Error | get_error() const  
PackedByteArray | get_file_as_bytes(path: String) static  
String | get_file_as_string(path: String) static  
float | get_float() const  
float | get_half() const  
bool | get_hidden_attribute(file: String) static  
int | get_length() const  
String | get_line() const  
String | get_md5(path: String) static  
int | get_modified_time(file: String) static  
Error | get_open_error() static  
String | get_pascal_string()  
String | get_path() const  
String | get_path_absolute() const  
int | get_position() const  
bool | get_read_only_attribute(file: String) static  
float | get_real() const  
String | get_sha256(path: String) static  
BitField[UnixPermissionFlags] | get_unix_permissions(file: String) static  
Variant | get_var(allow_objects: bool = false) const  
bool | is_open() const  
FileAccess | open(path: String, flags: ModeFlags) static  
FileAccess | open_compressed(path: String, mode_flags: ModeFlags, compression_mode: CompressionMode = 0) static  
FileAccess | open_encrypted(path: String, mode_flags: ModeFlags, key: PackedByteArray, iv: PackedByteArray = PackedByteArray()) static  
FileAccess | open_encrypted_with_pass(path: String, mode_flags: ModeFlags, pass: String) static  
Error | resize(length: int)  
void | seek(position: int)  
void | seek_end(position: int = 0)  
Error | set_hidden_attribute(file: String, hidden: bool) static  
Error | set_read_only_attribute(file: String, ro: bool) static  
Error | set_unix_permissions(file: String, permissions: BitField[UnixPermissionFlags]) static  
bool | store_8(value: int)  
bool | store_16(value: int)  
bool | store_32(value: int)  
bool | store_64(value: int)  
bool | store_buffer(buffer: PackedByteArray)  
bool | store_csv_line(values: PackedStringArray, delim: String = ",")  
bool | store_double(value: float)  
bool | store_float(value: float)  
bool | store_half(value: float)  
bool | store_line(line: String)  
bool | store_pascal_string(string: String)  
bool | store_real(value: float)  
bool | store_string(string: String)  
bool | store_var(value: Variant, full_objects: bool = false)  
  
## Enumerations

enum ModeFlags:

ModeFlags READ = `1`

Opens the file for read operations. The cursor is positioned at the beginning
of the file.

ModeFlags WRITE = `2`

Opens the file for write operations. The file is created if it does not exist,
and truncated if it does.

Note: When creating a file it must be in an already existing directory. To
recursively create directories for a file path, see
DirAccess.make_dir_recursive().

ModeFlags READ_WRITE = `3`

Opens the file for read and write operations. Does not truncate the file. The
cursor is positioned at the beginning of the file.

ModeFlags WRITE_READ = `7`

Opens the file for read and write operations. The file is created if it does
not exist, and truncated if it does. The cursor is positioned at the beginning
of the file.

Note: When creating a file it must be in an already existing directory. To
recursively create directories for a file path, see
DirAccess.make_dir_recursive().

enum CompressionMode:

CompressionMode COMPRESSION_FASTLZ = `0`

Uses the FastLZ compression method.

CompressionMode COMPRESSION_DEFLATE = `1`

Uses the DEFLATE compression method.

CompressionMode COMPRESSION_ZSTD = `2`

Uses the Zstandard compression method.

CompressionMode COMPRESSION_GZIP = `3`

Uses the gzip compression method.

CompressionMode COMPRESSION_BROTLI = `4`

Uses the brotli compression method (only decompression is supported).

flags UnixPermissionFlags:

UnixPermissionFlags UNIX_READ_OWNER = `256`

Read for owner bit.

UnixPermissionFlags UNIX_WRITE_OWNER = `128`

Write for owner bit.

UnixPermissionFlags UNIX_EXECUTE_OWNER = `64`

Execute for owner bit.

UnixPermissionFlags UNIX_READ_GROUP = `32`

Read for group bit.

UnixPermissionFlags UNIX_WRITE_GROUP = `16`

Write for group bit.

UnixPermissionFlags UNIX_EXECUTE_GROUP = `8`

Execute for group bit.

UnixPermissionFlags UNIX_READ_OTHER = `4`

Read for other bit.

UnixPermissionFlags UNIX_WRITE_OTHER = `2`

Write for other bit.

UnixPermissionFlags UNIX_EXECUTE_OTHER = `1`

Execute for other bit.

UnixPermissionFlags UNIX_SET_USER_ID = `2048`

Set user id on execution bit.

UnixPermissionFlags UNIX_SET_GROUP_ID = `1024`

Set group id on execution bit.

UnixPermissionFlags UNIX_RESTRICTED_DELETE = `512`

Restricted deletion (sticky) bit.

## Property Descriptions

bool big_endian

  * void set_big_endian(value: bool)

  * bool is_big_endian()

If `true`, the file is read with big-endian endianness. If `false`, the file
is read with little-endian endianness. If in doubt, leave this to `false` as
most files are written with little-endian endianness.

Note: big_endian is only about the file format, not the CPU type. The CPU
endianness doesn't affect the default endianness for files written.

Note: This is always reset to `false` whenever you open the file. Therefore,
you must set big_endian after opening the file, not before.

## Method Descriptions

void close()

Closes the currently opened file and prevents subsequent read/write
operations. Use flush() to persist the data to disk without closing the file.

Note: FileAccess will automatically close when it's freed, which happens when
it goes out of scope or when it gets assigned with `null`. In C# the reference
must be disposed after we are done using it, this can be done with the `using`
statement or calling the `Dispose` method directly.

FileAccess create_temp(mode_flags: int, prefix: String = "", extension: String
= "", keep: bool = false) static

Creates a temporary file. This file will be freed when the returned FileAccess
is freed.

If `prefix` is not empty, it will be prefixed to the file name, separated by a
`-`.

If `extension` is not empty, it will be appended to the temporary file name.

If `keep` is `true`, the file is not deleted when the returned FileAccess is
freed.

Returns `null` if opening the file failed. You can use get_open_error() to
check the error that occurred.

bool eof_reached() const

Returns `true` if the file cursor has already read past the end of the file.

Note: `eof_reached() == false` cannot be used to check whether there is more
data available. To loop while there is more data available, use:

GDScriptC#

    
    
    while file.get_position() < file.get_length():
        # Read data
    
    
    
    while (file.GetPosition() < file.GetLength())
    {
        // Read data
    }
    

bool file_exists(path: String) static

Returns `true` if the file exists in the given path.

Note: Many resources types are imported (e.g. textures or sound files), and
their source asset will not be included in the exported game, as only the
imported version is used. See ResourceLoader.exists() for an alternative
approach that takes resource remapping into account.

For a non-static, relative equivalent, use DirAccess.file_exists().

void flush()

Writes the file's buffer to disk. Flushing is automatically performed when the
file is closed. This means you don't need to call flush() manually before
closing a file. Still, calling flush() can be used to ensure the data is safe
even if the project crashes instead of being closed gracefully.

Note: Only call flush() when you actually need it. Otherwise, it will decrease
performance due to constant disk writes.

int get_8() const

Returns the next 8 bits from the file as an integer. See store_8() for details
on what values can be stored and retrieved this way.

int get_16() const

Returns the next 16 bits from the file as an integer. See store_16() for
details on what values can be stored and retrieved this way.

int get_32() const

Returns the next 32 bits from the file as an integer. See store_32() for
details on what values can be stored and retrieved this way.

int get_64() const

Returns the next 64 bits from the file as an integer. See store_64() for
details on what values can be stored and retrieved this way.

String get_as_text(skip_cr: bool = false) const

Returns the whole file as a String. Text is interpreted as being UTF-8
encoded.

If `skip_cr` is `true`, carriage return characters (`\r`, CR) will be ignored
when parsing the UTF-8, so that only line feed characters (`\n`, LF) represent
a new line (Unix convention).

PackedByteArray get_buffer(length: int) const

Returns next `length` bytes of the file as a PackedByteArray.

PackedStringArray get_csv_line(delim: String = ",") const

Returns the next value of the file in CSV (Comma-Separated Values) format. You
can pass a different delimiter `delim` to use other than the default `","`
(comma). This delimiter must be one-character long, and cannot be a double
quotation mark.

Text is interpreted as being UTF-8 encoded. Text values must be enclosed in
double quotes if they include the delimiter character. Double quotes within a
text value can be escaped by doubling their occurrence.

For example, the following CSV lines are valid and will be properly parsed as
two strings each:

    
    
    Alice,"Hello, Bob!"
    Bob,Alice! What a surprise!
    Alice,"I thought you'd reply with ""Hello, world""."
    

Note how the second line can omit the enclosing quotes as it does not include
the delimiter. However it could very well use quotes, it was only written
without for demonstration purposes. The third line must use `""` for each
quotation mark that needs to be interpreted as such instead of the end of a
text value.

float get_double() const

Returns the next 64 bits from the file as a floating-point number.

Error get_error() const

Returns the last error that happened when trying to perform operations.
Compare with the `ERR_FILE_*` constants from Error.

PackedByteArray get_file_as_bytes(path: String) static

Returns the whole `path` file contents as a PackedByteArray without any
decoding.

Returns an empty PackedByteArray if an error occurred while opening the file.
You can use get_open_error() to check the error that occurred.

String get_file_as_string(path: String) static

Returns the whole `path` file contents as a String. Text is interpreted as
being UTF-8 encoded.

Returns an empty String if an error occurred while opening the file. You can
use get_open_error() to check the error that occurred.

float get_float() const

Returns the next 32 bits from the file as a floating-point number.

float get_half() const

Returns the next 16 bits from the file as a half-precision floating-point
number.

bool get_hidden_attribute(file: String) static

Returns `true`, if file `hidden` attribute is set.

Note: This method is implemented on iOS, BSD, macOS, and Windows.

int get_length() const

Returns the size of the file in bytes. For a pipe, returns the number of bytes
available for reading from the pipe.

String get_line() const

Returns the next line of the file as a String. The returned string doesn't
include newline (`\n`) or carriage return (`\r`) characters, but does include
any other leading or trailing whitespace.

Text is interpreted as being UTF-8 encoded.

String get_md5(path: String) static

Returns an MD5 String representing the file at the given path or an empty
String on failure.

int get_modified_time(file: String) static

Returns the last time the `file` was modified in Unix timestamp format, or `0`
on error. This Unix timestamp can be converted to another format using the
Time singleton.

Error get_open_error() static

Returns the result of the last open() call in the current thread.

String get_pascal_string()

Returns a String saved in Pascal format from the file.

Text is interpreted as being UTF-8 encoded.

String get_path() const

Returns the path as a String for the current open file.

String get_path_absolute() const

Returns the absolute path as a String for the current open file.

int get_position() const

Returns the file cursor's position.

bool get_read_only_attribute(file: String) static

Returns `true`, if file `read only` attribute is set.

Note: This method is implemented on iOS, BSD, macOS, and Windows.

float get_real() const

Returns the next bits from the file as a floating-point number.

String get_sha256(path: String) static

Returns an SHA-256 String representing the file at the given path or an empty
String on failure.

BitField[UnixPermissionFlags] get_unix_permissions(file: String) static

Returns file UNIX permissions.

Note: This method is implemented on iOS, Linux/BSD, and macOS.

Variant get_var(allow_objects: bool = false) const

Returns the next Variant value from the file. If `allow_objects` is `true`,
decoding objects is allowed.

Internally, this uses the same decoding mechanism as the
@GlobalScope.bytes_to_var() method.

Warning: Deserialized objects can contain code which gets executed. Do not use
this option if the serialized object comes from untrusted sources to avoid
potential security threats such as remote code execution.

bool is_open() const

Returns `true` if the file is currently opened.

FileAccess open(path: String, flags: ModeFlags) static

Creates a new FileAccess object and opens the file for writing or reading,
depending on the flags.

Returns `null` if opening the file failed. You can use get_open_error() to
check the error that occurred.

FileAccess open_compressed(path: String, mode_flags: ModeFlags,
compression_mode: CompressionMode = 0) static

Creates a new FileAccess object and opens a compressed file for reading or
writing.

Note: open_compressed() can only read files that were saved by Godot, not
third-party compression formats. See GitHub issue #28999 for a workaround.

Returns `null` if opening the file failed. You can use get_open_error() to
check the error that occurred.

FileAccess open_encrypted(path: String, mode_flags: ModeFlags, key:
PackedByteArray, iv: PackedByteArray = PackedByteArray()) static

Creates a new FileAccess object and opens an encrypted file in write or read
mode. You need to pass a binary key to encrypt/decrypt it.

Note: The provided key must be 32 bytes long.

Returns `null` if opening the file failed. You can use get_open_error() to
check the error that occurred.

FileAccess open_encrypted_with_pass(path: String, mode_flags: ModeFlags, pass:
String) static

Creates a new FileAccess object and opens an encrypted file in write or read
mode. You need to pass a password to encrypt/decrypt it.

Returns `null` if opening the file failed. You can use get_open_error() to
check the error that occurred.

Error resize(length: int)

Resizes the file to a specified length. The file must be open in a mode that
permits writing. If the file is extended, NUL characters are appended. If the
file is truncated, all data from the end file to the original length of the
file is lost.

void seek(position: int)

Changes the file reading/writing cursor to the specified position (in bytes
from the beginning of the file).

void seek_end(position: int = 0)

Changes the file reading/writing cursor to the specified position (in bytes
from the end of the file).

Note: This is an offset, so you should use negative numbers or the cursor will
be at the end of the file.

Error set_hidden_attribute(file: String, hidden: bool) static

Sets file hidden attribute.

Note: This method is implemented on iOS, BSD, macOS, and Windows.

Error set_read_only_attribute(file: String, ro: bool) static

Sets file read only attribute.

Note: This method is implemented on iOS, BSD, macOS, and Windows.

Error set_unix_permissions(file: String, permissions:
BitField[UnixPermissionFlags]) static

Sets file UNIX permissions.

Note: This method is implemented on iOS, Linux/BSD, and macOS.

bool store_8(value: int)

Stores an integer as 8 bits in the file.

Note: The `value` should lie in the interval `[0, 255]`. Any other value will
overflow and wrap around.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

To store a signed integer, use store_64(), or convert it manually (see
store_16() for an example).

bool store_16(value: int)

Stores an integer as 16 bits in the file.

Note: The `value` should lie in the interval `[0, 2^16 - 1]`. Any other value
will overflow and wrap around.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

To store a signed integer, use store_64() or store a signed integer from the
interval `[-2^15, 2^15 - 1]` (i.e. keeping one bit for the signedness) and
compute its sign manually when reading. For example:

GDScriptC#

    
    
    const MAX_15B = 1 << 15
    const MAX_16B = 1 << 16
    
    func unsigned16_to_signed(unsigned):
        return (unsigned + MAX_15B) % MAX_16B - MAX_15B
    
    func _ready():
        var f = FileAccess.open("user://file.dat", FileAccess.WRITE_READ)
        f.store_16(-42) # This wraps around and stores 65494 (2^16 - 42).
        f.store_16(121) # In bounds, will store 121.
        f.seek(0) # Go back to start to read the stored value.
        var read1 = f.get_16() # 65494
        var read2 = f.get_16() # 121
        var converted1 = unsigned16_to_signed(read1) # -42
        var converted2 = unsigned16_to_signed(read2) # 121
    
    
    
    public override void _Ready()
    {
        using var f = FileAccess.Open("user://file.dat", FileAccess.ModeFlags.WriteRead);
        f.Store16(unchecked((ushort)-42)); // This wraps around and stores 65494 (2^16 - 42).
        f.Store16(121); // In bounds, will store 121.
        f.Seek(0); // Go back to start to read the stored value.
        ushort read1 = f.Get16(); // 65494
        ushort read2 = f.Get16(); // 121
        short converted1 = (short)read1; // -42
        short converted2 = (short)read2; // 121
    }
    

bool store_32(value: int)

Stores an integer as 32 bits in the file.

Note: The `value` should lie in the interval `[0, 2^32 - 1]`. Any other value
will overflow and wrap around.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

To store a signed integer, use store_64(), or convert it manually (see
store_16() for an example).

bool store_64(value: int)

Stores an integer as 64 bits in the file.

Note: The `value` must lie in the interval `[-2^63, 2^63 - 1]` (i.e. be a
valid int value).

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_buffer(buffer: PackedByteArray)

Stores the given array of bytes in the file.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_csv_line(values: PackedStringArray, delim: String = ",")

Store the given PackedStringArray in the file as a line formatted in the CSV
(Comma-Separated Values) format. You can pass a different delimiter `delim` to
use other than the default `","` (comma). This delimiter must be one-character
long.

Text will be encoded as UTF-8.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_double(value: float)

Stores a floating-point number as 64 bits in the file.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_float(value: float)

Stores a floating-point number as 32 bits in the file.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_half(value: float)

Stores a half-precision floating-point number as 16 bits in the file.

bool store_line(line: String)

Stores `line` in the file followed by a newline character (`\n`), encoding the
text as UTF-8.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_pascal_string(string: String)

Stores the given String as a line in the file in Pascal format (i.e. also
store the length of the string).

Text will be encoded as UTF-8.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_real(value: float)

Stores a floating-point number in the file.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_string(string: String)

Stores `string` in the file without a newline character (`\n`), encoding the
text as UTF-8.

Note: This method is intended to be used to write text files. The string is
stored as a UTF-8 encoded buffer without string length or terminating zero,
which means that it can't be loaded back easily. If you want to store a
retrievable string in a binary file, consider using store_pascal_string()
instead. For retrieving strings from a text file, you can use
`get_buffer(length).get_string_from_utf8()` (if you know the length) or
get_as_text().

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

bool store_var(value: Variant, full_objects: bool = false)

Stores any Variant value in the file. If `full_objects` is `true`, encoding
objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the
@GlobalScope.var_to_bytes() method.

Note: Not all properties are included. Only properties that are configured
with the @GlobalScope.PROPERTY_USAGE_STORAGE flag set will be serialized. You
can add a new usage flag to a property by overriding the
Object._get_property_list() method in your class. You can also check how
property usage is configured by calling Object._get_property_list(). See
PropertyUsageFlags for the possible usage flags.

Note: If an error occurs, the resulting value of the file position indicator
is indeterminate.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[BitField]: This value is an integer composed as a bitmask of the following flags.

