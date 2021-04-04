from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template('index.html', counter=session['count'])

@app.route('/plus_two', methods=['POST'])
def addTwo():
    session['count']+=1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count']=0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
