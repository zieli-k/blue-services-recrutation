import os
import json


class Config:

    def __init__(self):
        self.json_path = os.path.realpath('../resources/config')

    def get_config(self, env):
        with open(self.json_path + '/' + env + '.json', 'r') as json_file:
            json_data = json_file.read()
        return json_data

    def get_url(self, env):
        json_object = json.loads(self.get_config(env))
        return json_object['url']
