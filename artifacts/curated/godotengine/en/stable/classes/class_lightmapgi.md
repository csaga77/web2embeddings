# LightmapGI

Inherits: VisualInstance3D < Node3D < Node < Object

Computes and stores baked lightmaps for fast global illumination.

## Description

The LightmapGI node is used to compute and store baked lightmaps. Lightmaps
are used to provide high-quality indirect lighting with very little light
leaking. LightmapGI can also provide rough reflections using spherical
harmonics if directional is enabled. Dynamic objects can receive indirect
lighting thanks to light probes, which can be automatically placed by setting
generate_probes_subdiv to a value other than GENERATE_PROBES_DISABLED.
Additional lightmap probes can also be added by creating LightmapProbe nodes.
The downside is that lightmaps are fully static and cannot be baked in an
exported project. Baking a LightmapGI node is also slower compared to VoxelGI.

Procedural generation: Lightmap baking functionality is only available in the
editor. This means LightmapGI is not suited to procedurally generated or user-
built levels. For procedurally generated or user-built levels, use VoxelGI or
SDFGI instead (see Environment.sdfgi_enabled).

Performance: LightmapGI provides the best possible run-time performance for
global illumination. It is suitable for low-end hardware including integrated
graphics and mobile devices.

Note: Due to how lightmaps work, most properties only have a visible effect
once lightmaps are baked again.

Note: Lightmap baking on CSGShape3Ds and PrimitiveMeshes is not supported, as
these cannot store UV2 data required for baking.

Note: If no custom lightmappers are installed, LightmapGI can only be baked
from devices that support the Forward+ or Mobile renderers.

Note: The LightmapGI node only bakes light data for child nodes of its parent.
Nodes further up the hierarchy of the scene will not be baked.

## Tutorials

  * Using Lightmap global illumination

## Properties

float | bias | `0.0005`  
---|---|---  
float | bounce_indirect_energy | `1.0`  
int | bounces | `3`  
CameraAttributes | camera_attributes  
int | denoiser_range | `10`  
float | denoiser_strength | `0.1`  
bool | directional | `false`  
Color | environment_custom_color | `Color(1, 1, 1, 1)`  
float | environment_custom_energy | `1.0`  
Sky | environment_custom_sky  
EnvironmentMode | environment_mode | `1`  
GenerateProbes | generate_probes_subdiv | `2`  
bool | interior | `false`  
LightmapGIData | light_data  
int | max_texture_size | `16384`  
BakeQuality | quality | `1`  
ShadowmaskMode | shadowmask_mode | `0`  
bool | supersampling | `false`  
float | supersampling_factor | `2.0`  
float | texel_scale | `1.0`  
bool | use_denoiser | `true`  
bool | use_texture_for_bounces | `true`  
  
## Enumerations

enum BakeQuality:

BakeQuality BAKE_QUALITY_LOW = `0`

Low bake quality (fastest bake times). The quality of this preset can be
adjusted by changing
ProjectSettings.rendering/lightmapping/bake_quality/low_quality_ray_count and
ProjectSettings.rendering/lightmapping/bake_quality/low_quality_probe_ray_count.

BakeQuality BAKE_QUALITY_MEDIUM = `1`

Medium bake quality (fast bake times). The quality of this preset can be
adjusted by changing
ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_ray_count
and
ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_probe_ray_count.

BakeQuality BAKE_QUALITY_HIGH = `2`

High bake quality (slow bake times). The quality of this preset can be
adjusted by changing
ProjectSettings.rendering/lightmapping/bake_quality/high_quality_ray_count and
ProjectSettings.rendering/lightmapping/bake_quality/high_quality_probe_ray_count.

BakeQuality BAKE_QUALITY_ULTRA = `3`

Highest bake quality (slowest bake times). The quality of this preset can be
adjusted by changing
ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_ray_count
and
ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count.

enum GenerateProbes:

GenerateProbes GENERATE_PROBES_DISABLED = `0`

Don't generate lightmap probes for lighting dynamic objects.

GenerateProbes GENERATE_PROBES_SUBDIV_4 = `1`

