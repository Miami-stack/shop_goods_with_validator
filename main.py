import json
import jsonschema


with open("goods.schema.json") as e:
    data = json.load(e)

for i in data['examples']:
    print(i)
    print(i['name'], i['package_params']['width'], i['package_params']['height'])
    for j in i['location_and_quantity']:
        print(j)

