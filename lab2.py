import sys
from Adafruit_IO import MQTTClient
import random
import time
from simpleAI import *

AIO_FEED_IDs = ["button1"]
AIO_USERNAME = "tien2032002"
AIO_KEY = "aio_ujXn77sn3RraI7wP8xWMOh4OCdu4"
MODEL_PATH = "IOT\keras_model.h5"
CLASS_NAME_PATH = "IOT\labels.txt"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    client.publish("button1", random.randint(0, 1))
    client.publish("AI", simpleAI(model, class_names))
    time.sleep(5)
    pass