# AudioEffectSpectrumAnalyzer

Inherits: AudioEffect < Resource < RefCounted < Object

Audio effect that can be used for real-time audio visualizations.

## Description

This audio effect does not affect sound output, but can be used for real-time
audio visualizations.

This resource configures an AudioEffectSpectrumAnalyzerInstance, which
performs the actual analysis at runtime. An instance can be obtained with
AudioServer.get_bus_effect_instance().

See also AudioStreamGenerator for procedurally generating sounds.

## Tutorials

  * Audio Spectrum Visualizer Demo

## Properties

float | buffer_length | `2.0`  
---|---|---  
FFTSize | fft_size | `2`  
float | tap_back_pos | `0.01`  
  
## Enumerations

enum FFTSize:

FFTSize FFT_SIZE_256 = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency,
but least stable over time.

FFTSize FFT_SIZE_512 = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but
less stable over time.

FFTSize FFT_SIZE_1024 = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a
compromise between latency and stability over time.

FFTSize FFT_SIZE_2048 = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but
stable over time.

FFTSize FFT_SIZE_4096 = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency,
but most stable over time.

FFTSize FFT_SIZE_MAX = `5`

Represents the size of the FFTSize enum.

## Property Descriptions

float buffer_length = `2.0`

  * void set_buffer_length(value: float)

  * float get_buffer_length()

The length of the buffer to keep (in seconds). Higher values keep data around
for longer, but require more memory.

FFTSize fft_size = `2`

  * void set_fft_size(value: FFTSize)

  * FFTSize get_fft_size()

The size of the Fast Fourier transform buffer. Higher values smooth out the
spectrum analysis over time, but have greater latency. The effects of this
higher latency are especially noticeable with sudden amplitude changes.

float tap_back_pos = `0.01`

  * void set_tap_back_pos(value: float)

  * float get_tap_back_pos()

There is currently no description for this property. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

