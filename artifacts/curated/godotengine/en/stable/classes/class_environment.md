# Environment

Inherits: Resource < RefCounted < Object

Resource for environment nodes (like WorldEnvironment) that define multiple
rendering options.

## Description

Resource for environment nodes (like WorldEnvironment) that define multiple
environment operations (such as background Sky or Color, ambient light, fog,
depth-of-field...). These parameters affect the final render of the scene. The
order of these operations is:

  * Depth of Field Blur

  * Glow

  * Tonemap (Auto Exposure)

  * Adjustments

## Tutorials

  * Environment and post-processing

  * High dynamic range lighting

  * 3D Material Testers Demo

  * Third Person Shooter (TPS) Demo

## Properties

float | adjustment_brightness | `1.0`  
---|---|---  
Texture | adjustment_color_correction  
float | adjustment_contrast | `1.0`  
bool | adjustment_enabled | `false`  
float | adjustment_saturation | `1.0`  
Color | ambient_light_color | `Color(0, 0, 0, 1)`  
float | ambient_light_energy | `1.0`  
float | ambient_light_sky_contribution | `1.0`  
AmbientSource | ambient_light_source | `0`  
int | background_camera_feed_id | `1`  
int | background_canvas_max_layer | `0`  
Color | background_color | `Color(0, 0, 0, 1)`  
float | background_energy_multiplier | `1.0`  
float | background_intensity | `30000.0`  
BGMode | background_mode | `0`  
float | fog_aerial_perspective | `0.0`  
float | fog_density | `0.01`  
float | fog_depth_begin | `10.0`  
float | fog_depth_curve | `1.0`  
float | fog_depth_end | `100.0`  
bool | fog_enabled | `false`  
float | fog_height | `0.0`  
float | fog_height_density | `0.0`  
Color | fog_light_color | `Color(0.518, 0.553, 0.608, 1)`  
float | fog_light_energy | `1.0`  
FogMode | fog_mode | `0`  
float | fog_sky_affect | `1.0`  
float | fog_sun_scatter | `0.0`  
GlowBlendMode | glow_blend_mode | `2`  
float | glow_bloom | `0.0`  
bool | glow_enabled | `false`  
float | glow_hdr_luminance_cap | `12.0`  
float | glow_hdr_scale | `2.0`  
float | glow_hdr_threshold | `1.0`  
float | glow_intensity | `0.8`  
float | glow_levels/1 | `0.0`  
float | glow_levels/2 | `0.0`  
float | glow_levels/3 | `1.0`  
float | glow_levels/4 | `0.0`  
float | glow_levels/5 | `1.0`  
float | glow_levels/6 | `0.0`  
float | glow_levels/7 | `0.0`  
Texture | glow_map  
float | glow_map_strength | `0.8`  
float | glow_mix | `0.05`  
bool | glow_normalized | `false`  
float | glow_strength | `1.0`  
ReflectionSource | reflected_light_source | `0`  
float | sdfgi_bounce_feedback | `0.5`  
float | sdfgi_cascade0_distance | `12.8`  
int | sdfgi_cascades | `4`  
bool | sdfgi_enabled | `false`  
float | sdfgi_energy | `1.0`  
float | sdfgi_max_distance | `204.8`  
float | sdfgi_min_cell_size | `0.2`  
float | sdfgi_normal_bias | `1.1`  
float | sdfgi_probe_bias | `1.1`  
bool | sdfgi_read_sky_light | `true`  
bool | sdfgi_use_occlusion | `false`  
SDFGIYScale | sdfgi_y_scale | `1`  
Sky | sky  
float | sky_custom_fov | `0.0`  
Vector3 | sky_rotation | `Vector3(0, 0, 0)`  
float | ssao_ao_channel_affect | `0.0`  
float | ssao_detail | `0.5`  
bool | ssao_enabled | `false`  
float | ssao_horizon | `0.06`  
float | ssao_intensity | `2.0`  
float | ssao_light_affect | `0.0`  
float | ssao_power | `1.5`  
float | ssao_radius | `1.0`  
float | ssao_sharpness | `0.98`  
bool | ssil_enabled | `false`  
float | ssil_intensity | `1.0`  
float | ssil_normal_rejection | `1.0`  
float | ssil_radius | `5.0`  
float | ssil_sharpness | `0.98`  
float | ssr_depth_tolerance | `0.2`  
bool | ssr_enabled | `false`  
float | ssr_fade_in | `0.15`  
float | ssr_fade_out | `2.0`  
int | ssr_max_steps | `64`  
float | tonemap_exposure | `1.0`  
ToneMapper | tonemap_mode | `0`  
float | tonemap_white | `1.0`  
Color | volumetric_fog_albedo | `Color(1, 1, 1, 1)`  
float | volumetric_fog_ambient_inject | `0.0`  
float | volumetric_fog_anisotropy | `0.2`  
float | volumetric_fog_density | `0.05`  
float | volumetric_fog_detail_spread | `2.0`  
Color | volumetric_fog_emission | `Color(0, 0, 0, 1)`  
float | volumetric_fog_emission_energy | `1.0`  
bool | volumetric_fog_enabled | `false`  
float | volumetric_fog_gi_inject | `1.0`  
float | volumetric_fog_length | `64.0`  
float | volumetric_fog_sky_affect | `1.0`  
float | volumetric_fog_temporal_reprojection_amount | `0.9`  
bool | volumetric_fog_temporal_reprojection_enabled | `true`  
  
## Methods

float | get_glow_level(idx: int) const  
---|---  
void | set_glow_level(idx: int, intensity: float)  
  
