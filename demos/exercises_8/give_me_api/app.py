from flask import Flask, send_from_directory, request, jsonify
import hashlib
from collections import Counter

app = Flask(__name__, static_folder='static')


@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/sha256', methods=['POST'])
def api_sha256():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text parameter'}), 400

        text = data['text']

        hash_object = hashlib.sha256(text.encode('utf-8'))
        hex_hash = hash_object.hexdigest()

        return jsonify({'hash': hex_hash})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/calc', methods=['POST'])
def api_calc():
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data or 'op' not in data:
            return jsonify({'error': 'Missing parameters: a, b, op'}), 400

        a = data['a']
        b = data['b']
        op = data['op']

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return jsonify({'error': 'Parameters a and b must be numbers'}), 400

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        else:
            return jsonify({'error': 'Invalid operation. Supported: +, -, *'}), 400

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reverse', methods=['POST'])
def api_reverse():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text parameter'}), 400

        text = data['text']
        reversed_text = text[::-1]

        return jsonify({'reversed': reversed_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/most-freq', methods=['POST'])
def api_most_freq():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text parameter'}), 400

        text = data['text']
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400

        char_count = Counter(text)

        most_frequent_char = char_count.most_common(1)[0][0]

        return jsonify({'most-freq': most_frequent_char})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
