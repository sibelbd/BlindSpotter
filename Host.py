import socket

HOST_RPI =  # '10.104.99.110'
HOST_SERVER=  # '10.104.127.47'
PORT_OUT= 65432
PORT_IN= 65431

""" Sample socket communication to receive data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_SERVER,PORT_IN))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        data = data.decode()
        data = int(data)
"""

def __init__():
    #main method starts new thread for automatic distance alerting
    #starts other thread waiting for vocal commands, initiated by keyword or button input

def distanceChecking():
    #do while on == true, check distance
    #f distance greater than some distance, then don't sent alert
    #if distance less than some distance send alert
    #alert uses text to speech of #warning, object ahead within ___ distance of you

def waitForCommand():
    #connect button to this method
    #method launches listing for audio method


def processDistance(distance):
    #calls and returns distance variable

def processInputVoiceCommand(strings[], distance):
    #speech strings is passed in
    #string template with distance, like "I see ___, ___, ___, and __." plus first four string args concatinated in a sentence
    #use google text to speech API to turn it into speech
    #play speech over speakers

def processOutputVoiceCommand(data):
    #audio data is passed in
    #data is processed through google speech to text API
    #a string is returned
    #if string == "What's over there?" "What is over there" "What's over here" "What is over here?" "What is this" "What is that" or "What is in front of me"
    #then call client.recordImage() && processDistance()
    #use the variables above to call processInputVoiceCommand()