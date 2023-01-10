#!/usr/bin/env python3
import requests
import getpass

HIQ_IP = str(input("HIQ Cluster IP:"))
HIQ_User = str(input("HIQ CLuster User ID:"))
HIQ_Pass = getpass.getpass(prompt="HIQ CLuster Password:")

base_url = "http://{}:3000/prometheus/api/v1/".format(HIQ_IP)
HiqAuth = (HIQ_User, HIQ_Pass)

BucketNames = [item for item in input("Enter the Bucket Names : ").split()]

print("################# Bucket Owner Info ######################")
for bucket in BucketNames:
    try:
        query = 'admin_system_bucketlist{bucketname=\"' + bucket +'\"}'
        response = requests.get(base_url + 'query', params={'query': query}, auth=HiqAuth)
        for result in response.json()['data']['result']:
            print(result['metric']['bucketname'], result['metric']['group'], result['metric']['user'])
    except Exception as e:
        print(e, response.text, response.url)
