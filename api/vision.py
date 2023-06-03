from google.cloud import vision
import io


def markImage(content):
    client = vision.ImageAnnotatorClient.from_service_account_json('keyfile.json')
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels[0].description