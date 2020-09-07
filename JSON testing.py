import json
with open('C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\task\\hypernews\\news.json', 'r') as json_file:
    dict_from_json = json.load(json_file)
print(dict_from_json[0]['created'])
