# RDSamplerState

Inherits: RefCounted < Object

Sampler state (used by RenderingDevice).

## Description

This object is used by RenderingDevice.

## Properties

float | anisotropy_max | `1.0`  
---|---|---  
SamplerBorderColor | border_color | `2`  
CompareOperator | compare_op | `7`  
bool | enable_compare | `false`  
float | lod_bias | `0.0`  
SamplerFilter | mag_filter | `0`  
float | max_lod | `1e+20`  
SamplerFilter | min_filter | `0`  
float | min_lod | `0.0`  
SamplerFilter | mip_filter | `0`  
SamplerRepeatMode | repeat_u | `2`  
SamplerRepeatMode | repeat_v | `2`  
SamplerRepeatMode | repeat_w | `2`  
bool | unnormalized_uvw | `false`  
bool | use_anisotropy | `false`  
  
## Property Descriptions

float anisotropy_max = `1.0`

  * void set_anisotropy_max(value: float)

  * float get_anisotropy_max()

Maximum anisotropy that can be used when sampling. Only effective if
use_anisotropy is `true`. Higher values result in a sharper sampler at oblique
angles, at the cost of performance (due to memory bandwidth). This value may
be limited by the graphics hardware in use. Most graphics hardware only
supports values up to `16.0`.

If anisotropy_max is `1.0`, forcibly disables anisotropy even if
use_anisotropy is `true`.

SamplerBorderColor border_color = `2`

  * void set_border_color(value: SamplerBorderColor)

  * SamplerBorderColor get_border_color()

The border color that will be returned when sampling outside the sampler's
bounds and the repeat_u, repeat_v or repeat_w modes have repeating disabled.

CompareOperator compare_op = `7`

  * void set_compare_op(value: CompareOperator)

  * CompareOperator get_compare_op()

The compare operation to use. Only effective if enable_compare is `true`.

bool enable_compare = `false`

  * void set_enable_compare(value: bool)

  * bool get_enable_compare()

If `true`, returned values will be based on the comparison operation defined
in compare_op. This is a hardware-based approach and is therefore faster than
performing this manually in a shader. For example, compare operations are used
for shadow map rendering by comparing depth values from a shadow sampler.

float lod_bias = `0.0`

  * void set_lod_bias(value: float)

  * float get_lod_bias()

The mipmap LOD bias to use. Positive values will make the sampler blurrier at
a given distance, while negative values will make the sampler sharper at a
given distance (at the risk of looking grainy). Recommended values are between
`-0.5` and `0.0`. Only effective if the sampler has mipmaps available.

SamplerFilter mag_filter = `0`

  * void set_mag_filter(value: SamplerFilter)

  * SamplerFilter get_mag_filter()

The sampler's magnification filter. It is the filtering method used when
sampling texels that appear bigger than on-screen pixels.

float max_lod = `1e+20`

  * void set_max_lod(value: float)

  * float get_max_lod()

The maximum mipmap LOD bias to display (lowest resolution). Only effective if
the sampler has mipmaps available.

SamplerFilter min_filter = `0`

  * void set_min_filter(value: SamplerFilter)

  * SamplerFilter get_min_filter()

The sampler's minification filter. It is the filtering method used when
sampling texels that appear smaller than on-screen pixels.

float min_lod = `0.0`

  * void set_min_lod(value: float)

  * float get_min_lod()

The minimum mipmap LOD bias to display (highest resolution). Only effective if
the sampler has mipmaps available.

SamplerFilter mip_filter = `0`

  * void set_mip_filter(value: SamplerFilter)

  * SamplerFilter get_mip_filter()

The filtering method to use for mipmaps.

SamplerRepeatMode repeat_u = `2`

  * void set_repeat_u(value: SamplerRepeatMode)

  * SamplerRepeatMode get_repeat_u()

The repeat mode to use along the U axis of UV coordinates. This affects the
returned values if sampling outside the UV bounds.

SamplerRepeatMode repeat_v = `2`

  * void set_repeat_v(value: SamplerRepeatMode)

  * SamplerRepeatMode get_repeat_v()

The repeat mode to use along the V axis of UV coordinates. This affects the
returned values if sampling outside the UV bounds.

SamplerRepeatMode repeat_w = `2`

  * void set_repeat_w(value: SamplerRepeatMode)

  * SamplerRepeatMode get_repeat_w()

The repeat mode to use along the W axis of UV coordinates. This affects the
returned values if sampling outside the UV bounds. Only effective for 3D
samplers.

bool unnormalized_uvw = `false`

  * void set_unnormalized_uvw(value: bool)

  * bool get_unnormalized_uvw()

If `true`, the texture will be sampled with coordinates ranging from 0 to the
texture's resolution. Otherwise, the coordinates will be normalized and range
from 0 to 1.

bool use_anisotropy = `false`

  * void set_use_anisotropy(value: bool)

  * bool get_use_anisotropy()

If `true`, perform anisotropic sampling. See anisotropy_max.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

