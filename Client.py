
import socket
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

HOST_RPI = #'10.104.99.110'
HOST_SERVER = #'10.104.127.47'
PORT_OUT = 65431
PORT_IN = 65432



def recordImage():
    #pull image file from SSD


    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/wakeupcat.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #modify this part below to read labels to audio using text to speech and project to audio
    print('Labels:')
    for label in labels:
        print(label.description)


def recordDistance():
    #

def closeDistanceWarning():
    #

def inputVoiceCommand():
    #put data in

def outputVoiceCommand():
    #