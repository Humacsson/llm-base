make: build base.env start

build:
	docker build -t llm-base-gradio .

base.env:
	cp base.example.env base.env

start:
	docker run \
	-ti \
	--env-file base.env \
	-p 7860:7860 \
	-v $(shell pwd):/gradio \
	llm-base-gradio sh ./scripts/run.sh
sh:
	docker run -it -v $(shell pwd):/gradio llm-base-gradio sh

