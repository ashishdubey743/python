from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Dummy data for demonstration
    data = {'message': 'Hello'}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    # Get JSON data from the request body
    request_data = request.get_json()

    # Dummy processing
    processed_data = {'message': f"This is a POST request with data: {request_data}"}

    return jsonify(processed_data), 201

if __name__ == '__main__':
    app.run(debug=True)
