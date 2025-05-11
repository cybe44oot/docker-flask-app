from flask import Flask

app = Flask(_name)  # Use __name_ instead of name

@app.route("/")
def hello():
    return "Hello yall my geeks from Dockerized Flask App!"  # Proper indentation

if _name_ == "_main":  #  Use __name_ and "_main_"
    app.run(host="0.0.0.0", port=5000, debug=True)