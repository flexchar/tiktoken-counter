GITHUB_USER=flexchar
IMAGE_NAME=tiktoken-counter
CONTAINER_NAME=tiktoken-counter
PLATFORMS=linux/amd64,linux/arm64
BUILDER_NAME=$(IMAGE_NAME)-builder
REMOTE_TAG=ghcr.io/$(GITHUB_USER)/$(IMAGE_NAME)

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

publish:
	docker buildx create --use --name $(BUILDER_NAME) || true
	docker buildx build --platform $(PLATFORMS) -t $(REMOTE_TAG) --push .
	docker buildx rm $(BUILDER_NAME)