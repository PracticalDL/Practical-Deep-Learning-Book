import http.client, urllib, base64
import sys
import os
from os import listdir
from os.path import isfile, join
import json
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import boto3

google_api_key = 'ADD_YOUR_KEY_HERE'

def google(filename):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    endpoint = "/v1/images:annotate?key=" + google_api_key
    
    detection_type = "LABEL_DETECTION"
    request_body = {
        "requests":[
        {
            "image":{
                "content":encoded_string
            },
            "features":[
            {
                "type":detection_type,
                "maxResults":10
            }
            ]
        }
        ]
    }

    try:
        conn = http.client.HTTPSConnection('vision.googleapis.com')
        conn.request("POST", endpoint, json.dumps(request_body))
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        result = []
        annotations = json_data['responses'][0]['labelAnnotations']
    for annotation in annotations:
        result.append((annotation['description'], annotation['score']))
        return result
        conn.close()
    except Exception as e:
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
    results[image] = google(image)
    return results

def process_images(directory):
    images = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f)) and (f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"))]
    results = {}
    for image in images:
        results[image] = google(image)
    return results


if __name__ == '__main__':
    input_args = getopts(sys.argv)
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
        print("Usage: python google.py [-i path to an image | -d path to directory of images] [-o output path]")
