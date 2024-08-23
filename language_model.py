from transformers import AutoModelForCausalLM, AutoTokenizer

class Chatbot:
    def __init__(self, model_name="gpt-3"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
    
    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs.input_ids, max_length=150)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

if __name__ == "__main__":
    bot = Chatbot(model_name="gpt-3")
    response = bot.generate_response("How are you?")
    print("Chatbot Response:", response)
