
import re
import requests
import pprint
import json


json_file = open('cities.json','r')
city_json = json.load(json_file)

json_file.close()
print(type(city_json))
