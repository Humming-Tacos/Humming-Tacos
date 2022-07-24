from HummingTACOS import Tacos

import XTranscribe
import XGeneration
import XSynthesis


if __name__ == '__main__':

    # creating Taco object :D
    tacos = Tacos(
        transcribe=XTranscribe.transcribe, 
        compose=XGeneration.compose, 
        synthesize=XSynthesis.synthesize) 


    # Example input output
    input_humming_wav_path = 'example_input/mjve.wav'
    output_music_wav_path = tacos.process(input_humming_wav_path)
    print(output_music_wav_path)

