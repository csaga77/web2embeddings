# PortableCompressedTexture2D

Inherits: Texture2D < Texture < Resource < RefCounted < Object

Provides a compressed texture for disk and/or VRAM in a way that is portable.

## Description

This class allows storing compressed textures as self contained (not imported)
resources.

For 2D usage (compressed on disk, uncompressed on VRAM), the lossy and
lossless modes are recommended. For 3D usage (compressed on VRAM) it depends
on the target platform.

If you intend to only use desktop, S3TC or BPTC are recommended. For only
mobile, ETC2 is recommended.

For portable, self contained 3D textures that work on both desktop and mobile,
Basis Universal is recommended (although it has a small quality cost and
longer compression time as a tradeoff).

This resource is intended to be created from code.

## Properties

bool | keep_compressed_buffer | `false`  
---|---|---  
bool | resource_local_to_scene | `false` (overrides Resource)  
Vector2 | size_override | `Vector2(0, 0)`  
  
## Methods

void | create_from_image(image: Image, compression_mode: CompressionMode, normal_map: bool = false, lossy_quality: float = 0.8)  
---|---  
CompressionMode | get_compression_mode() const  
Format | get_format() const  
bool | is_keeping_all_compressed_buffers() static  
void | set_keep_all_compressed_buffers(keep: bool) static  
  
## Enumerations

enum CompressionMode:

CompressionMode COMPRESSION_MODE_LOSSLESS = `0`

There is currently no description for this enum. Please help us by
contributing one!

CompressionMode COMPRESSION_MODE_LOSSY = `1`

There is currently no description for this enum. Please help us by
contributing one!

CompressionMode COMPRESSION_MODE_BASIS_UNIVERSAL = `2`

There is currently no description for this enum. Please help us by
contributing one!

CompressionMode COMPRESSION_MODE_S3TC = `3`

There is currently no description for this enum. Please help us by
contributing one!

CompressionMode COMPRESSION_MODE_ETC2 = `4`

There is currently no description for this enum. Please help us by
contributing one!

CompressionMode COMPRESSION_MODE_BPTC = `5`

There is currently no description for this enum. Please help us by
contributing one!

## Property Descriptions

bool keep_compressed_buffer = `false`

  * void set_keep_compressed_buffer(value: bool)

  * bool is_keeping_compressed_buffer()

When running on the editor, this class will keep the source compressed data in
memory. Otherwise, the source compressed data is lost after loading and the
resource can't be re saved.

This flag allows to keep the compressed data in memory if you intend it to
persist after loading.

Vector2 size_override = `Vector2(0, 0)`

  * void set_size_override(value: Vector2)

  * Vector2 get_size_override()

Allow overriding the texture size (for 2D only).

## Method Descriptions

void create_from_image(image: Image, compression_mode: CompressionMode,
normal_map: bool = false, lossy_quality: float = 0.8)

Initializes the compressed texture from a base image. The compression mode
must be provided.

`normal_map` is recommended to ensure optimum quality if this image will be
used as a normal map.

If lossy compression is requested, the quality setting can optionally be
provided. This maps to Lossy WebP compression quality.

CompressionMode get_compression_mode() const

Return the compression mode used (valid after initialized).

Format get_format() const

Return the image format used (valid after initialized).

bool is_keeping_all_compressed_buffers() static

Return whether the flag is overridden for all textures of this type.

void set_keep_all_compressed_buffers(keep: bool) static

Overrides the flag globally for all textures of this type. This is used
primarily by the editor.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[static]: This method doesn't need an instance to be called, so it can be called directly using the class name.

