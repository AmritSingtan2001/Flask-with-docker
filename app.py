from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def json_endpoint():
    data = request.get_json()
    response = {
        'received': data,
        'message': 'JSON received successfully!'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
