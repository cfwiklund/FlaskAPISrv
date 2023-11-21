from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'Hello, this is a simple API!'
    }
    return jsonify(data)

@app.route('/api/params', methods=['GET'])
def params():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    
    if param1 and param2:
        result = f'Received parameters: param1={param1}, param2={param2}'
    else:
        result = 'Missing parameters'
        
    data = {
        'message': result
    }
    return jsonify(data)

@app.route('/api', methods=['POST'])
def postapi():
    data = request.get_json()  # Get JSON data from the POST request
    if data is not None:
        # Process the received JSON data (you can perform any operation here)
        response = {
            'message': 'POST request successful',
            'data_received': data
        }
        return jsonify(response), 200  # Return a JSON response with a success status code
    else:
        return jsonify({'error': 'Invalid JSON'}), 400  # Return an error response for invalid JSON data


if __name__ == '__main__':
    app.run(debug=True)
