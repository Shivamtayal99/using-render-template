from flask import Flask, jsonify,render_template
from multiprocessing import Value

app = Flask(__name__)
@app.route('/')
def result():
    return render_template('index.html')


app.run(port=5001,debug=True)