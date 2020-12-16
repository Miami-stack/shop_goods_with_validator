import json
import os
import sys

import jsonschema


def default_json(file: str):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, file)
    with open(file_path) as f:
        data = json.load(f)
        return data


def check_input_json(file: str):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, file)
    if os.path.splitext(file_path)[1] == '.json':
        with open(file_path) as e:
            data = json.load(e)
            return data
    else:
        print('Это не json файл')
        sys.exit(0)


schema = default_json('goods.schema.json')
input_data = check_input_json('file.json')

valid = jsonschema.validate(input_data, schema)

print(input_data, valid)
