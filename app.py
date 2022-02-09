from flask import Flask,render_template,request
from numpy import True_

#app = Flask(__name__)

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
     return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True_)
