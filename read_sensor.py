import serial.tools.list_ports
import  sys
import time

# function get port name
# in this example, i will hard code COM7
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return "COM7"

mess = ""

def processData(client, raw_data):
    # my data will be sent through serial with format:
    # "!<feed_name>:<data>#"
    # delete start and end token
    raw_data = raw_data.replace("!", "")
    raw_data = raw_data.replace("#", "")
    print (raw_data)
    # split data to get feed name and data
    splitData = raw_data.split(":")
    client.publish(splitData[0], splitData[1])

def readSerial(client, ser):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            # take data sent in format and call function processData
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
