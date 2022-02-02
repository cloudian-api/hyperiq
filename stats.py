#!/usr/bin/env python
import requests

base_url = 'http://<HyperIQ IP>:3000/prometheus/api/v1/'
hiq_auth = ('cloudian_admin', '<HyperIQ password>')

queries = {
        '# of S3 operations per sec averaged over last 30 min (group G1)': "sum(rate(hs_s3operations{groupid='G1'}[30m]))",
        '# of PUTs over last 24 hrs (group G1)': "sum(increase(hs_s3operations{groupid='G1', s3operation='putObject'}[24h]))",
        '# of GETs and PUTs per sec happening right now (group G1)': "sum(irate(hs_s3operations{groupid='G1', s3operation=~'getObject|putObject'}[1m]))",
        '# Average PUT request duration over last 1 day, all buckets': "avg by (bucketname, cluster)((rate(hs_put_request_duration_microseconds_sum{}[1d]))/(rate(hs_put_request_duration_microseconds_count{}[1d])))",
        '# Average GET request duration over last 1 day, all buckets': "avg by (bucketname, cluster)((rate(hs_get_request_duration_microseconds_sum{}[1d]))/(rate(hs_get_request_duration_microseconds_count{}[1d])))",
        '# Number of GETs over last 1 day for bucket blah': "sum by (bucketname, cluster) (increase(hs_get_request_duration_microseconds_count{bucketname='blah'}[1d]))",
        '# Number of PUTs over last 1 day for bucket blah': "sum by (bucketname, cluster) (increase(hs_put_request_duration_microseconds_count{bucketname='blah'}[1d]))",
        }

for desc, query in queries.items():
    print(desc + ":")
    response = requests.get(base_url + 'query', params={'query': query}, auth=hiq_auth)
    print(response.json()['data']['result'], '\n')
