from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/<int:times>')
def index1(times):
    return render_template("index.html",time=times)
if __name__=="__main__":
        app.run(debug=True)