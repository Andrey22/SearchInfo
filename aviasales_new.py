import requests
import pprint
import re
import json

flight_params = {
    'origin': 'MOW',
    'destination': 'AER',
    'one_way': 'true'
}
country_params = {"iata": "MOW",
        "name": "Moscow"}

direction_params = {
    "origin_iata=":"LED",
    'one_way': 'false'
    }

search_hg = r'MOW'

req = requests.get("http://min-prices.aviasales.ru/calendar_preload", params=flight_params)
#country_get = requests.get('http://api.travelpayouts.com/data/ru/countries.json', params=country_params)

direction_get = requests.get('http://map.aviasales.ru/supported_directions.json')
city_get = requests.get('http://api.travelpayouts.com/data/ru/cities.json')
city_text = city_get.text
#pprint.pprint(city_text)

city_json = json.loads(city_text)

re.findall(r'MOW', city_json)

#for i in city_json:
#    moscow = re.search(r'MOW', i)
#    print(moscow)


#re.findall(search_hg, city_text)

#qq = requests.get('https://www.travelpayouts.com/widgets_suggest_params')

#pprint.pprint(datta)

#country_data = country_get.json()
#pprint.pprint(country_get.json())

#pprint.pprint(direction_get.json())


#data = req.json()
#pprint.pprint(data)

#print(data)

#print(req)
#print(data)

#data_direction = direction_get.json()
#pprint.pprint(data_direction)
#tickets = data['best_prices']
#pprint.pprint(tickets)
#for ticket in tickets:
    #if ticket['value'] < 3000:
        #print(ticket)

