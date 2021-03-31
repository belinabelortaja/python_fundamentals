@app.route('/')
def HelloWorld():
    return "Hello World"
@app.route('/dashboard')
def dashboard():
    return "This is a dashboard"
@app.route('/dashboard/<name>/<int:year>/<int:id>')   
def dashboardItem (name, year, id)
    return name + "" + str(year) + " " str(id)