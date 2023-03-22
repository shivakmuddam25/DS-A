# Step 1 - To import FLASK
from flask import Flask, request, render_template

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)


###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality

# @app.route('/', methods=['GET'])
# def home_page():
#     return render_template('home_old.html')
#

# @app.route('/search', methods=['GET', 'POST'])
# def search_fun():
#     if request.method == 'POST':
#         return "Welcome to the search page using POST Req"
#     else:
#         return render_template('search.html')


@app.route('/', methods=['POST', 'GET'])
def add_fun():
    # if request.method == 'POST':
    res = request.form.get('var_1')
    print(res)
    return render_template("home.html", result=res)

###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)
