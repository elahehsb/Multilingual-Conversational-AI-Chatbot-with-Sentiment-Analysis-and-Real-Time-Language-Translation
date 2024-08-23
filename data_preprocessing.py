import re
import torchaudio
from torchaudio.transforms import Resample

def preprocess_text(text):
    # Basic text preprocessing: lowercasing, removing special characters, etc.
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def preprocess_speech(audio_file, new_sample_rate=16000):
    # Resampling audio to a common sample rate
    waveform, sample_rate = torchaudio.load(audio_file)
    resampler = Resample(orig_freq=sample_rate, new_freq=new_sample_rate)
    waveform = resampler(waveform)
    return waveform

if __name__ == "__main__":
    sample_text = "Hello, World!"
    processed_text = preprocess_text(sample_text)
    print("Processed Text:", processed_text)
    
    sample_audio = "path_to_audio.wav"
    processed_audio = preprocess_speech(sample_audio)
    print("Processed Audio:", processed_audio.shape)
