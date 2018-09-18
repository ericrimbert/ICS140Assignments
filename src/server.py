# imports flask and the render template function to render html files
# then sets the application to name for running and also sets templates and static folder location for calling html/css
from flask import Flask, render_template
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')


# sets index route
@app.route('/')
def index():
    return render_template('index.html')


# sets homework route, this will serve as a basic function for now, and will change depending on file uses
@app.route('/homework.html')
def homework():
    return render_template('homework.html')


# runs the server
if __name__ == "__main__":
    app.run(debug=True, port=9999)
