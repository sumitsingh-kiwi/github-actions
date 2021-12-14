from flask import Flask
app = Flask(__name__, template_folder='templates')
from flask import request
from flask import render_template


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


#url_for('static', filename='style.css')
#app = Flask(__name__,
#            static_url_path='', 
#            static_folder='web/static',
#            template_folder='web/templates')
