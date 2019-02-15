from flask import Flask

app = Flask(__name__)

@app.route('/')
def begin():
    return "<3"

app.run(debug=True, host='0.0.0.0', port=5000)
