import ollama

class Tutor:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "english-tutor"

    def get_definition(self):
        prompt = input("Type the word you want to learn: ")
        response = self.client.generate(model=self.model, prompt=prompt)
        print(response.response)
        return response.response
