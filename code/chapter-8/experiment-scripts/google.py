import base64, httplib, json

def googlecloud_tagimage(filename):
    with open(filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())

    endpoint = '/v1/images:annotate?key=ADD_YOUR_KEY_HERE'
    
    request_body = {
        'requests':[
        {
            'image':{
                'content':encoded_string
            },
            'features':[
            {
                'type':'LABEL_DETECTION',
                'maxResults':10
            }
            ]
        }
        ]
    }

    conn = httplib.HTTPSConnection('vision.googleapis.com')
    conn.request('POST', endpoint, json.dumps(request_body))
    response = conn.getresponse()
    print(response.read())
    conn.close()

googlecloud_tagimage('DogAndBaby.jpg')
