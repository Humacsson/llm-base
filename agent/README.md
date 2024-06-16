## Dependencies

Make sure you have both docker and Ollama installed on your machine.

### Ollama
You can download ollama here:
https://ollama.com

Install the model you want to use with: 
```ollama pull llama3``` (replace `llama3` with your model of choice)

Make sure the model is installed by running:
```ollama run llama3``` (replace `llama3` with your model of choice)

Or run the list command:
```ollama list```

Also, make sure the ollama web server is running with:
```curl localhost:11434```

### Docker
For docker, on mac I recommend installing the docker client and Colima.

Colima will run the docker containers instead of something much heavier like Docker Desktop (not recommended due to privacy concerns and just plain size):
`brew install colima`

Read more here: https://github.com/abiosoft/colima

Make sure colima is installed with:
```colima list```

There should be at least one item running returned.

If not, run:
```colima start```

Once colima is installed, install the docker CLI:
`brew install docker`

Make sure docker is running with:
```docker run hello-world```

## Run the UI
Run `make` to start the UI.

Now access it at: http://localhost:7860

You can change the variables in the base.env file to change the prompt file or the model in use. If you change a file then rerun the script for the changes to take effect. I am working on making hot-reloading work but haven't gotten there just yet.

If you get an error when chatting with the model, check the error message in the terminal.

## Recommended Models for Japanese
- aya
- qwen2:7b

See all available models at the ollama website:
https://ollama.com/library
