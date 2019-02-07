from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():

    # display = request.args.get('display')

    index_file = open('index.html', 'r')
    my_html = index_file.read()

    return my_html

