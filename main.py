import os
import json
from flask import Flask , request , Response

app = Flask(__name__)

port = os.getenv('PORT')

@app.route("/")
def hello():
    return "Augury Test!"

@app.route("/get_variable/<name>")
def get_env_variable(name):
    env_variable = os.getenv(name)
    if env_variable is None:
        return "",500
    else:
      result = {"variable_name": name, "variable_value": env_variable}
      return json.dumps(result)

@app.route("/healthy")
def health():
    return json.dumps({"status": "ok"}),200

@app.post('/set_variable')
def set_variable():
    data = request.json
    variable_name = data["name"]
    variable_value = data["value"]
    if os.getenv(variable_name) is None:
        os.environ.setdefault(variable_name, variable_value)
    else:
        os.environ[variable_name] = str(variable_value)
    return Response(variable_value)

app.run('localhost',port=port)