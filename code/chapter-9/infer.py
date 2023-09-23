import flask
import tensorflow as tf
from tf import keras
from keras.utils.generic_utils import CustomObjectScope
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = flask.Flask(__name__)

with CustomObjectScope({"relu6": keras.applications.mobilenet.relu6}):
    model = load_model("ADD_H5_MODEL_PATH")


def preprocess(image):
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


@app.route("/infer", methods=["POST"])
def infer():
    file = flask.request.files["image"].read()
    image = Image.open(io.BytesIO(file))
    image = preprocess(image)

    predictions = model.predict(image)
    max_index = np.argmax(predictions)

    # We know the labels from the model we trained previously
    if max_index == 0:
        return "Cat"
    else:
        return "Dog"


if __name__ == "__main__":
    app.run()