Lowest level of subdivision (fastest bake times, smallest file sizes).

GenerateProbes GENERATE_PROBES_SUBDIV_8 = `2`

Low level of subdivision (fast bake times, small file sizes).

GenerateProbes GENERATE_PROBES_SUBDIV_16 = `3`

High level of subdivision (slow bake times, large file sizes).

GenerateProbes GENERATE_PROBES_SUBDIV_32 = `4`

Highest level of subdivision (slowest bake times, largest file sizes).

enum BakeError:

BakeError BAKE_ERROR_OK = `0`

Lightmap baking was successful.

BakeError BAKE_ERROR_NO_SCENE_ROOT = `1`

Lightmap baking failed because the root node for the edited scene could not be
accessed.

BakeError BAKE_ERROR_FOREIGN_DATA = `2`

Lightmap baking failed as the lightmap data resource is embedded in a foreign
resource.

BakeError BAKE_ERROR_NO_LIGHTMAPPER = `3`

Lightmap baking failed as there is no lightmapper available in this Godot
build.

BakeError BAKE_ERROR_NO_SAVE_PATH = `4`

Lightmap baking failed as the LightmapGIData save path isn't configured in the
resource.

BakeError BAKE_ERROR_NO_MESHES = `5`

Lightmap baking failed as there are no meshes whose GeometryInstance3D.gi_mode
is GeometryInstance3D.GI_MODE_STATIC and with valid UV2 mapping in the current
scene. You may need to select 3D scenes in the Import dock and change their
global illumination mode accordingly.

BakeError BAKE_ERROR_MESHES_INVALID = `6`

Lightmap baking failed as the lightmapper failed to analyze some of the meshes
marked as static for baking.

BakeError BAKE_ERROR_CANT_CREATE_IMAGE = `7`

Lightmap baking failed as the resulting image couldn't be saved or imported by
Godot after it was saved.

BakeError BAKE_ERROR_USER_ABORTED = `8`

The user aborted the lightmap baking operation (typically by clicking the
Cancel button in the progress dialog).

BakeError BAKE_ERROR_TEXTURE_SIZE_TOO_SMALL = `9`

Lightmap baking failed as the maximum texture size is too small to fit some of
the meshes marked for baking.

BakeError BAKE_ERROR_LIGHTMAP_TOO_SMALL = `10`

Lightmap baking failed as the lightmap is too small.

BakeError BAKE_ERROR_ATLAS_TOO_SMALL = `11`

Lightmap baking failed as the lightmap was unable to fit into an atlas.

enum EnvironmentMode:

EnvironmentMode ENVIRONMENT_MODE_DISABLED = `0`

Ignore environment lighting when baking lightmaps.

EnvironmentMode ENVIRONMENT_MODE_SCENE = `1`

Use the scene's environment lighting when baking lightmaps.

Note: If baking lightmaps in a scene with no WorldEnvironment node, this will
act like ENVIRONMENT_MODE_DISABLED. The editor's preview sky and sun is not
taken into account by LightmapGI when baking lightmaps.

EnvironmentMode ENVIRONMENT_MODE_CUSTOM_SKY = `2`

Use environment_custom_sky as a source of environment lighting when baking
lightmaps.

EnvironmentMode ENVIRONMENT_MODE_CUSTOM_COLOR = `3`

Use environment_custom_color multiplied by environment_custom_energy as a
constant source of environment lighting when baking lightmaps.

## Property Descriptions

float bias = `0.0005`

  * void set_bias(value: float)

  * float get_bias()

The bias to use when computing shadows. Increasing bias can fix shadow acne on
the resulting baked lightmap, but can introduce peter-panning (shadows not
connecting to their casters). Real-time Light3D shadows are not affected by
this bias property.

float bounce_indirect_energy = `1.0`

  * void set_bounce_indirect_energy(value: float)

  * float get_bounce_indirect_energy()

The energy multiplier for each bounce. Higher values will make indirect
lighting brighter. A value of `1.0` represents physically accurate behavior,
but higher values can be used to make indirect lighting propagate more visibly
when using a low number of bounces. This can be used to speed up bake times by
lowering the number of bounces then increasing bounce_indirect_energy.

