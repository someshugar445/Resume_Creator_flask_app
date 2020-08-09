#!/usr/bin/env python
# encoding: utf-8

import json
import os
from flask import Flask, request, jsonify
from os.path import join, dirname, realpath

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

#this is get request
@app.route('/', methods=['GET'])
def query_record():
    try:
        name = request.args.get('name')
        print(name)
        with open('data.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
        if name:
            record_found = False
            for record in records:
                if record['name'] == name:
                    name_record = record
                    record_found = True
            if record_found:
                return jsonify(name_record)
            else:
                return "error: name not found"
        else:
            return jsonify(records)
    except Exception as e:
        print("Exception", e)


@app.route('/', methods=['PUT'])
def update_record():
    name = request.args.get('name')
    print(name)
    new_record = json.loads(request.data)
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    record_found = False
    for r in records:
        if r['name'] == new_record['name']:
            old_record = r
            record_found = True
    if record_found:
        records.remove(old_record)
        records.append(new_record)
    else:
        records.append(new_record)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(records)


@app.route('/', methods=['POST'])
def create_record():
    name = request.args.get('name')
    print(name)
    new_record = json.loads(request.data)
    with open('data.txt', 'r') as f:
        data = f.read()
        old_records = json.loads(data)
    record_not_found = False
    for record in old_records:
        if record['name'] != new_record['name'] and record['email'] != new_record['email']:
            record_not_found = True
            add_record = new_record
    if not old_records:
        old_records.append(new_record)
        with open('data.txt', 'w') as f:
            f.write(json.dumps(old_records, indent=2))
        return jsonify(old_records), 201

    elif record_not_found:
        old_records.append(add_record)
        with open('data.txt', 'w') as f:
            f.write(json.dumps(old_records, indent=2))
        return jsonify(old_records), 201
    else:
        return "error': 'name or email already exists"


@app.route('/', methods=['DELETE'])
def delete_record():
    name = request.args.get('name')
    print(name)
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    if name:
        for record in records:
            record_found = False
            if record['name'] == name:
                record_found = True
                name_record = record
        if record_found:
            records.remove(name_record)
            with open('data.txt', 'w') as f:
                f.write(json.dumps(records, indent=2))
            return jsonify(records, {'message': 'record has been deleted'})
        else:
            return jsonify({'error': 'name not found'})
    else:
        for record in records:
            records.remove(record)
        with open('data.txt', 'w') as f:
            f.write(json.dumps(records, indent=2))
        return jsonify(records, {'message': 'All records has been deleted'})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
