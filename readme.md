## Running models locally with Ollama
The main goal of this project is to help you run a free llm model on your computer to help with basic tasks, such as improving your vocabulary in a new language.

### Download and install ollama
- The first step is to download ollama on your computer through their [website](https://ollama.com/)

### Select the preferred model
- After downloading ollama, you'll need to select a [Model](https://ollama.com/search)
- Every model has its own tags that stands for its size (number of parameters), if its able to connect to a mcp server, etc.

### Get the model to your machine
- The next step after selecting the model is to pull it into your computer. For this, use this command
```
ollama pull <model>
```
- You can later check which models you have available using the command:
```
ollama list
```

### Run the model
- Finally, to run the model, the only thing needed is to type
```
ollama run <model>
```
---

### Python alternative to CLI
- If instead of running the model using the terminal directly, you can install a library called [ollama](https://pypi.org/project/ollama/) using **pip**

- After installing the library, simply create a python file to call the model using a prompt like the template script below

```Python
import ollama

class Tutor:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "qwen3.5:4b"

    def get_definition(self):
        prompt = "Your prompt to the model"
        response = self.client.generate(model=self.model, prompt=prompt)
        print(response.response)
        return response.response

```
---
## Fine tune the model

### Modelfile
- By creating a Modelfile, you can give context to the model on what and how it should answer the user input
- In the Modelfile, there is the keyword SYSTEM that enables you to write how the model should answer. Along with the SYSTEM, you need to pass the model you want to use via the key word FROM 'model-name'
- After writing the instructions to the model, you can create a new model by typing
```
ollama create <chosen_model_name> -f /path/to/Modelfile 
```
- After creating you customized model, you can use in the terminal or in the python file
