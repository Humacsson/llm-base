make: docker data start

docker:
	docker build \
		--platform=linux/amd64 \
		-t \
		llm-base-rag .

data:
	docker run \
		--env-file=docker.env \
		-v $(shell pwd):/rag \
		-w /rag/data \
		llm-base-rag wget --input-file ../data_links.txt

start:
	docker run \
	-ti \
	--env-file=docker.env \
	-p 7860:7860 \
	-v $(shell pwd):/rag \
	llm-base-rag python run.py

sh:
	docker run -it -v $(shell pwd):/rag llm-base-rag sh

