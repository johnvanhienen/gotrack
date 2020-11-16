#!/usr/bin/env python3
import datetime
import os, sys
import click
import logging

from common import Common
from location import Location

outputfile = ""

@click.command()
@click.option('-a','--apikey', help='Apikey from developer.here.com')
@click.option('-h','--homelocation', required=True, help='Origin/home location')
@click.option('-o','--outputfile', default="./gotrack.csv", help='Location and name of csv output file')
@click.option('-w','--worklocation', required=True, help='Destination/work location')
def main(apikey, homelocation, outputfile, worklocation):
    if os.environ['GOTRACK_APIKEY']:
        apikey = os.environ['GOTRACK_APIKEY']

    if os.environ['GOTRACK_OUTPUTFILE']:
        outputfile = os.environ['GOTRACK_OUTPUTFILE']

    if not apikey:
        logging.fatal("Missing apikey from developer.here.com")
        sys.exit(1)

    print(homelocation, worklocation, outputfile, apikey)
    # Set departure and destination based on time
    if Common.is_time_between(datetime.time(5, 0), datetime.time(12, 0)):
        departure, destination = homelocation, worklocation
    else:
        departure, destination = worklocation, homelocation

    # Retrieve longitude and latitude
    departure_pos = Location.lookupposition(departure, apikey)
    destination_pos = Location.lookupposition(destination, apikey)

    route = Location.calculateroute(departure_pos, destination_pos, apikey)

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

    Common.writetofile(data, headers, outputfile)


if __name__ == '__main__':
    main()
