from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_wolrd():
  return "<h2>Hello world!</h2>"

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"}), 200

def not_found(error):
    return jsonify({"error": "Route not found"}), 404
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)