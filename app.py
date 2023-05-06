from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def calc() -> int:
    text = request.json.get('text', '')
    encoding = request.json.get('encoding', 'cl100k_base')
    tokens = tiktoken.get_encoding(encoding).encode(text)
    return jsonify(tokens=len(tokens))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
