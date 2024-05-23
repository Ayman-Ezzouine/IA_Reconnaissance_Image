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


def check_for_animal(labels):
    for label in labels:
        if "animal" in label.description.lower():
            return True
    return False


def check_for_humans(labels):
    keywords = [
        "person", "human", "man", "woman", "child", "boy", "girl", "adult", "baby", "toddler", "teenager",
        "face", "head", "hair", "eye", "mouth", "nose", "ear", "hand", "arm", "leg", "foot", "torso", "body", "smile",
        "activity", "walking", "running", "sitting", "standing", "dancing", "jumping", "playing", "working",
        "forehead", "cheek", "chin", "jaw", "lip", "eyebrow", "eyelash", "beard", "mustache"
    ]
    for label in labels:
        if any(keyword in label.description.lower() for keyword in keywords):
            return True
    return False


# Set up your environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './image-detection-424208-8bc0bc7c7183.json'

# Classify an image
image_path = './images/photo_2.jpg'
labels = classify_image(image_path)
animal = check_for_animal(labels)
human = check_for_humans(labels)

if animal:
    print("Animal detected in the image.")
else:
    print("No animals detected.")
if human:
    print("Human detected in page")
else:
    print("No humans detected")