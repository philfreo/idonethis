#!/usr/bin/env python
import json, sys, os, requests
try:
    raw_text = sys.argv[1]
except IndexError:
    raw_text = None

headers = {
    'authorization': 'Token %s' % os.getenv('IDONETHIS_TOKEN')
}

endpoint = 'https://idonethis.com/api/v0.1/dones/'

if raw_text:
    print requests.post(endpoint, headers=headers, data={
        'team': os.getenv('IDONETHIS_TEAM'),
        'raw_text': raw_text
    })

dones = requests.get(endpoint, headers=headers, params={
    'owner': os.getenv('IDONETHIS_USERNAME'),
    'done_date': 'today',
    'page_size': 100
}).json()['results']
for done in dones:
    print '-'+done['raw_text']
