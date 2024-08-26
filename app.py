from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

# models/encodings from tiktoken
# https://github.com/openai/tiktoken/blob/c0ba74c238d18b4824c25f3c27fc8698055b9a76/tiktoken/model.py#L9
# "gpt-4o-": "o200k_base",  # e.g., gpt-4o-2024-05-13
# "gpt-4-": "cl100k_base",  # e.g., gpt-4-0314, etc., plus gpt-4-32k


# Predownload the encodings for the models
tiktoken.encoding_for_model("gpt-4o").encode_ordinary("warmup")


@app.route("/count", methods=["POST"])
def calculate():
    text: str = request.json.get("text", "")
    model: str = request.json.get("model", "gpt-4o")

    encoding: str = tiktoken.encoding_name_for_model(model)
    tokens = tiktoken.get_encoding(encoding).encode_ordinary(text)

    return jsonify(tokens=len(tokens), encoding=encoding)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