Note: bounce_indirect_energy only has an effect if bounces is set to a value
greater than or equal to `1`.

int bounces = `3`

  * void set_bounces(value: int)

  * int get_bounces()

Number of light bounces that are taken into account during baking. Higher
values result in brighter, more realistic lighting, at the cost of longer bake
times. If set to `0`, only environment lighting, direct light and emissive
lighting is baked.

CameraAttributes camera_attributes

  * void set_camera_attributes(value: CameraAttributes)

  * CameraAttributes get_camera_attributes()

The CameraAttributes resource that specifies exposure levels to bake at. Auto-
exposure and non exposure properties will be ignored. Exposure settings should
be used to reduce the dynamic range present when baking. If exposure is too
high, the LightmapGI will have banding artifacts or may have over-exposure
artifacts.

int denoiser_range = `10`

  * void set_denoiser_range(value: int)

  * int get_denoiser_range()

The distance in pixels from which the denoiser samples. Lower values preserve
more details, but may give blotchy results if the lightmap quality is not high
enough. Only effective if use_denoiser is `true` and
ProjectSettings.rendering/lightmapping/denoising/denoiser is set to JNLM.

float denoiser_strength = `0.1`

  * void set_denoiser_strength(value: float)

  * float get_denoiser_strength()

The strength of denoising step applied to the generated lightmaps. Only
effective if use_denoiser is `true` and
ProjectSettings.rendering/lightmapping/denoising/denoiser is set to JNLM.

bool directional = `false`

  * void set_directional(value: bool)

  * bool is_directional()

If `true`, bakes lightmaps to contain directional information as spherical
harmonics. This results in more realistic lighting appearance, especially with
normal mapped materials and for lights that have their direct light baked
(Light3D.light_bake_mode set to Light3D.BAKE_STATIC and with
Light3D.editor_only set to `false`). The directional information is also used
to provide rough reflections for static and dynamic objects. This has a small
run-time performance cost as the shader has to perform more work to interpret
the direction information from the lightmap. Directional lightmaps also take
longer to bake and result in larger file sizes.

Note: The property's name has no relationship with DirectionalLight3D.
directional works with all light types.

Color environment_custom_color = `Color(1, 1, 1, 1)`

  * void set_environment_custom_color(value: Color)

  * Color get_environment_custom_color()

The color to use for environment lighting. Only effective if environment_mode
is ENVIRONMENT_MODE_CUSTOM_COLOR.

float environment_custom_energy = `1.0`

  * void set_environment_custom_energy(value: float)

  * float get_environment_custom_energy()

The color multiplier to use for environment lighting. Only effective if
environment_mode is ENVIRONMENT_MODE_CUSTOM_COLOR.

Sky environment_custom_sky

  * void set_environment_custom_sky(value: Sky)

  * Sky get_environment_custom_sky()

The sky to use as a source of environment lighting. Only effective if
environment_mode is ENVIRONMENT_MODE_CUSTOM_SKY.

EnvironmentMode environment_mode = `1`

  * void set_environment_mode(value: EnvironmentMode)

  * EnvironmentMode get_environment_mode()

The environment mode to use when baking lightmaps.

GenerateProbes generate_probes_subdiv = `2`

  * void set_generate_probes(value: GenerateProbes)

  * GenerateProbes get_generate_probes()

The level of subdivision to use when automatically generating LightmapProbes
for dynamic object lighting. Higher values result in more accurate indirect
lighting on dynamic objects, at the cost of longer bake times and larger file
sizes.

Note: Automatically generated LightmapProbes are not visible as nodes in the
Scene tree dock, and cannot be modified this way after they are generated.

Note: Regardless of generate_probes_subdiv, direct lighting on dynamic objects
is always applied using Light3D nodes in real-time.

bool interior = `false`

  * void set_interior(value: bool)

  * bool is_interior()

If `true`, ignore environment lighting when baking lightmaps.

LightmapGIData light_data

  * void set_light_data(value: LightmapGIData)

  * LightmapGIData get_light_data()

