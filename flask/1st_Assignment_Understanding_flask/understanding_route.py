from flask import Flask  
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')
def dojo():
    return 'Dojo'
@app.route('/say/<name>')
def say(name):
    return 'Hi '+ name.capitalize() +'!'
@app.route('/repeat/<numb>/<name>')
def num(numb,name):
    n=int(numb)
    newName=name*n
    return newName
if __name__=="__main__":   
    app.run(debug=True)