import requests
import json
import time

apiKey = 'your_api_key_here'
trackingUrl = 'https://parcelsapp.com/api/v3/shipments/tracking'
shipments = [{'trackingId': 'tracking_number_1', 'language': 'en', 'country': 'United States'},
             {'trackingId': 'tracking_number_2', 'language': 'en', 'country': 'United States'},
             ...]

# Initiate tracking request
response = requests.post(trackingUrl, json={'apiKey': apiKey, 'shipments': shipments})

if response.status_code == 200:
    # Get UUID from response
    uuid = response.json()['uuid']
    # Function to check tracking status with UUID
    def check_tracking_status():
        response = requests.get(trackingUrl, params={'apiKey': apiKey, 'uuid': uuid})
        if response.status_code == 200:
            if response.json()['done']:
                print('Tracking complete')
            else:
                print('Tracking in progress...')
                time.sleep(N) # sleep for N sec
                check_tracking_status()
        else:
            print(response.text)
    check_tracking_status()
else:
    print(response.text)