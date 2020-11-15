import datetime
import os
import csv


class Common:
    def is_time_between(begin_time, end_time):
        current_time = datetime.datetime.now().time()
        if begin_time < end_time:
            return current_time >= begin_time and current_time <= end_time

    def formattime(triptime):
        # Remove date
        triptime = triptime.split('T')[-1]
        # Remove timezone
        triptime = triptime.split('+')[0]
        return triptime

    def writetofile(data, headers, filelocation):
        file_exists = os.path.isfile(filelocation)

        with open(filelocation, 'a+', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            if not file_exists:
                writer.writerow(headers)

            writer.writerow(data)
