import json
from os.path import abspath


def get_data(file):
    with open(abspath('task_manager/fixtures/{file}'.format(file=file)), 'r') \
            as json_file:
        data = json.load(json_file)
        return data