The LightmapGIData associated to this LightmapGI node. This resource is
automatically created after baking, and is not meant to be created manually.

int max_texture_size = `16384`

  * void set_max_texture_size(value: int)

  * int get_max_texture_size()

The maximum texture size for the generated texture atlas. Higher values will
result in fewer slices being generated, but may not work on all hardware as a
result of hardware limitations on texture sizes. Leave max_texture_size at its
default value of `16384` if unsure.

BakeQuality quality = `1`

  * void set_bake_quality(value: BakeQuality)

  * BakeQuality get_bake_quality()

The quality preset to use when baking lightmaps. This affects bake times, but
output file sizes remain mostly identical across quality levels.

To further speed up bake times, decrease bounces, disable use_denoiser and/or
decrease texel_scale.

To further increase quality, enable supersampling and/or increase texel_scale.

ShadowmaskMode shadowmask_mode = `0`

  * void set_shadowmask_mode(value: ShadowmaskMode)

  * ShadowmaskMode get_shadowmask_mode()

Experimental: This property may be changed or removed in future versions.

The shadowmasking policy to use for directional shadows on static objects that
are baked with this LightmapGI instance.

Shadowmasking allows DirectionalLight3D nodes to cast shadows even outside the
range defined by their DirectionalLight3D.directional_shadow_max_distance
property. This is done by baking a texture that contains a shadowmap for the
directional light, then using this texture according to the current shadowmask
mode.

Note: The shadowmask texture is only created if shadowmask_mode is not
LightmapGIData.SHADOWMASK_MODE_NONE. To see a difference, you need to bake
lightmaps again after switching from LightmapGIData.SHADOWMASK_MODE_NONE to
any other mode.

bool supersampling = `false`

  * void set_supersampling_enabled(value: bool)

  * bool is_supersampling_enabled()

If `true`, lightmaps are baked with the texel scale multiplied with
supersampling_factor and downsampled before saving the lightmap (so the
effective texel density is identical to having supersampling disabled).

Supersampling provides increased lightmap quality with less noise, smoother
shadows and better shadowing of small-scale features in objects. However, it
may result in significantly increased bake times and memory usage while baking
lightmaps. Padding is automatically adjusted to avoid increasing light
leaking.

float supersampling_factor = `2.0`

  * void set_supersampling_factor(value: float)

  * float get_supersampling_factor()

The factor by which the texel density is multiplied for supersampling. For
best results, use an integer value. While fractional values are allowed, they
can result in increased light leaking and a blurry lightmap.

Higher values may result in better quality, but also increase bake times and
memory usage while baking.

See supersampling for more information.

float texel_scale = `1.0`

  * void set_texel_scale(value: float)

  * float get_texel_scale()

Scales the lightmap texel density of all meshes for the current bake. This is
a multiplier that builds upon the existing lightmap texel size defined in each
imported 3D scene, along with the per-mesh density multiplier (which is
designed to be used when the same mesh is used at different scales). Lower
values will result in faster bake times.

For example, doubling texel_scale doubles the lightmap texture resolution for
all objects on each axis, so it will quadruple the texel count.

bool use_denoiser = `true`

  * void set_use_denoiser(value: bool)

  * bool is_using_denoiser()

If `true`, uses a GPU-based denoising algorithm on the generated lightmap.
This eliminates most noise within the generated lightmap at the cost of longer
bake times. File sizes are generally not impacted significantly by the use of
a denoiser, although lossless compression may do a better job at compressing a
denoised image.

bool use_texture_for_bounces = `true`

  * void set_use_texture_for_bounces(value: bool)

  * bool is_using_texture_for_bounces()

If `true`, a texture with the lighting information will be generated to speed
up the generation of indirect lighting at the cost of some accuracy. The
geometry might exhibit extra light leak artifacts when using low resolution
lightmaps or UVs that stretch the lightmap significantly across surfaces.
Leave use_texture_for_bounces at its default value of `true` if unsure.

Note: use_texture_for_bounces only has an effect if bounces is set to a value
greater than or equal to `1`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

