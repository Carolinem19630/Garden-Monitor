#defines the webserver for data viewing / configuration
from flask import Flask, render_template
import random

app = Flask(__name__)

#TODO: define api for configuring stuffs

#endpoint for getting sensor data (realtime)
@app.route('/sensor_<name>')
def send_sensor(name):
    return str(random.random()) #dummy implementation

#endpoint for getting nice graphs
@app.route('/graph_<name>.png')
def send_graph(name):
    return

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
