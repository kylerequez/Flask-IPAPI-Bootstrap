from flask import Flask, request, render_template
import ipapi

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    ip = request.form.get('ip')
    data = ipapi.location(ip=ip, output='json')
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)