import datetime
import sys

from flask import Flask, request, Response, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/noderedchart")
def noderedchart():
    return render_template('graphfromnodered.html')


if __name__ == '__main__':
   try:
        
        app.run(debug=True,host='0.0.0.0')
        print("Web server is waiting for requests")
   except:
        print("Exception")
        err = sys.exc_info()
        print(err[0])
        print(err[1])
        #for i in range(len(err())):
        #     print(err[i])
