from flask import Flask, request, render_template, redirect
from requests import get

app = Flask(__name__)

addresses = []

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        ip = request.form.get('ip')
        data = get('https://ipapi.co/' + ip + '/json/').json()
        addresses.append([ip, '?ip=' + ip])
        return render_template('index.html', data=data, addresses=addresses)
    elif request.method == "GET":
        args = request.args
        if "ip" in args:
            ip = args["ip"]
            data = get('https://ipapi.co/' + ip + '/json/').json()
            return render_template('index.html', data=data, addresses=addresses)
        else:
            return render_template('index.html', addresses=addresses)
            
if __name__ == "__main__":
    app.run(debug=True)