## Enumerations

enum BGMode:

BGMode BG_CLEAR_COLOR = `0`

Clears the background using the clear color defined in
ProjectSettings.rendering/environment/defaults/default_clear_color.

BGMode BG_COLOR = `1`

Clears the background using a custom clear color.

BGMode BG_SKY = `2`

Displays a user-defined sky in the background.

BGMode BG_CANVAS = `3`

Displays a CanvasLayer in the background.

BGMode BG_KEEP = `4`

Keeps on screen every pixel drawn in the background. This is the fastest
background mode, but it can only be safely used in fully-interior scenes (no
visible sky or sky reflections). If enabled in a scene where the background is
visible, "ghost trail" artifacts will be visible when moving the camera.

BGMode BG_CAMERA_FEED = `5`

Displays a camera feed in the background.

BGMode BG_MAX = `6`

Represents the size of the BGMode enum.

enum AmbientSource:

AmbientSource AMBIENT_SOURCE_BG = `0`

Gather ambient light from whichever source is specified as the background.

AmbientSource AMBIENT_SOURCE_DISABLED = `1`

Disable ambient light. This provides a slight performance boost over
AMBIENT_SOURCE_SKY.

AmbientSource AMBIENT_SOURCE_COLOR = `2`

Specify a specific Color for ambient light. This provides a slight performance
boost over AMBIENT_SOURCE_SKY.

AmbientSource AMBIENT_SOURCE_SKY = `3`

Gather ambient light from the Sky regardless of what the background is.

enum ReflectionSource:

ReflectionSource REFLECTION_SOURCE_BG = `0`

Use the background for reflections.

ReflectionSource REFLECTION_SOURCE_DISABLED = `1`

Disable reflections. This provides a slight performance boost over other
options.

ReflectionSource REFLECTION_SOURCE_SKY = `2`

Use the Sky for reflections regardless of what the background is.

enum ToneMapper:

ToneMapper TONE_MAPPER_LINEAR = `0`

Does not modify color data, resulting in a linear tonemapping curve which
unnaturally clips bright values, causing bright lighting to look blown out.
The simplest and fastest tonemapper.

ToneMapper TONE_MAPPER_REINHARDT = `1`

A simple tonemapping curve that rolls off bright values to prevent clipping.
This results in an image that can appear dull and low contrast. Slower than
TONE_MAPPER_LINEAR.

Note: When tonemap_white is left at the default value of `1.0`,
TONE_MAPPER_REINHARDT produces an identical image to TONE_MAPPER_LINEAR.

ToneMapper TONE_MAPPER_FILMIC = `2`

Uses a film-like tonemapping curve to prevent clipping of bright values and
provide better contrast than TONE_MAPPER_REINHARDT. Slightly slower than
TONE_MAPPER_REINHARDT.

ToneMapper TONE_MAPPER_ACES = `3`

Uses a high-contrast film-like tonemapping curve and desaturates bright values
for a more realistic appearance. Slightly slower than TONE_MAPPER_FILMIC.

Note: This tonemapping operator is called "ACES Fitted" in Godot 3.x.

ToneMapper TONE_MAPPER_AGX = `4`

Uses a film-like tonemapping curve and desaturates bright values for a more
realistic appearance. Better than other tonemappers at maintaining the hue of
colors as they become brighter. The slowest tonemapping option.

Note: tonemap_white is fixed at a value of `16.29`, which makes
TONE_MAPPER_AGX unsuitable for use with the Mobile rendering method.

enum GlowBlendMode:

GlowBlendMode GLOW_BLEND_MODE_ADDITIVE = `0`

Additive glow blending mode. Mostly used for particles, glows (bloom), lens
flare, bright sources.

GlowBlendMode GLOW_BLEND_MODE_SCREEN = `1`

Screen glow blending mode. Increases brightness, used frequently with bloom.

GlowBlendMode GLOW_BLEND_MODE_SOFTLIGHT = `2`

Soft light glow blending mode. Modifies contrast, exposes shadows and
highlights (vivid bloom).

GlowBlendMode GLOW_BLEND_MODE_REPLACE = `3`

Replace glow blending mode. Replaces all pixels' color by the glow value. This
can be used to simulate a full-screen blur effect by tweaking the glow
parameters to match the original image's brightness.

GlowBlendMode GLOW_BLEND_MODE_MIX = `4`

Mixes the glow with the underlying color to avoid increasing brightness as
much while still maintaining a glow effect.

enum FogMode:

FogMode FOG_MODE_EXPONENTIAL = `0`

Use a physically-based fog model defined primarily by fog density.

FogMode FOG_MODE_DEPTH = `1`

Use a simple fog model defined by start and end positions and a custom curve.
While not physically accurate, this model can be useful when you need more
artistic control.

enum SDFGIYScale:

SDFGIYScale SDFGI_Y_SCALE_50_PERCENT = `0`

Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be twice as
short as they are wide. This allows providing increased GI detail and reduced
light leaking with thin floors and ceilings. This is usually the best choice
for scenes that don't feature much verticality.

SDFGIYScale SDFGI_Y_SCALE_75_PERCENT = `1`

Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance between
the 50% and 100% SDFGI Y scales.

SDFGIYScale SDFGI_Y_SCALE_100_PERCENT = `2`

Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be as tall
as they are wide. This is usually the best choice for highly vertical scenes.
The downside is that light leaking may become more noticeable with thin floors
and ceilings.

## Property Descriptions

float adjustment_brightness = `1.0`

  * void set_adjustment_brightness(value: float)

  * float get_adjustment_brightness()

