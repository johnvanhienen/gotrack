import requests
import json


class Location:
    def lookupposition(address, apikey):
        position_url = "https://geocode.search.hereapi.com/v1/geocode"
        position_payload = {
            'q': address,
            'apiKey': apikey
        }
        position_data = json.loads(requests.request(
            "get", position_url, params=position_payload).text)
        lat, lon = position_data['items'][0]['position'].values()

        return f"{lat},{lon}"

    def calculateroute(departure, destination, apikey):
        url = "https://router.hereapi.com/v8/routes"
        payload = {
            'transportMode': 'car',
            'origin': departure,
            'destination': destination,
            'apiKey': apikey,
            'return': 'summary'
        }
        response = requests.request("get", url, params=payload)
        return response.json()
