import json
import os

class TestData:
    def __init__(self):
        self.json_path = os.path.realpath('../resources/test_data')

    def get_data(self, test_name, type_of_data, data):
        with open(self.json_path + '/' + test_name + '.json', 'r') as json_file:
            json_data = json_file.read()
        json_object = json.loads(json_data)
        return json_object[type_of_data][data]