The global brightness value of the rendered scene. Effective only if
adjustment_enabled is `true`.

Texture adjustment_color_correction

  * void set_adjustment_color_correction(value: Texture)

  * Texture get_adjustment_color_correction()

The Texture2D or Texture3D lookup table (LUT) to use for the built-in post-
process color grading. Can use a GradientTexture1D for a 1-dimensional LUT, or
a Texture3D for a more complex LUT. Effective only if adjustment_enabled is
`true`.

float adjustment_contrast = `1.0`

  * void set_adjustment_contrast(value: float)

  * float get_adjustment_contrast()

The global contrast value of the rendered scene (default value is 1).
Effective only if adjustment_enabled is `true`.

bool adjustment_enabled = `false`

  * void set_adjustment_enabled(value: bool)

  * bool is_adjustment_enabled()

If `true`, enables the `adjustment_*` properties provided by this resource. If
`false`, modifications to the `adjustment_*` properties will have no effect on
the rendered scene.

float adjustment_saturation = `1.0`

  * void set_adjustment_saturation(value: float)

  * float get_adjustment_saturation()

The global color saturation value of the rendered scene (default value is 1).
Effective only if adjustment_enabled is `true`.

Color ambient_light_color = `Color(0, 0, 0, 1)`

  * void set_ambient_light_color(value: Color)

  * Color get_ambient_light_color()

The ambient light's Color. Only effective if ambient_light_sky_contribution is
lower than `1.0` (exclusive).

float ambient_light_energy = `1.0`

  * void set_ambient_light_energy(value: float)

  * float get_ambient_light_energy()

The ambient light's energy. The higher the value, the stronger the light. Only
effective if ambient_light_sky_contribution is lower than `1.0` (exclusive).

float ambient_light_sky_contribution = `1.0`

  * void set_ambient_light_sky_contribution(value: float)

  * float get_ambient_light_sky_contribution()

Defines the amount of light that the sky brings on the scene. A value of `0.0`
means that the sky's light emission has no effect on the scene illumination,
thus all ambient illumination is provided by the ambient light. On the
contrary, a value of `1.0` means that all the light that affects the scene is
provided by the sky, thus the ambient light parameter has no effect on the
scene.

Note: ambient_light_sky_contribution is internally clamped between `0.0` and
`1.0` (inclusive).

AmbientSource ambient_light_source = `0`

  * void set_ambient_source(value: AmbientSource)

  * AmbientSource get_ambient_source()

The ambient light source to use for rendering materials and global
illumination.

int background_camera_feed_id = `1`

  * void set_camera_feed_id(value: int)

  * int get_camera_feed_id()

The ID of the camera feed to show in the background.

int background_canvas_max_layer = `0`

  * void set_canvas_max_layer(value: int)

  * int get_canvas_max_layer()

The maximum layer ID to display. Only effective when using the BG_CANVAS
background mode.

Color background_color = `Color(0, 0, 0, 1)`

  * void set_bg_color(value: Color)

  * Color get_bg_color()

The Color displayed for clear areas of the scene. Only effective when using
the BG_COLOR background mode.

float background_energy_multiplier = `1.0`

  * void set_bg_energy_multiplier(value: float)

  * float get_bg_energy_multiplier()

Multiplier for background energy. Increase to make background brighter,
decrease to make background dimmer.

float background_intensity = `30000.0`

  * void set_bg_intensity(value: float)

  * float get_bg_intensity()

Luminance of background measured in nits (candela per square meter). Only used
when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is
enabled. The default value is roughly equivalent to the sky at midday.

BGMode background_mode = `0`

  * void set_background(value: BGMode)

  * BGMode get_background()

The background mode. See BGMode for possible values.

float fog_aerial_perspective = `0.0`

  * void set_fog_aerial_perspective(value: float)

  * float get_fog_aerial_perspective()

If set above `0.0` (exclusive), blends between the fog's color and the color
of the background Sky, as read from the radiance cubemap. This has a small
performance cost when set above `0.0`. Must have background_mode set to
BG_SKY.

This is useful to simulate aerial perspective in large scenes with low density
fog. However, it is not very useful for high-density fog, as the sky will
shine through. When set to `1.0`, the fog color comes completely from the Sky.
If set to `0.0`, aerial perspective is disabled.

Notice that this does not sample the Sky directly, but rather the radiance
cubemap. The cubemap is sampled at a mipmap level depending on the depth of
the rendered pixel; the farther away, the higher the resolution of the sampled
mipmap. This results in the actual color being a blurred version of the sky,
with more blur closer to the camera. The highest mipmap resolution is used at
a depth of Camera3D.far.

float fog_density = `0.01`

  * void set_fog_density(value: float)

  * float get_fog_density()

The fog density to be used. This is demonstrated in different ways depending
on the fog_mode mode chosen:

Exponential Fog Mode: Higher values result in denser fog. The fog rendering is
exponential like in real life.

Depth Fog mode: The maximum intensity of the deep fog, effect will appear in
the distance (relative to the camera). At `1.0` the fog will fully obscure the
scene, at `0.0` the fog will not be visible.

float fog_depth_begin = `10.0`

  * void set_fog_depth_begin(value: float)

  * float get_fog_depth_begin()

The fog's depth starting distance from the camera. Only available when
fog_mode is set to FOG_MODE_DEPTH.

float fog_depth_curve = `1.0`

  * void set_fog_depth_curve(value: float)

  * float get_fog_depth_curve()

The fog depth's intensity curve. A number of presets are available in the
Inspector by right-clicking the curve. Only available when fog_mode is set to
FOG_MODE_DEPTH.

