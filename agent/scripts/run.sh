litellm --model ollama/llama3 --api_base http://host.docker.internal:11434 &
P1=$!

python agent.py &
P2=$!

# Make sure all running processes can be stopped with ctrl-c
wait $P1 $P2

