import requests
import secrets
import json
import logging
import time


def main():
    payload = {'origins': 'Casnate', 'destinations': 'Rimini', 'mode': 'driving', 'departure_time': 'now', 'key': secrets.api_key}
    URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    logging.basicConfig(filename='drivetime.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    time_between_requests_in_seconds = 600

    while (True):
        r = requests.get(URL,params=payload)
        output = json.loads(r.text)
        duration_in_traffic = output['rows'][0]['elements'][0]['duration_in_traffic']['text']    
        traveltime = 'From {source} to {destination} will take {drivetime}'.format(source = payload['origins'], destination = payload['destinations'], drivetime = duration_in_traffic)

        print(traveltime)
        logging.info(traveltime)
        time.sleep(time_between_requests_in_seconds)


if __name__ == "__main__":
    main()