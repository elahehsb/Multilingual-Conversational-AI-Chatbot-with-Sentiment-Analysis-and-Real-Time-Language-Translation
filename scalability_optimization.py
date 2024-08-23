import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ScalableChatbot:
    def __init__(self, model_name="gpt-3"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def batch_generate_responses(self, prompts):
        inputs = self.tokenizer(prompts, return_tensors="pt", padding=True)
        outputs = self.model.generate(inputs.input_ids, max_length=150)
        responses = [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        return responses

if __name__ == "__main__":
    bot = ScalableChatbot()
    responses = bot.batch_generate_responses(["Hello, how are you?", "What is the weather today?"])
    print("Batch Responses:", responses)
