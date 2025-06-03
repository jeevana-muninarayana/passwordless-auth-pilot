from flask import Flask, jsonify
from webauthn import generate_registration_options

app = Flask(__name__)

@app.route("/register", methods=["GET"])
def register():
    options = generate_registration_options(user_id="demo-user", username="demo")
    return jsonify(options.dict())

if __name__ == "__main__":
    app.run(debug=True)