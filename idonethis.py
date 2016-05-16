#!/usr/bin/env python
import json, sys, os, urllib, urllib2

headers = {
    'authorization': 'Token %s' % os.getenv('IDONETHIS_TOKEN')
}

def request(endpoint, data = None):
    r = urllib2.Request(endpoint, data and urllib.urlencode(data), headers)
    return json.loads(urllib2.urlopen(r).read())

if len(sys.argv) > 1:
    raw_text = ' '.join(sys.argv[1:])
else:
    raw_text = None

endpoint = 'https://idonethis.com/api/v0.1/dones/'

if raw_text:
    print request(endpoint, {
        'team': os.getenv('IDONETHIS_TEAM'),
        'raw_text': raw_text
    })

dones = request(endpoint + "?" + urllib.urlencode({
    'owner': os.getenv('IDONETHIS_USERNAME'),
    'done_date': 'today',
    'page_size': 100
}))['results']
for done in dones:
    print '-'+done['raw_text']
