# Tiktoken Counter

Tiktoken Counter is an API for counting tokens in a text using the Tiktoken library. The API is built using Flask and served with Gunicorn. The Docker image is available at `ghcr.io/flexchar/tiktoken-counter`.

## Purpose

This API is designed to help developers count tokens in a given text, from another service/language, which is particularly useful when working with OpenAI's GPT models, such as GPT-4o. By utilizing the Tiktoken library, this API provides a simple way to count tokens for specific encodings.

> For example, I use it from inside Laravel (php) code base where I need to estimate tokens without calling any APIs outside the server. Docker makes it super easy to expand with the microservice concept.

## Building the Docker Image

To build the Docker image, simply run the following command in your terminal:

```bash
make build
```

This command will build the Docker image with the tag `tiktoken-counter`.

## Running the API

To run the API, use the following command:

```bash
make run
```

This command will start the API on port 8000.

## Pushing the Docker Image

To push the Docker image to GitHub Container Registry, use the following command:

```bash
make push
```

This command will tag the image with your GitHub username and push it to the registry.

## Example Usage

Here is an example of how to use the API for counting tokens:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, World!", "model": "gpt-4o"}' http://localhost:8000/count
```

This request will return the number of tokens in the given text.

```json
{
    "tokens": 5,
    "encoding": "o200k_base"
}
```

In this example, the `text` parameter contains the text for which you want to count tokens, and the `model` parameter specifies the encoding used for tokenization. The default model is `gpt-4o`.
