from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/play')
def display():
    return render_template("display.html")
@app.route('/play/<int:times>')
def display_box(times):
    return render_template("display.html",time= times )
@app.route('/play/<int:times>/<color>')
def display_color(times,color):
    print(times, color)
    return render_template('display.html',time=times, col=color)
if __name__=="__main__":
        app.run(debug=True)
