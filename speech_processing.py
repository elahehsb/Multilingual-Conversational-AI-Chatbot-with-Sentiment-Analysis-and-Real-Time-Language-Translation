import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, T5ForConditionalGeneration, T5Tokenizer

class SpeechProcessor:
    def __init__(self):
        self.stt_processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
        self.stt_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
        self.tts_model = T5ForConditionalGeneration.from_pretrained("t5-small")
        self.tts_tokenizer = T5Tokenizer.from_pretrained("t5-small")
    
    def speech_to_text(self, audio):
        input_values = self.stt_processor(audio, return_tensors="pt", padding="longest").input_values
        logits = self.stt_model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.stt_processor.decode(predicted_ids[0])
        return transcription
    
    def text_to_speech(self, text):
        input_ids = self.tts_tokenizer(text, return_tensors="pt").input_ids
        outputs = self.tts_model.generate(input_ids)
        return self.tts_tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    processor = SpeechProcessor()
    speech_text = processor.speech_to_text("path_to_audio.wav")
    print("Transcribed Text:", speech_text)
    
    synthesized_speech = processor.text_to_speech("Hello, how can I help you?")
    print("Synthesized Speech:", synthesized_speech)
