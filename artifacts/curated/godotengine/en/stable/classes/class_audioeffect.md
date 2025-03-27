# AudioEffect

Inherits: Resource < RefCounted < Object

Inherited By: AudioEffectAmplify, AudioEffectCapture, AudioEffectChorus,
AudioEffectCompressor, AudioEffectDelay, AudioEffectDistortion, AudioEffectEQ,
AudioEffectFilter, AudioEffectHardLimiter, AudioEffectLimiter,
AudioEffectPanner, AudioEffectPhaser, AudioEffectPitchShift,
AudioEffectRecord, AudioEffectReverb, AudioEffectSpectrumAnalyzer,
AudioEffectStereoEnhance

Base class for audio effect resources.

## Description

The base Resource for every audio effect. In the editor, an audio effect can
be added to the current bus layout through the Audio panel. At run-time, it is
also possible to manipulate audio effects through
AudioServer.add_bus_effect(), AudioServer.remove_bus_effect(), and
AudioServer.get_bus_effect().

When applied on a bus, an audio effect creates a corresponding
AudioEffectInstance. The instance is directly responsible for manipulating the
sound, based on the original audio effect's properties.

## Tutorials

  * Audio buses

  * Audio Microphone Record Demo

## Methods

AudioEffectInstance | _instantiate() virtual  
---|---  
  
## Method Descriptions

AudioEffectInstance _instantiate() virtual

Override this method to customize the AudioEffectInstance created when this
effect is applied on a bus in the editor's Audio panel, or through
AudioServer.add_bus_effect().

    
    
    extends AudioEffect
    
    @export var strength = 4.0
    
    func _instantiate():
        var effect = CustomAudioEffectInstance.new()
        effect.base = self
    
        return effect
    

Note: It is recommended to keep a reference to the original AudioEffect in the
new instance. Depending on the implementation this allows the effect instance
to listen for changes at run-time and be modified accordingly.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.