float fog_depth_end = `100.0`

  * void set_fog_depth_end(value: float)

  * float get_fog_depth_end()

The fog's depth end distance from the camera. If this value is set to `0`, it
will be equal to the current camera's Camera3D.far value. Only available when
fog_mode is set to FOG_MODE_DEPTH.

bool fog_enabled = `false`

  * void set_fog_enabled(value: bool)

  * bool is_fog_enabled()

If `true`, fog effects are enabled.

float fog_height = `0.0`

  * void set_fog_height(value: float)

  * float get_fog_height()

The height at which the height fog effect begins.

float fog_height_density = `0.0`

  * void set_fog_height_density(value: float)

  * float get_fog_height_density()

The density used to increase fog as height decreases. To make fog increase as
height increases, use a negative value.

Color fog_light_color = `Color(0.518, 0.553, 0.608, 1)`

  * void set_fog_light_color(value: Color)

  * Color get_fog_light_color()

The fog's color.

float fog_light_energy = `1.0`

  * void set_fog_light_energy(value: float)

  * float get_fog_light_energy()

The fog's brightness. Higher values result in brighter fog.

FogMode fog_mode = `0`

  * void set_fog_mode(value: FogMode)

  * FogMode get_fog_mode()

The fog mode. See FogMode for possible values.

float fog_sky_affect = `1.0`

  * void set_fog_sky_affect(value: float)

  * float get_fog_sky_affect()

The factor to use when affecting the sky with non-volumetric fog. `1.0` means
that fog can fully obscure the sky. Lower values reduce the impact of fog on
sky rendering, with `0.0` not affecting sky rendering at all.

Note: fog_sky_affect has no visual effect if fog_aerial_perspective is `1.0`.

float fog_sun_scatter = `0.0`

  * void set_fog_sun_scatter(value: float)

  * float get_fog_sun_scatter()

If set above `0.0`, renders the scene's directional light(s) in the fog color
depending on the view angle. This can be used to give the impression that the
sun is "piercing" through the fog.

GlowBlendMode glow_blend_mode = `2`

  * void set_glow_blend_mode(value: GlowBlendMode)

  * GlowBlendMode get_glow_blend_mode()

The glow blending mode.

Note: glow_blend_mode has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_bloom = `0.0`

  * void set_glow_bloom(value: float)

  * float get_glow_bloom()

The bloom's intensity. If set to a value higher than `0`, this will make glow
visible in areas darker than the glow_hdr_threshold.

bool glow_enabled = `false`

  * void set_glow_enabled(value: bool)

  * bool is_glow_enabled()

If `true`, the glow effect is enabled. This simulates real world eye/camera
behavior where bright pixels bleed onto surrounding pixels.

Note: When using the Mobile rendering method, glow looks different due to the
lower dynamic range available in the Mobile rendering method.

Note: When using the Compatibility rendering method, glow uses a different
implementation with some properties being unavailable and hidden from the
inspector: `glow_levels/*`, glow_normalized, glow_strength, glow_blend_mode,
glow_mix, glow_map, and glow_map_strength. This implementation is optimized to
run on low-end devices and is less flexible as a result.

float glow_hdr_luminance_cap = `12.0`

  * void set_glow_hdr_luminance_cap(value: float)

  * float get_glow_hdr_luminance_cap()

The higher threshold of the HDR glow. Areas brighter than this threshold will
be clamped for the purposes of the glow effect.

float glow_hdr_scale = `2.0`

  * void set_glow_hdr_bleed_scale(value: float)

  * float get_glow_hdr_bleed_scale()

The bleed scale of the HDR glow.

float glow_hdr_threshold = `1.0`

  * void set_glow_hdr_bleed_threshold(value: float)

  * float get_glow_hdr_bleed_threshold()

The lower threshold of the HDR glow. When using the Mobile rendering method
(which only supports a lower dynamic range up to `2.0`), this may need to be
below `1.0` for glow to be visible. A value of `0.9` works well in this case.
This value also needs to be decreased below `1.0` when using glow in 2D, as 2D
rendering is performed in SDR.

float glow_intensity = `0.8`

  * void set_glow_intensity(value: float)

  * float get_glow_intensity()

The overall brightness multiplier of the glow effect. When using the Mobile
rendering method (which only supports a lower dynamic range up to `2.0`), this
should be increased to `1.5` to compensate.

float glow_levels/1 = `0.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 1st level of glow. This is the most "local" level (least
blurry).

Note: glow_levels/1 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/2 = `0.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 2nd level of glow.

Note: glow_levels/2 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/3 = `1.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 3rd level of glow.

Note: glow_levels/3 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/4 = `0.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 4th level of glow.

Note: glow_levels/4 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/5 = `1.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 5th level of glow.

Note: glow_levels/5 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/6 = `0.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 6th level of glow.

Note: glow_levels/6 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_levels/7 = `0.0`

  * void set_glow_level(idx: int, intensity: float)

  * float get_glow_level(idx: int) const

The intensity of the 7th level of glow. This is the most "global" level
(blurriest).

Note: glow_levels/7 has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

Texture glow_map

  * void set_glow_map(value: Texture)

  * Texture get_glow_map()

The texture that should be used as a glow map to multiply the resulting glow
color according to glow_map_strength. This can be used to create a "lens dirt"
effect. The texture's RGB color channels are used for modulation, but the
alpha channel is ignored.

Note: The texture will be stretched to fit the screen. Therefore, it's
recommended to use a texture with an aspect ratio that matches your project's
base aspect ratio (typically 16:9).

