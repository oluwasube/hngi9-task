from flask import Flask
import json
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'], strict_slashes=False)
def home_page():
  data_set = {
    'slackUsername':'Oluwasube',
    'backend': True,
    'age':25,
    'bio':'I am a backend engineer who derive pleasure in solving problems using codes'
  }
  result =json.dumps(data_set)
  return result

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)