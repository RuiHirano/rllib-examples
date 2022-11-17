build:
	docker build -t rllib-examples:latest -f docker/Dockerfile .
run:
	docker run --rm -it rllib-examples:latest bash