Note: glow_map has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation optimized for
low-end devices.

float glow_map_strength = `0.8`

  * void set_glow_map_strength(value: float)

  * float get_glow_map_strength()

How strong of an influence the glow_map should have on the overall glow
effect. A strength of `0.0` means the glow map has no influence, while a
strength of `1.0` means the glow map has full influence.

Note: If the glow map has black areas, a value of `1.0` can also turn off the
glow effect entirely in specific areas of the screen.

Note: glow_map_strength has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_mix = `0.05`

  * void set_glow_mix(value: float)

  * float get_glow_mix()

When using the GLOW_BLEND_MODE_MIX glow_blend_mode, this controls how much the
source image is blended with the glow layer. A value of `0.0` makes the glow
rendering invisible, while a value of `1.0` is equivalent to
GLOW_BLEND_MODE_REPLACE.

Note: glow_mix has no effect when using the Compatibility rendering method,
due to this rendering method using a simpler glow implementation optimized for
low-end devices.

bool glow_normalized = `false`

  * void set_glow_normalized(value: bool)

  * bool is_glow_normalized()

If `true`, glow levels will be normalized so that summed together their
intensities equal `1.0`.

Note: glow_normalized has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

float glow_strength = `1.0`

  * void set_glow_strength(value: float)

  * float get_glow_strength()

The strength of the glow effect. This applies as the glow is blurred across
the screen and increases the distance and intensity of the blur. When using
the Mobile rendering method, this should be increased to compensate for the
lower dynamic range.

Note: glow_strength has no effect when using the Compatibility rendering
method, due to this rendering method using a simpler glow implementation
optimized for low-end devices.

ReflectionSource reflected_light_source = `0`

  * void set_reflection_source(value: ReflectionSource)

  * ReflectionSource get_reflection_source()

The reflected (specular) light source.

float sdfgi_bounce_feedback = `0.5`

  * void set_sdfgi_bounce_feedback(value: float)

  * float get_sdfgi_bounce_feedback()

The energy multiplier applied to light every time it bounces from a surface
when using SDFGI. Values greater than `0.0` will simulate multiple bounces,
resulting in a more realistic appearance. Increasing sdfgi_bounce_feedback
generally has no performance impact. See also sdfgi_energy.

Note: Values greater than `0.5` can cause infinite feedback loops and should
be avoided in scenes with bright materials.

Note: If sdfgi_bounce_feedback is `0.0`, indirect lighting will not be
represented in reflections as light will only bounce one time.

float sdfgi_cascade0_distance = `12.8`

  * void set_sdfgi_cascade0_distance(value: float)

  * float get_sdfgi_cascade0_distance()

Note: This property is linked to sdfgi_min_cell_size and sdfgi_max_distance.
Changing its value will automatically change those properties as well.

int sdfgi_cascades = `4`

  * void set_sdfgi_cascades(value: int)

  * int get_sdfgi_cascades()

The number of cascades to use for SDFGI (between 1 and 8). A higher number of
cascades allows displaying SDFGI further away while preserving detail up
close, at the cost of performance. When using SDFGI on small-scale levels,
sdfgi_cascades can often be decreased between `1` and `4` to improve
performance.

bool sdfgi_enabled = `false`

  * void set_sdfgi_enabled(value: bool)

  * bool is_sdfgi_enabled()

If `true`, enables signed distance field global illumination for meshes that
have their GeometryInstance3D.gi_mode set to
GeometryInstance3D.GI_MODE_STATIC. SDFGI is a real-time global illumination
technique that works well with procedurally generated and user-built levels,
including in situations where geometry is created during gameplay. The signed
distance field is automatically generated around the camera as it moves.
Dynamic lights are supported, but dynamic occluders and emissive surfaces are
not.

Note: SDFGI is only supported in the Forward+ rendering method, not Mobile or
Compatibility.

Performance: SDFGI is relatively demanding on the GPU and is not suited to
low-end hardware such as integrated graphics (consider LightmapGI instead). To
improve SDFGI performance, enable
ProjectSettings.rendering/global_illumination/gi/use_half_resolution in the
Project Settings.

Note: Meshes should have sufficiently thick walls to avoid light leaks (avoid
one-sided walls). For interior levels, enclose your level geometry in a
sufficiently large box and bridge the loops to close the mesh.

float sdfgi_energy = `1.0`

  * void set_sdfgi_energy(value: float)

  * float get_sdfgi_energy()

The energy multiplier to use for SDFGI. Higher values will result in brighter
indirect lighting and reflections. See also sdfgi_bounce_feedback.

float sdfgi_max_distance = `204.8`

  * void set_sdfgi_max_distance(value: float)

  * float get_sdfgi_max_distance()

The maximum distance at which SDFGI is visible. Beyond this distance,
environment lighting or other sources of GI such as ReflectionProbe will be
used as a fallback.

Note: This property is linked to sdfgi_min_cell_size and
sdfgi_cascade0_distance. Changing its value will automatically change those
properties as well.

float sdfgi_min_cell_size = `0.2`

  * void set_sdfgi_min_cell_size(value: float)

  * float get_sdfgi_min_cell_size()

The cell size to use for the closest SDFGI cascade (in 3D units). Lower values
allow SDFGI to be more precise up close, at the cost of making SDFGI updates
more demanding. This can cause stuttering when the camera moves fast. Higher
values allow SDFGI to cover more ground, while also reducing the performance
impact of SDFGI updates.

Note: This property is linked to sdfgi_max_distance and
sdfgi_cascade0_distance. Changing its value will automatically change those
properties as well.

