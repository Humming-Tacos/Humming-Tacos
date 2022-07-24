class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tacos:
    """Tacos Object to combine the audio processing functions.
    """    
    def __init__(self, transcribe, compose, synthesize, proc_name='HummingTACOS'):
        """Tacos Object's initializer.

        Args:
            transcribe (function): Function that takes in an input humming wav file, then outputs a transcribed midi file.
            compose (function): Function that takes in a transcribed midi file and outputs a generated midi composition.
            synthesize (function): Function that takes in a midi composition, and outputs a synthesized wav file.
            proc_name (str, optional): The logged process name. Defaults to 'HummingTACOS'.
        """        
        self.transcribe = transcribe
        self.compose = compose
        self.synthesize = synthesize
        self.PROC_NAME = f'{bcolors.BOLD}{bcolors.UNDERLINE}[{proc_name}]{bcolors.ENDC}'
        

    def process(self, humming_wav_path):
        """Process given humming wav audio, then generates and output the path of a music composition based on the humming.

        Args:
            humming_wav_path (path): Path to the input humming wav recording.

        Returns:
            synthesized_wav_path (path): Path to the output synthesized wav composition.
        """        
        # Transcribe
        print(self.PROC_NAME, f'TRANSCRIBE HUMMING: {humming_wav_path}')
        humming_midi_path = self.transcribe(humming_wav_path)
        print(self.PROC_NAME, f'TRANSCRIBED HUMMING: {humming_midi_path}')

        # Composition
        print(self.PROC_NAME, f'COMPOSE HUMMING WITH: {humming_midi_path}')
        composition_midi_path = self.compose(humming_midi_path)
        print(self.PROC_NAME, f'COMPOSED HUMMING: {composition_midi_path}')

        # Synthesize
        print(self.PROC_NAME, f'SYNTHESIZING HUMMING WITH: {composition_midi_path}')
        synthesized_wav_path = self.synthesize(composition_midi_path)
        print(self.PROC_NAME, f'SYNTHESIZED HUMMING: {synthesized_wav_path}')

        # equivalent to: self.synthesize(self.compose(self.transcribe(humming_wav_path)))
        return synthesized_wav_path


