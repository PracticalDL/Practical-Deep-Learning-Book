import http.client, urllib
from sys import argv
import json
import os
from os import listdir
from os.path import isfile, join
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

microsoft_api_key = 'ADD_YOUR_KEY_HERE'
path_to_images = "http://ADD_YOUR_IP_ADDRESS_HERE/images/"

def microsoft_phase_1(filename):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': microsoft_api_key,
    }

    endpoint = "/vision/v2.0/recognizeText?mode=Printed"
    params = urllib.urlencode({
        # Request parameters
        # 'mode': 'Printed'
    })
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        request_body = "{\"url\":\"" + path_to_images + filename + "\"}"
        conn.request("POST", endpoint, request_body, headers)
        response = conn.getresponse()
        url = response.getheader("Operation-Location")
        recognition_id = urlparse(url).path.split('/')[-1]
        return recognition_id
        conn.close()
    except Exception as e:
       print(e) 
       print("Error")


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse.
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_image(image):
    results = {}
    results[image] = microsoft_phase_1(image)
    return results

def process_images(directory):
    results = {}
    images = [f for f in listdir(directory) if isfile(join(directory, f))]
    for image in images:
	    results[image] = microsoft_phase_1(image)
    return results

if __name__ == '__main__':
    input_args = getopts(argv)
    results = []
    if '-i' in input_args:
        image = input_args['-i']
        results = process_image(image)
        for key, value in results.iteritems():
            print(key + "," + value)
    elif '-d' in input_args:
        directory = input_args['-d']
        results = process_images(directory)
        for key, value in results.iteritems():
            print(key + "," + value)
    else:
        print("Usage: python microsoft-phase-1.py [-i path to an image | -d path to directory of images]")