float sdfgi_normal_bias = `1.1`

  * void set_sdfgi_normal_bias(value: float)

  * float get_sdfgi_normal_bias()

The normal bias to use for SDFGI probes. Increasing this value can reduce
visible streaking artifacts on sloped surfaces, at the cost of increased light
leaking.

float sdfgi_probe_bias = `1.1`

  * void set_sdfgi_probe_bias(value: float)

  * float get_sdfgi_probe_bias()

The constant bias to use for SDFGI probes. Increasing this value can reduce
visible streaking artifacts on sloped surfaces, at the cost of increased light
leaking.

bool sdfgi_read_sky_light = `true`

  * void set_sdfgi_read_sky_light(value: bool)

  * bool is_sdfgi_reading_sky_light()

If `true`, SDFGI takes the environment lighting into account. This should be
set to `false` for interior scenes.

bool sdfgi_use_occlusion = `false`

  * void set_sdfgi_use_occlusion(value: bool)

  * bool is_sdfgi_using_occlusion()

If `true`, SDFGI uses an occlusion detection approach to reduce light leaking.
Occlusion may however introduce dark blotches in certain spots, which may be
undesired in mostly outdoor scenes. sdfgi_use_occlusion has a performance
impact and should only be enabled when needed.

SDFGIYScale sdfgi_y_scale = `1`

  * void set_sdfgi_y_scale(value: SDFGIYScale)

  * SDFGIYScale get_sdfgi_y_scale()

The Y scale to use for SDFGI cells. Lower values will result in SDFGI cells
being packed together more closely on the Y axis. This is used to balance
between quality and covering a lot of vertical ground. sdfgi_y_scale should be
set depending on how vertical your scene is (and how fast your camera may move
on the Y axis).

Sky sky

  * void set_sky(value: Sky)

  * Sky get_sky()

The Sky resource used for this Environment.

float sky_custom_fov = `0.0`

  * void set_sky_custom_fov(value: float)

  * float get_sky_custom_fov()

If set to a value greater than `0.0`, overrides the field of view to use for
sky rendering. If set to `0.0`, the same FOV as the current Camera3D is used
for sky rendering.

Vector3 sky_rotation = `Vector3(0, 0, 0)`

  * void set_sky_rotation(value: Vector3)

  * Vector3 get_sky_rotation()

The rotation to use for sky rendering.

float ssao_ao_channel_affect = `0.0`

  * void set_ssao_ao_channel_affect(value: float)

  * float get_ssao_ao_channel_affect()

The screen-space ambient occlusion intensity on materials that have an AO
texture defined. Values higher than `0` will make the SSAO effect visible in
areas darkened by AO textures.

float ssao_detail = `0.5`

  * void set_ssao_detail(value: float)

  * float get_ssao_detail()

Sets the strength of the additional level of detail for the screen-space
ambient occlusion effect. A high value makes the detail pass more prominent,
but it may contribute to aliasing in your final image.

bool ssao_enabled = `false`

  * void set_ssao_enabled(value: bool)

  * bool is_ssao_enabled()

If `true`, the screen-space ambient occlusion effect is enabled. This darkens
objects' corners and cavities to simulate ambient light not reaching the
entire object as in real life. This works well for small, dynamic objects, but
baked lighting or ambient occlusion textures will do a better job at
displaying ambient occlusion on large static objects. Godot uses a form of
SSAO called Adaptive Screen Space Ambient Occlusion which is itself a form of
Horizon Based Ambient Occlusion.

Note: SSAO is only supported in the Forward+ rendering method, not Mobile or
Compatibility.

float ssao_horizon = `0.06`

  * void set_ssao_horizon(value: float)

  * float get_ssao_horizon()

The threshold for considering whether a given point on a surface is occluded
or not represented as an angle from the horizon mapped into the `0.0-1.0`
range. A value of `1.0` results in no occlusion.

float ssao_intensity = `2.0`

  * void set_ssao_intensity(value: float)

  * float get_ssao_intensity()

The primary screen-space ambient occlusion intensity. Acts as a multiplier for
the screen-space ambient occlusion effect. A higher value results in darker
occlusion.

float ssao_light_affect = `0.0`

  * void set_ssao_direct_light_affect(value: float)

  * float get_ssao_direct_light_affect()

The screen-space ambient occlusion intensity in direct light. In real life,
ambient occlusion only applies to indirect light, which means its effects
can't be seen in direct light. Values higher than `0` will make the SSAO
effect visible in direct light.

float ssao_power = `1.5`

  * void set_ssao_power(value: float)

  * float get_ssao_power()

The distribution of occlusion. A higher value results in darker occlusion,
similar to ssao_intensity, but with a sharper falloff.

float ssao_radius = `1.0`

  * void set_ssao_radius(value: float)

  * float get_ssao_radius()

The distance at which objects can occlude each other when calculating screen-
space ambient occlusion. Higher values will result in occlusion over a greater
distance at the cost of performance and quality.

float ssao_sharpness = `0.98`

  * void set_ssao_sharpness(value: float)

  * float get_ssao_sharpness()

The amount that the screen-space ambient occlusion effect is allowed to blur
over the edges of objects. Setting too high will result in aliasing around the
edges of objects. Setting too low will make object edges appear blurry.

bool ssil_enabled = `false`

  * void set_ssil_enabled(value: bool)

  * bool is_ssil_enabled()

