from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/return', methods=["POST"])
def ret_form():
        return render_template("return.html", name=request.form['name'], location=request.form['locations'],language=request.form['languages'],comment=request.form['comments'], gender=request.form['gender'], system=request.form['op_system'])
@app.route('/index', methods=["GET"])
def go_back():
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)