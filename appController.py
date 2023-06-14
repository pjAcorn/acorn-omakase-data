from flask import Flask, request, json, jsonify
from flask_cors import CORS

PORT_NUM = 8000

app = Flask(__name__)

@app.route("/test", methods=['POST'])
def test():
    params = request.get_json()
    print("받은 데이터 ", params)

    response = {
        "result": "OK"
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT_NUM)