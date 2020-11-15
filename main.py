#!/usr/bin/env python3
import datetime

from common import Common
from location import Location

APIKEY = ""

homelocation = ""
worklocation = ""

outputfile = ""


def main():
    # Set departure and destination based on time
    if Common.is_time_between(datetime.time(5, 0), datetime.time(12, 0)):
        departure, destination = homelocation, worklocation
    else:
        departure, destination = worklocation, homelocation

    # Retrieve longitude and latitude
    departure_pos = Location.lookupposition(departure, APIKEY)
    destination_pos = Location.lookupposition(destination, APIKEY)

    route = Location.calculateroute(departure_pos, destination_pos, APIKEY)

    trip_departuretime = Common.formattime(
        route['routes'][0]['sections'][0]['departure']['time'])
    trip_arrivaltime = Common.formattime(
        route['routes'][0]['sections'][0]['arrival']['time'])
    trip_minutes = round(
        int(route['routes'][0]['sections'][0]['summary']['duration'])/60)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    # Prepare data and headers for outputfile
    headers = ['Date', 'Departure', 'Departure time',
               'Destination', 'Arrival time', 'Duration']
    data = [current_date,  departure, trip_departuretime,
            destination, trip_arrivaltime, trip_minutes]

    # Common.writetofile(data, headers, outputfile)


main()
