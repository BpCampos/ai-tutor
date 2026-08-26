## Running models locally with Ollama

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

### Python alternative do CLI
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