If `true`, the screen-space indirect lighting effect is enabled. Screen space
indirect lighting is a form of indirect lighting that allows diffuse light to
bounce between nearby objects. Screen-space indirect lighting works very
similarly to screen-space ambient occlusion, in that it only affects a limited
range. It is intended to be used along with a form of proper global
illumination like SDFGI or VoxelGI. Screen-space indirect lighting is not
affected by individual light's Light3D.light_indirect_energy.

Note: SSIL is only supported in the Forward+ rendering method, not Mobile or
Compatibility.

float ssil_intensity = `1.0`

  * void set_ssil_intensity(value: float)

  * float get_ssil_intensity()

The brightness multiplier for the screen-space indirect lighting effect. A
higher value will result in brighter light.

float ssil_normal_rejection = `1.0`

  * void set_ssil_normal_rejection(value: float)

  * float get_ssil_normal_rejection()

Amount of normal rejection used when calculating screen-space indirect
lighting. Normal rejection uses the normal of a given sample point to reject
samples that are facing away from the current pixel. Normal rejection is
necessary to avoid light leaking when only one side of an object is
illuminated. However, normal rejection can be disabled if light leaking is
desirable, such as when the scene mostly contains emissive objects that emit
light from faces that cannot be seen from the camera.

float ssil_radius = `5.0`

  * void set_ssil_radius(value: float)

  * float get_ssil_radius()

The distance that bounced lighting can travel when using the screen space
indirect lighting effect. A larger value will result in light bouncing further
in a scene, but may result in under-sampling artifacts which look like long
spikes surrounding light sources.

float ssil_sharpness = `0.98`

  * void set_ssil_sharpness(value: float)

  * float get_ssil_sharpness()

The amount that the screen-space indirect lighting effect is allowed to blur
over the edges of objects. Setting too high will result in aliasing around the
edges of objects. Setting too low will make object edges appear blurry.

float ssr_depth_tolerance = `0.2`

  * void set_ssr_depth_tolerance(value: float)

  * float get_ssr_depth_tolerance()

The depth tolerance for screen-space reflections.

bool ssr_enabled = `false`

  * void set_ssr_enabled(value: bool)

  * bool is_ssr_enabled()

If `true`, screen-space reflections are enabled. Screen-space reflections are
more accurate than reflections from VoxelGIs or ReflectionProbes, but are
slower and can't reflect surfaces occluded by others.

Note: SSR is only supported in the Forward+ rendering method, not Mobile or
Compatibility.

float ssr_fade_in = `0.15`

  * void set_ssr_fade_in(value: float)

  * float get_ssr_fade_in()

The fade-in distance for screen-space reflections. Affects the area from the
reflected material to the screen-space reflection. Only positive values are
valid (negative values will be clamped to `0.0`).

float ssr_fade_out = `2.0`

  * void set_ssr_fade_out(value: float)

  * float get_ssr_fade_out()

The fade-out distance for screen-space reflections. Affects the area from the
screen-space reflection to the "global" reflection. Only positive values are
valid (negative values will be clamped to `0.0`).

int ssr_max_steps = `64`

  * void set_ssr_max_steps(value: int)

  * int get_ssr_max_steps()

The maximum number of steps for screen-space reflections. Higher values are
slower.

float tonemap_exposure = `1.0`

  * void set_tonemap_exposure(value: float)

  * float get_tonemap_exposure()

Adjusts the brightness of values before they are provided to the tonemapper.
Higher tonemap_exposure values result in a brighter image. See also
tonemap_white.

Note: Values provided to the tonemapper will also be multiplied by `2.0` and
`1.8` for TONE_MAPPER_FILMIC and TONE_MAPPER_ACES respectively to produce a
similar apparent brightness as TONE_MAPPER_LINEAR.

ToneMapper tonemap_mode = `0`

  * void set_tonemapper(value: ToneMapper)

  * ToneMapper get_tonemapper()

The tonemapping mode to use. Tonemapping is the process that "converts" HDR
values to be suitable for rendering on an LDR display. (Godot doesn't support
rendering on HDR displays yet.)

float tonemap_white = `1.0`

  * void set_tonemap_white(value: float)

  * float get_tonemap_white()

The white reference value for tonemapping, which indicates where bright white
is located in the scale of values provided to the tonemapper. For
photorealistic lighting, recommended values are between `6.0` and `8.0`.
Higher values result in less blown out highlights, but may make the scene
appear lower contrast. See also tonemap_exposure.

Note: tonemap_white is ignored when using TONE_MAPPER_LINEAR or
TONE_MAPPER_AGX.

Color volumetric_fog_albedo = `Color(1, 1, 1, 1)`

  * void set_volumetric_fog_albedo(value: Color)

  * Color get_volumetric_fog_albedo()

The Color of the volumetric fog when interacting with lights. Mist and fog
have an albedo close to `Color(1, 1, 1, 1)` while smoke has a darker albedo.

float volumetric_fog_ambient_inject = `0.0`

  * void set_volumetric_fog_ambient_inject(value: float)

  * float get_volumetric_fog_ambient_inject()

Scales the strength of ambient light used in the volumetric fog. A value of
`0.0` means that ambient light will not impact the volumetric fog.
volumetric_fog_ambient_inject has a small performance cost when set above
`0.0`.

Note: This has no visible effect if volumetric_fog_density is `0.0` or if
volumetric_fog_albedo is a fully black color.

float volumetric_fog_anisotropy = `0.2`

  * void set_volumetric_fog_anisotropy(value: float)

  * float get_volumetric_fog_anisotropy()

The direction of scattered light as it goes through the volumetric fog. A
value close to `1.0` means almost all light is scattered forward. A value
close to `0.0` means light is scattered equally in all directions. A value
close to `-1.0` means light is scattered mostly backward. Fog and mist scatter
light slightly forward, while smoke scatters light equally in all directions.

