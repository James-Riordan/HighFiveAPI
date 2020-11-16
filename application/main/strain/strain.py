import sys
from typing import Dict
from typing import List
from typing import Optional
from pprint import pprint
import json
import ast
import requests

sys.path.append("../../")

from config import Config

API_KEY = Config.API_KEY


class StrainAPI:
    def __init__(self):
        self.url = f'http://strainapi.evanbusse.com/{API_KEY}'

    def convert_bytes(self, bytes: bytes):

        strains = bytes
        dict_str = strains.decode("UTF-8")
        decoded_data = ast.literal_eval(dict_str)

        return decoded_data

    def convert_to_json(self, data: str, outfile: str, indent=4):

        with open(outfile, 'w') as outfile:
            json.dump(data, outfile, indent=indent)

    def get_all_strains(self) -> dict:

        url = self.url + '/strains/search/all'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = {'STRAIN_NAME': {'id': int, 'race': 'string', 'flavors': [], 'effects': {'positive': [], 'negative': [], 'medical': []}}}
        return decoded_data

    def strain_by_name(self, name) -> list:

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/search/name/{name}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = [{'desc', 'id', 'name', 'race'}]
        return decoded_data

    def strain_by_race(self, race) -> list:
        # Sativa, Indica, Hybrid

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/search/race/{race}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = [{'id', 'name', 'race'}]
        return decoded_data

    def strain_by_effect(self, effect) -> list:

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/search/effect/{effect}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        return decoded_data

    def strain_by_flavor(self, flavor):

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/search/flavor/{flavor}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = [{'flavor', 'id', 'name', 'race'}]
        return decoded_data

    def strain_description(self, strain_id=None, strain_name=None) -> dict:

        if strain_id == None and StrainAPI.strain_by_name({strain_name}):
            strain_id = StrainAPI.strain_by_name({strain_name})[0]['id']

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/data/desc/{strain_id}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = {'desc'}
        return decoded_data

    def strain_effects(self, strain_id=None, strain_name=None) -> dict:

        if strain_id == None and StrainAPI.strain_by_name({strain_name}):
            strain_id = StrainAPI.strain_by_name({strain_name})[0]['id']

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/data/effects/{strain_id}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        # decoded_data = {'medical': [], 'negative': [], 'positive': []}
        return decoded_data

    def get_strain_flavors(self, strain_id=None, strain_name=None) -> list:

        url = f'http://strainapi.evanbusse.com/{API_KEY}/strains/data/flavors/{strain_id}'
        content = requests.get(url).content
        decoded_data = self.convert_bytes(content)

        return decoded_data


bot = StrainAPI()


# Add data to strain.json

if __name__ == "__main__":
    bot.convert_to_json(bot.get_all_strains(), '../data/strain.json')
    
