import os
from flask import Flask, render_template, request, json

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

@app.route("/")
def hello_world():
    
    if request.method == 'POST':
        return 'wtf are you doing'
    else:
        poem_url =  json_url = os.path.join(SITE_ROOT, "poems", "poem.json")
        # with open(poem_url) as f:
        #     file_content = f.read()
        # return render_template('index.html', poem=file_content)
        poem = json.load(open(poem_url))
        print(poem)
        return render_template('index.html', title=poem["title"], poem=poem["text"])

@app.route("/<month>")
def month(m):
    if request.method == 'POST':
        return 'wtf are you doing'
    else:
        return render_template('archive.html', month=m)


