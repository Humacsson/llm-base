litellm --model ollama/llama3 --api_base http://host.docker.internal:11434 &

echo -n 'Waiting for litellm'
# Use weget to check if the URL is up: 
#   --spider speeds up the check by not downloading the content
#   2> dev/null hides error message
until wget --spider localhost:4000 2> /dev/null
do
  echo -n '.'
  sleep 1
done

echo 'Connection established! Running agent...'

python agent.py