float volumetric_fog_density = `0.05`

  * void set_volumetric_fog_density(value: float)

  * float get_volumetric_fog_density()

The base exponential density of the volumetric fog. Set this to the lowest
density you want to have globally. FogVolumes can be used to add to or
subtract from this density in specific areas. Fog rendering is exponential as
in real life.

A value of `0.0` disables global volumetric fog while allowing FogVolumes to
display volumetric fog in specific areas.

To make volumetric fog work as a volumetric lighting solution, set
volumetric_fog_density to the lowest non-zero value (`0.0001`) then increase
lights' Light3D.light_volumetric_fog_energy to values between `10000` and
`100000` to compensate for the very low density.

float volumetric_fog_detail_spread = `2.0`

  * void set_volumetric_fog_detail_spread(value: float)

  * float get_volumetric_fog_detail_spread()

The distribution of size down the length of the froxel buffer. A higher value
compresses the froxels closer to the camera and places more detail closer to
the camera.

Color volumetric_fog_emission = `Color(0, 0, 0, 1)`

  * void set_volumetric_fog_emission(value: Color)

  * Color get_volumetric_fog_emission()

The emitted light from the volumetric fog. Even with emission, volumetric fog
will not cast light onto other surfaces. Emission is useful to establish an
ambient color. As the volumetric fog effect uses single-scattering only, fog
tends to need a little bit of emission to soften the harsh shadows.

float volumetric_fog_emission_energy = `1.0`

  * void set_volumetric_fog_emission_energy(value: float)

  * float get_volumetric_fog_emission_energy()

The brightness of the emitted light from the volumetric fog.

bool volumetric_fog_enabled = `false`

  * void set_volumetric_fog_enabled(value: bool)

  * bool is_volumetric_fog_enabled()

Enables the volumetric fog effect. Volumetric fog uses a screen-aligned froxel
buffer to calculate accurate volumetric scattering in the short to medium
range. Volumetric fog interacts with FogVolumes and lights to calculate
localized and global fog. Volumetric fog uses a PBR single-scattering model
based on extinction, scattering, and emission which it exposes to users as
density, albedo, and emission.

Note: Volumetric fog is only supported in the Forward+ rendering method, not
Mobile or Compatibility.

float volumetric_fog_gi_inject = `1.0`

  * void set_volumetric_fog_gi_inject(value: float)

  * float get_volumetric_fog_gi_inject()

Scales the strength of Global Illumination used in the volumetric fog's albedo
color. A value of `0.0` means that Global Illumination will not impact the
volumetric fog. volumetric_fog_gi_inject has a small performance cost when set
above `0.0`.

Note: This has no visible effect if volumetric_fog_density is `0.0` or if
volumetric_fog_albedo is a fully black color.

Note: Only VoxelGI and SDFGI (sdfgi_enabled) are taken into account when using
volumetric_fog_gi_inject. Global illumination from LightmapGI, ReflectionProbe
and SSIL (see ssil_enabled) will be ignored by volumetric fog.

float volumetric_fog_length = `64.0`

  * void set_volumetric_fog_length(value: float)

  * float get_volumetric_fog_length()

The distance over which the volumetric fog is computed. Increase to compute
fog over a greater range, decrease to add more detail when a long range is not
needed. For best quality fog, keep this as low as possible. See also
ProjectSettings.rendering/environment/volumetric_fog/volume_depth.

float volumetric_fog_sky_affect = `1.0`

  * void set_volumetric_fog_sky_affect(value: float)

  * float get_volumetric_fog_sky_affect()

The factor to use when affecting the sky with volumetric fog. `1.0` means that
volumetric fog can fully obscure the sky. Lower values reduce the impact of
volumetric fog on sky rendering, with `0.0` not affecting sky rendering at
all.

Note: volumetric_fog_sky_affect also affects FogVolumes, even if
volumetric_fog_density is `0.0`. If you notice FogVolumes are disappearing
when looking towards the sky, set volumetric_fog_sky_affect to `1.0`.

float volumetric_fog_temporal_reprojection_amount = `0.9`

  * void set_volumetric_fog_temporal_reprojection_amount(value: float)

  * float get_volumetric_fog_temporal_reprojection_amount()

The amount by which to blend the last frame with the current frame. A higher
number results in smoother volumetric fog, but makes "ghosting" much worse. A
lower value reduces ghosting but can result in the per-frame temporal jitter
becoming visible.

bool volumetric_fog_temporal_reprojection_enabled = `true`

  * void set_volumetric_fog_temporal_reprojection_enabled(value: bool)

  * bool is_volumetric_fog_temporal_reprojection_enabled()

Enables temporal reprojection in the volumetric fog. Temporal reprojection
blends the current frame's volumetric fog with the last frame's volumetric fog
to smooth out jagged edges. The performance cost is minimal; however, it leads
to moving FogVolumes and Light3Ds "ghosting" and leaving a trail behind them.
When temporal reprojection is enabled, try to avoid moving FogVolumes or
Light3Ds too fast. Short-lived dynamic lighting effects should have
Light3D.light_volumetric_fog_energy set to `0.0` to avoid ghosting.

## Method Descriptions

float get_glow_level(idx: int) const

Returns the intensity of the glow level `idx`.

void set_glow_level(idx: int, intensity: float)

Sets the intensity of the glow level `idx`. A value above `0.0` enables the
level. Each level relies on the previous level. This means that enabling
higher glow levels will slow down the glow effect rendering, even if previous
levels aren't enabled.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

