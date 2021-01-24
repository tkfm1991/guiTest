import json

json_open = open('main_template.json', 'r')
json_load = json.load(json_open)

print(json_load)

for data in json_load:
    print(data)

print('---')

for data in json_load.values():
    print(data)

print('---')

for k in json_load.keys():
    print(k)

print('---')

for k, v in json_load.items():
    # print(k, v)
    print(json_load[k]['element_type'])