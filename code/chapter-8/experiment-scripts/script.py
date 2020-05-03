import httplib, urllib, base64
import sys
import os
from os import listdir
from os.path import isfile, join
import json
import base64
from watson_developer_cloud import VisualRecognitionV3
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from urlparse import urlparse
import boto3


def google(recognition_type, filename):
    print(filename)
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    endpoint = "/v1/images:annotate?key=ADD_YOUR_KEY_HERE"
    
    if recognition_type == "ocr":
        detection_type = "TEXT_DETECTION"
    else:
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
        conn = httplib.HTTPSConnection('vision.googleapis.com')
        conn.request("POST", endpoint, json.dumps(request_body))
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        result = []
        if recognition_type == "ocr":
            annotations = json_data['responses'][0]['textAnnotations']
            for annotation in annotations:
                result.append(annotation['description'])
            return result
        else:
            annotations = json_data['responses'][0]['labelAnnotations']
            for annotation in annotations:
                result.append((annotation['description'], annotation['score']))
            return result
        conn.close()
    except Exception as e:
        print(e)


def amazon(recognition_type, filename):
    with open(filename, "rb") as image_file:
        image_bytes = image_file.read()
    client=boto3.client('rekognition')
    response=client.detect_labels(Image={'Bytes': image_bytes })
    print(response)
    textDetections=response['Labels']
    result = []
    for each in textDetections:
        result.append(each['Name'])
    print(result)
    return result

def watson(recognition_type, filename):
    visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='ADD_YOUR_KEY_HERE')

    if recognition_type == "ocr":
        print("OCR not supported on Watson")
    else:
        with open(filename, 'rb') as images_file:
            data = visual_recognition.classify(
                images_file,
                parameters=json.dumps({
                    'classifier_ids': ['default'],
                    'threshold': 0.6
                }))
            result = []
            classes = data['images'][0]['classifiers'][0]['classes']
            for recognition_class in classes:
                result.append((recognition_class['class'], recognition_class['score']))
            return result


def clarifai(recognition_type, filename):
    app = ClarifaiApp(api_key='ADD_YOUR_KEY_HERE')

    if recognition_type == "ocr":
        print("OCR not supported on Watson")
    else:
        model = app.models.get('general-v1.3')
        image = ClImage(file_obj=open(filename, 'rb'))
        json_data = model.predict([image])
        result = []
        concepts = json_data['outputs'][0]['data']['concepts']
        for concept in concepts:
            result.append((concept['name'], concept['value']))
        return result




def microsoftphase2(recognitionid):
    headers = {
        'Ocp-Apim-Subscription-Key': 'ADD_YOUR_KEY_HERE',
    }

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/vision/v2.0/textOperations/" + recognitionid, "", headers)
        result = []
        response = conn.getresponse()
    print(response.read())
    except Exception as e:
    print(e)
 
def microsoft(recognition_type, filename):
        
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'ADD_YOUR_KEY_HERE',
    }

    if recognition_type == "ocr":
        endpoint = "/vision/v2.0/recognizeText?mode=Printed"
        params = urllib.urlencode({
            # Request parameters
            # 'mode': 'Printed'
        })
    else:
        endpoint = "/vision/v1.0/analyze?%s"
        params = urllib.urlencode({
            'language': 'en',
        })

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", endpoint, "{\"url\":\"http://76.103.208.220/images/" + filename + "\"}", headers)
        result = []
        response = conn.getresponse()
        url = response.getheader("Operation-Location")
    recognitionid = urlparse(url).path.split('/')[-1]
    print (recognitionid)
        if recognition_type == "ocr":
           if "regions" in json_data.keys():
                regions = json_data['regions']
                for region in regions:
                    lines = region['lines']
                    for line in lines:
                        words = line['words']
                        for word in words:
                            print (word['text']),
                            result.append(word['text'])
        else:
            categories = json_data['categories']
            for category in categories:
                result.append((category['name'], category['score']))
        conn.close()
    except Exception as e:
       print(e) 
       print("Error")
    return result


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse.
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_images(service_name, recognition_type, image, recognitionid):
    if os.path.isfile(image):
        #location is a single image
        results = {}
        if service_name == "microsoft":
            results[image] = microsoft(recognition_type, image)
        elif service_name == "microsoftphase2":
            results[image] = microsoftphase2(recognitionid)
        elif service_name == "google":
            results[image] = google(recognition_type, image)
        elif service_name == "amazon":
            results[image] = amazon(recognition_type, image)
        elif service_name == "watson":
            results[image] = watson(recognition_type, image)
        elif service_name == "clarifai":
            results[image] = clarifai(recognition_type, image)
        else:
            print("Invalid service name specified.")
        return results
    else:
        #location is a directory
        images = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f)) and (f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"))]
        results = {}
        for image in images:
            if service_name == "microsoft":
                results[image] = microsoft(recognition_type, image)
            elif service_name == "microsoftphase2":
                results[image] = microsoftphase2(recognitionid)
            elif service_name == "google":
                results[image] = google(recognition_type, image)
            elif service_name == "amazon":
                results[image] = amazon(recognition_type, image)
            elif service_name == "watson":
                results[image] = watson(recognition_type, image)
            elif service_name == "clarifai":
                results[image] = clarifai(recognition_type, image)
            else:
                print("Invalid service name specified.")
        return results


if __name__ == '__main__':
    from sys import argv
    input_args = getopts(argv)
    results = []
    if '-d' in input_args and '-t' in input_args:
        directory = input_args['-d']
        recognition_type = input_args['-t']
        service_name = input_args['-s']
    recognitionid = input_args['-r']
        results = process_images(service_name, recognition_type, directory, recognitionid)
        print(results)
        #return results
    else:
        print("Usage: python script.py -d [directory of images] -s [service name microsoft|google|amazon|watson|clarifai] -t [type of recognition ocr|object]")