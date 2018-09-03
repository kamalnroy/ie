import os
import numpy as np
import pandas as pd
from kafka import SimpleProducer, KafkaClient
import time
import random
import configparser

# Config file name
CONF_FILE_NAME="groupe.conf"

# Parse the config file
config = configparser.ConfigParser()
config.read(CONF_FILE_NAME)

# Create a Kafka Producer client object
#client = KafkaClient("10.128.0.2:9092")
kakfka_host_port = config['KAFKA']['kafkabroker_host'] + str(":") + str(config['KAFKA']['kafkabroker_port'])
print(kakfka_host_port)
client = KafkaClient(kakfka_host_port)
producer = SimpleProducer(client)

# Files containing the weather records such as pressure/temp/wind-speed/wind-direction etc. for different cooordinates
filepath1 = 'longspeak1.csv'  
filepath2 = 'longspeak2.csv'  
filepath3 = 'longspeak3.csv'  
filepath4 = 'longspeak4.csv'
fp1 = open(filepath1)
fp2 = open(filepath2)
fp3 = open(filepath3)
fp4 = open(filepath4)

# Dummy coordinates for simulation purposes
latitude1 = "40.4549"
longitude1 = "-105.6160"
latitude2 = "40.5549"
longitude2 = "-105.7160"
latitude3 = "40.6549"
longitude3 = "-105.8160"
latitude4 = "40.7549"
longitude4 = "-105.9160"

# Read data from random files and start sending the data to Kafka topic; this is a simulation of IoT devices that will
# be sending the data in real life. 
while True:
    fp = None
    lat = None
    longitude = None
    
    rand = random.randint(1,4)
    print("Random no. is ", rand)
    if rand == 1:
        fp = fp1
        latitude = latitude1
        longitude = longitude1
    elif rand == 2:
        fp = fp2
        latitude = latitude2
        longitude = longitude2
    elif rand == 3:
        fp = fp3
        latitude = latitude3
        longitude = longitude3
    elif rand == 4:
        fp = fp4
        latitude = latitude4
        longitude = longitude4        
    
    line = fp.readline()
    line = latitude + " " + longitude + " " + line
    print(line)
    producer.send_messages(config["KAFKA"]["kafka_topic"], line.encode())
    time.sleep(2)
