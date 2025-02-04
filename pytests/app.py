from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi, this is Darvin Xavier, 2024 graduate from Sathyabama Institute of Science and Technology."

@app.route('/health')
def health_check():
    return jsonify(status="OK"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
