import numpy as np
from PIL import Image
import json
import argparse

def resize_image(img):
    max_dimension = 256
    width, height = img.size

    if width < max_dimension and height < max_dimension:
        return img

    resize_proportion = 1
    if width > height:
        resize_proportion = width / max_dimension
    else: 
        resize_proportion = height / max_dimension
    
    width = int(round(width / resize_proportion))
    height = int(round(height / resize_proportion))

    resized_image = img.resize((width, height), Image.ANTIALIAS)

    return resized_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a single image into a JSON request.')
    parser.add_argument('--input', help='Name of input image file', dest="input_filename", required=True)
    parser.add_argument('--output', help='Name of output JSON file', dest="output_filename", required=True)

    args = parser.parse_args()

    img = Image.open(args.input_filename)
    img.load()
    img = resize_image(img)
    data = np.asarray(img)

    json_obj = json.dumps({ "image": data.tolist() })

    f = open(args.output_filename, "w")
    f.write(json_obj)
    f.close()