from flask import Flask, request, render_template, redirect
from requests import get

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        ip = request.form.get('ip')
        data = get('https://ipapi.co/' + ip + '/json/').json()
        return render_template('index.html', data=data)
    elif request.method == "GET":
        if request.args != '':
            ip = request.args
            data = get('https://ipapi.co/' + ip[1] + '/json/').json()
            return render_template('index.html', data=data)
        else:
            return render_template('index.html')
            

if __name__ == "__main__":
    app.run(debug=True)