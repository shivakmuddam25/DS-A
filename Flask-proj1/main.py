from flask import request, Flask
import json

app = Flask(__name__)


# @app.route("/")
# def home_page():
#     message = "Welcome to the homepage."
#     return message


@app.route("/", methods=["Get"])
def home():
    username = request.args.get("username")
    # password = request.args.get("password")
    if username is None:
        username = ""
    message = "Dear " + str(username.upper()) + " Welcome to the Home page"
    return message


# @app.route("/query", methods=["Get"])
# def query():
#     username = request.args.get("user")
#     return "Welcome to the Home page" + str(username.upper())


if __name__ == "__main__":
    app.run()
