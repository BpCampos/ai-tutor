import ollama

client = ollama.Client()

model = "english-tutor"

prompt = input("Write the word you want to understand: ")

response = client.generate(model=model, prompt=prompt)

print(f"{response.response}")