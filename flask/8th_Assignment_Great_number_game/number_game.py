from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session['random_number'] = random.randint(1, 100)
    print (session['random_number'])
    return render_template('index.html')
@app.route('/<int:guess>', methods=['POST'])
def result():
    if int(request.form['guess']) == int(session['random_number']):
        session['answer'] = "This is the number"
        return render_template("index.html", answer=answer)
    elif int(request.form['guess']) > int(session['random_number']):
        session['answer'] = "Too Low"
        return render_template("index.html", answer=answer)
    else:
        session['answer'] = "Too High"
        return render_template("index.html", answer=answer)

if __name__=="__main__":   
    app.run(debug=True)   