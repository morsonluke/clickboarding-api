import http.client, urllib.request, urllib.parse, urllib.error, base64
import ast
import json

client_id = ''

endpoints = {
    "clients": "/v1/Clients?",
    "users"  : "/v1/Clients/" + client_id + "/Users?",
    "candidates": "/v1/Clients/" + client_id + "/Candidates?",
    "locations": "/v1/Clients/" + client_id + "/Locations?",
    "processes": "/v1/Clients/" + client_id + "/Processes?",
    "candidateprocesses" : "/v1/Clients/" + client_id + "/CandidateProcesses?",
    "tasks": "/v1/Clients/" + client_id + "/Tasks?"
}


class Clickboarding(object):

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def call_api(self, uri, limit):

        headers = {
        # Request headers
        'x-api-key': '',
        }

        params = urllib.parse.urlencode({
        # Request parameters
        'limit': limit
        })

        try:
            conn = http.client.HTTPSConnection('api.clickboarding.com')
            conn.request("GET", "%s%s" %(uri, params), "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


        # decode to str
        my_str = data.decode('utf8')
        # decode str to dict 
        my_dict = json.loads(my_str)
        print(uri, len(my_dict['items']))

for key, value in endpoints.items():
   api = Clickboarding(key)
   api.call_api(value, "1000")