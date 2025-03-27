# LightmapProbe

Inherits: Node3D < Node < Object

Represents a single manually placed probe for dynamic object lighting with
LightmapGI.

## Description

LightmapProbe represents the position of a single manually placed probe for
dynamic object lighting with LightmapGI. Lightmap probes affect the lighting
of GeometryInstance3D-derived nodes that have their GeometryInstance3D.gi_mode
set to GeometryInstance3D.GI_MODE_DYNAMIC.

Typically, LightmapGI probes are placed automatically by setting
LightmapGI.generate_probes_subdiv to a value other than
LightmapGI.GENERATE_PROBES_DISABLED. By creating LightmapProbe nodes before
baking lightmaps, you can add more probes in specific areas for greater
detail, or disable automatic generation and rely only on manually placed
probes instead.

Note: LightmapProbe nodes that are placed after baking lightmaps are ignored
by dynamic objects. You must bake lightmaps again after creating or modifying
LightmapProbes for the probes to be effective.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

