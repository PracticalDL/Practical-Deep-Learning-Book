import http.client, urllib, base64
import sys
import os
from os import listdir
from os.path import isfile, join
import json
import base64
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import boto3

microsoft_api_key = 'ADD_YOUR_KEY_HERE'

def microsoft_phase_2(recognition_id):
    headers = {
        'Ocp-Apim-Subscription-Key': microsoft_api_key,
    }

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/vision/v2.0/textOperations/" + recognition_id, "", headers)
        result = []
        response = conn.getresponse()
        return response.read()
    except Exception as e:
    	print(e)

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse.
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_images(recognition_id_filename):
    data = []
    with open(recognition_id_filename) as file:
        data = file.readlines()
    results = {}
    for each in data:
        image_name = each.split(",")[0].strip()
        recognition_id = each.split(",")[-1].strip("\n").strip()
        results[image_name] = microsoft_phase_2(recognition_id)
    return results


if __name__ == '__main__':
    from sys import argv
    input_args = getopts(argv)
    results = []
    if '-i' in input_args and '-o' in input_args:
        recognition_ids_filename = input_args['-i']
        results = process_images(recognition_ids_filename)
        output_path = input_args['-o']
        with open(output_path, "w") as write_file:
            json.dump(results, write_file)
    else:
        print("Usage: python microsoft-phase-2.py [-i path to recognition IDs file] [-o output path]")