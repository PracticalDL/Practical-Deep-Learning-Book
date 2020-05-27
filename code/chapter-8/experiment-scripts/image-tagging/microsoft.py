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

def microsoft(filename):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': microsoft_api_key,
    }
    
    endpoint = "/vision/v2.0/analyze?%s"
    params = urllib.urlencode({
        'language': 'en',
    })
    
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        request_body = "{\"url\":\"" + path_to_images + filename + "\"}"
        conn.request("POST", endpoint, request_body, headers)
        response = conn.getresponse()
        json_data = json.loads(response.read())
        categories = json_data['categories']
        
        results = []
        for category in categories:
            results.append((category['name'], category['score']))
        conn.close()
        return results
    except Exception as e:
        print("ERROR!!")
        print(e)

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse.
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_image(image):
    results = {}
    results[image] = microsoft(image)
    return results

def process_images(directory):
    results = {}
    images = [f for f in listdir(directory) if isfile(join(directory, f))]
    for image in images:
        results[image] = microsoft(image)
    return results

if __name__ == '__main__':
    input_args = getopts(argv)
    results = []
    if '-i' in input_args and '-o' in input_args:
        image = input_args['-i']
        results = process_image(image)
        output_path = input_args['-o']
        with open(output_path, "w") as write_file:
            json.dump(results, write_file)
    elif '-d' in input_args and '-o' in input_args:
        directory = input_args['-d']
        results = process_images(directory)
        output_path = input_args['-o']
        with open(output_path, "w") as write_file:
            json.dump(results, write_file)
    else:
        print("Usage: python microsoft.py [-i path to an image | -d path to directory of images] [-o output path]")
