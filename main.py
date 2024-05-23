import io
import os
from google.cloud import vision
from google.cloud.vision_v1 import types


def classify_image(image_path):
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        print(f'Description: {label.description}, Score: {label.score}')

    return labels


# Set up your environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './image-detection-424208-8bc0bc7c7183.json'

# Classify an image
image_path = './chien.jpg'
classify_image(image_path)