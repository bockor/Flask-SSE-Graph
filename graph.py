# Ref: https://medium.com/@01one/simple-server-sent-events-sse-with-python-flask-0259e93162d1
# Invoke using: python3 graph.py

from flask import Flask, Response, render_template
import time
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('graph.html')

@app.route("/listen")
def listen():

    def send_update_to_client():
        while True:
            with open("graph_data.json", "r") as fin:
                _data = json.load(fin)
                yield f"id: 1\ndata: {json.dumps(_data)}\nevent: online\n\n"
                time.sleep(5)

    return Response(send_update_to_client(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)