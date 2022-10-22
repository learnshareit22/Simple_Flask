from msilib.schema import Error
from flask import Flask, render_template, request
import model
# Create flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/solution", methods = ["POST"])
def solution():
    parameter = [float(x) for x in request.form.values()]  
    a = parameter[0]
    b = parameter[1]
    c = parameter[2]
    solution = model.quadratic(a,b,c)
    if solution == None:
        return render_template("index.html", text = "No solution")
    return render_template("index.html", text = "Solution of the equation is {}".format(solution))

if __name__ == "__main__":
    flask_app.run(debug=True)