# from application.main.controller.strain.strain import StrainAPI

from ast import literal_eval
# from application.main.strain.strain import API_KEY
import requests
import json

API_KEY = 'GFPrSmY'

class StrainAPI:
    def __init__(self):
        self.url = f'http://strainapi.evanbusse.com/{API_KEY}'

    def convert_bytes(self, bytes: bytes):

        strains = bytes
        my_json = strains.decode("UTF-8")
        return my_json


    def convert_to_json(self, data: dict, outfile: str, indent=4):

        my_json = json.loads(data)

        with open(outfile, 'w') as outfile:
            json.dump(my_json, outfile, indent=indent)

        #TODO Should it be my_json and not data?


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

    def strain_by_race(self,race) -> list:
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


temp = bot.get_all_strains()

gelato = bot.strain_by_name('Gorilla Glue')
print(gelato)

    
   