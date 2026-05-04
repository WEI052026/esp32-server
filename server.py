from flask import Flask, request, jsonify

app = Flask(__name__)

cmd = "0"

@app.route("/set", methods=["POST"])
def set_cmd():
    global cmd
    cmd = request.json.get("cmd", "0")
    return jsonify({"cmd": cmd})

@app.route("/get", methods=["GET"])
def get_cmd():
    return jsonify({"cmd": cmd})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)