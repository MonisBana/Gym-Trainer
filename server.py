from gym import Gym
from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/one')
def one():
    Gym.one()
    return jsonify(msg="one")

@app.route('/two')
def two():
    Gym.two()
    return jsonify(msg="two")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
