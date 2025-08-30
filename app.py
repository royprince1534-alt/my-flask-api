from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello Dev! 👋 Ye tumhari first API hai!"

# Example API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Dev",
        "message": "API chal rahi hai 🚀",
        "status": "success"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)