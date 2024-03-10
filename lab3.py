import sys
from Adafruit_IO import MQTTClient
import random
import time
from simpleAI import *
from read_sensor import *

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "tien2032002"
AIO_KEY = "aio_gLcs26H1I9ATN92a6BjBBqdFHYnT"
MODEL_PATH = "IOT/keras_model.h5"
CLASS_NAME_PATH = "IOT/labels.txt"

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
    if (feed_id == "button1"):
        if(payload == "0"):
            writeData("Tat den\n")
        else:
            writeData("Bat den\n")
    elif feed_id == "button2":
        if (payload == "0"):
            writeData("Tat may bom\n")
        else:
            writeData("Bat may bom\n")

def writeData (data):
    ser.write(str(data).encode())

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

ser = serial.Serial( port=getPort(), baudrate=115200)

while True:
    # client.publish("button1", random.randint(0, 1))
    # # CAMERA can be 0 or 1 based on default camera of your computer
    # camera = cv2.VideoCapture(0)
    # # Grab the webcamera's image.
    # ret, image = camera.read()

    # # Resize the raw image into (224-height,224-width) pixels
    # image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # # Show the image in a window
    # client.publish("AI", simpleAI(model, class_names, image))
    readSerial(client, ser)
    time.sleep(1)
    pass