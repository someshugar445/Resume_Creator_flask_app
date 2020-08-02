from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

quarks = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]


@app.route('/quarks', methods=['GET'])
def return_all():
    return jsonify({'quarks': quarks})


@app.route('/quarks/<string:name>', methods=['GET'])
def return_one(name):
    theOne = quarks[0]
    for i, q in enumerate(quarks):
        if q['name'] == name:
            theOne = quarks[i]
    return jsonify({'quarks': theOne})


@app.route('/quarks', methods=['POST'])
def add_one():
    new_quark = request.get_json()
    quarks.append(new_quark)
    return jsonify({'quarks': quarks})


@app.route('/quarks/<string:name>', methods=['PUT'])
def edit_one(name):
    new_quark = request.get_json()
    for i, q in enumerate(quarks):
        if q['name'] == name:
            quarks[i] = new_quark
    qs = request.get_json()
    return jsonify({'quarks': quarks})


@app.route('/quarks/<string:name>', methods=['DELETE'])
def delete_one(name):
    for i, q in enumerate(quarks):
        if q['name'] == name:
            del quarks[i]
    return jsonify({'quarks': quarks})


if __name__ == "__main__":
    app.run(debug=True)
