"""Получение json и запись значений этого json'a в базу."""
import json
import os
import sys

import jsonschema


def default_json(file: str) -> dict:
    """Эта функция читает схему json."""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, file)
    with open(file_path) as f:
        data = json.load(f)
        return data


def input_json(file: str) -> dict:
    """Эта функция читает json файл, который подается."""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, file)
    if os.path.splitext(file_path)[1] == '.json':
        with open(file_path) as e:
            data = json.load(e)
            return data
    else:
        print('Это не json файл')
        sys.exit(0)


def validation_json(data: dict, data2: dict) -> str:
    """Эта функция валидирует поданный json со схемой."""
    try:
        jsonschema.validate(data, data2)
        return "Json валидный"
    except jsonschema.exceptions.ValidationError:
        return "Json невалидный"
    except json.decoder.JSONDecodeError:
        return "Json невалидный"


def add_values(data: dict):
    goods = [data['id'], data['name'], data['package_params']['width'], data['package_params']['height']]
    shop_goods = []
    for i in data['location_and_quantity']:
        shop_goods.append(i['location'])
        shop_goods.append(i['amount'])
    return goods, shop_goods


input_data = input_json('file.json')
schema = default_json('goods.schema.json')

goods, shoops = add_values(input_data)
print(input_data, '\n', validation_json(input_data, schema), '\n', t, v)
