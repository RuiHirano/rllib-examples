cmd=bash
build:
	docker build -t rllib-examples:latest -f docker/Dockerfile .
run:
	docker run --rm -v ${PWD}:/workspace/rllib-examples -it rllib-examples:latest ${cmd}