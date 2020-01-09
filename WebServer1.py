from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/', methods=['GET','POST'])
def foo():
    subprocess.Popen("GUI1.py 1", shell=True)
    os._exit(0)
    return

if __name__ == '__main__':
    app.run(debug=False)
