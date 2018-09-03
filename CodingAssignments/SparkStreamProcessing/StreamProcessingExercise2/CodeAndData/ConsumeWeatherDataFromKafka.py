from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
import sys
import requests
import time
import datetime
import sys
from pyspark.streaming.kafka import KafkaUtils
import random
import queue
import smtplib
import numpy as np
import configparser

##
# Declaring some config parameters here
##
CONF_FILE_NAME="groupe.conf"
config = configparser.ConfigParser()
config.read(CONF_FILE_NAME)
print(config['KAFKA']['kafka_topic'])

##
# Declaring some config and globals here (TODO: move config values to conf file and gloabls to a class)
##
#KAFKA_BROKER="10.128.0.2:9092"
#KAFKA_TOPIC="weather_data_topic"

##
# Declare globals here
##
climaticCondDict = {}
WT_RWS = 0.5
WT_WA = 0.3
WT_WD = 0.2

##
# Class for storing various weather parameters
##
class ClimaticCondition:
    def __init__(self, currTime, latitude, longitude, pressure_0m, temperature_10m, winddirection_10m, winddirection_40m, windspeed_10m, windspeed_40m):
        self.ts = currTime
        self.latitude = latitude
        self.longitude = longitude
        self.pressure_0m = pressure_0m
        self.temperature_10m = temperature_10m
        self.winddirection_10m = winddirection_10m
        self.winddirection_40m = winddirection_40m
        self.windspeed_10m = windspeed_10m
        self.windspeed_40m = windspeed_40m 

##
# A helper function to send email notification - This can be further extended to SMS etc.
# In real life the notification has to be sent to the subscriber over REST Web interface
##
def send_email_notification(email_reipient, email_sub, email_mesg):
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (config['SMTP.CONF.DETAILS']['smtp_login'], ", ".join(email_reipient), email_sub, email_mesg)
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL(config['SMTP.CONF.DETAILS']['smtp_host'], config['SMTP.CONF.DETAILS']['smtp_ssl_port'])
    server_ssl.ehlo() # optional, called by login()
    server_ssl.login(config['SMTP.CONF.DETAILS']['smtp_login'], config['SMTP.CONF.DETAILS']['smtp_password'])
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
    
    server_ssl.sendmail(config['SMTP.CONF.DETAILS']['smtp_login'], email_reipient, message)
    #server_ssl.sendmail(FROM, TO, message)
    #server_ssl.quit()
    server_ssl.close()
    print("successfully sent the mail")
    

##
# This function returns the windspeed at current location
# In real world this function will retrive data from an IoT device installed on the boat
##
def get_wind_speed_at_curr_loc():
    rand_wind_speed = random.uniform(5,40)
    return rand_wind_speed

##
# The following function tells us the current wind direction
# In real world this function will retrive data from an IoT device installed on the boat
##
def get_curr_wind_dir():
    rand_wind_dir = random.uniform(0, 360)
    return rand_wind_dir

##
# The following function tells us the coordinates of the boat
# In real world this function will retrive data from an IoT device installed on the boat
##
def get_curr_coord():
    rand_latitude = random.uniform(40.2000, 40.8000)
    rand_longitude = random.uniform(-105.9000, -105.2000)
    return rand_latitude,rand_longitude
    
    
##
# Compute relative wind speed 
##
def get_relative_wind_speed(cc, curr_ws):
    return cc.windspeed_10m - curr_ws
    
##
# Compute avg acceleration at a given cooord
##
def get_avg_wind_accelerations_at_coord(ccobj):
    # TODO: iterate through the vec of different wind speeds during diff times and calculate the wind acc
    return 0 # for now
    prevCc = None
    ccList = climaticCondDict.get(coord, None)
    if ccList != None:
        avgAcc = 0
        prevCc = None
        cnt = 0
        for x in ccList:
            if prevCc == None:
                prevCc = x
                continue
            else:
                cnt += 1
                currCc = x
                acc = (currCc.windspeed_10m - prevCc.windspeed_10m) / (currCc.ts - prevCc.ts)
                avgAcc = (avgAcc + acc)/cnt
                prevCc = currCc
        return avgCc
    else:
        return 0

##
# calculate the delta of prospective direction from current direction
##
def get_delta_dir(ccobj):
    currLat,currLong = get_curr_coord()
    dlat = currLat - ccobj.latitude
    dlon = currLong - ccobj.longitude

    rads = np.arctan2(dlon, dlat) #angle in radians
    ang = np.degrees(rads) # angle in degrees
    
    return ang
   

###
## def get_highest_ws
###
#def get_highest_ws_coord():
#    curr_ws = get_wind_speed_at_curr_loc()
#    rec_ws = curr_ws
#    rec_lat, rec_long = None
#    for coord, ccobj in climaticCondDict.items():
#        if ccobj.windspeed_10m > curr_ws:
#            return 

    
##
# This function makes a recommendation about the direction in which the boat should steer after
# taking into consideration various factors such as wind-speed, wind-direction and wind_acceleartion
# The direction with the best score is suggested
##
def determine_rec_direction():
    if(len(climaticCondDict) <= 1):
        return None
        #return None,None #stay the course
    
    prev_score = 0
    rec_coord = None
    rec_lat = None
    rec_long = None
    for coord, ccobj in climaticCondDict.items():
        rws = ccobj.windspeed_10m - get_wind_speed_at_curr_loc()
        curr_score = ((WT_RWS * rws) + (WT_WA * get_avg_wind_accelerations_at_coord(ccobj)) + (WT_WD * get_delta_dir(ccobj)))
        if curr_score > prev_score:
            prev_score = curr_score
            rec_coord = coord
            rec_lat = ccobj.latitude
            rec_long = ccobj.longitude

    #return rec_lat,rec_long
    rec_coord = str(rec_lat) + str(",") + str(rec_long)
    return rec_coord


##
# The following function parses the received data at different subscribed coordinates
# and determines the best direction in which the boat must move to
##
def process_weather_data(rdd):
    tuple_of_words = rdd.collect()
    print(tuple_of_words)
    if len(tuple_of_words) >=9:
        ts = 0
        lati = float(tuple_of_words[0])
        longi = float(tuple_of_words[1])
        pressure_0 = float(tuple_of_words[3])
        temp_10 = float(tuple_of_words[4])
        wd10 = float(tuple_of_words[5])
        wd40 = float(tuple_of_words[6])
        ws10 = float(tuple_of_words[7])
        ws40 = float(tuple_of_words[8])
    
        currentCcParams = ClimaticCondition(ts, lati, longi, pressure_0, temp_10, wd10, wd40, ws10, ws40)
        latlongkey = tuple_of_words[0] + tuple_of_words[1]
        print("latlongkey:", latlongkey)
        prevCcParams = climaticCondDict.get(latlongkey, None)
        climaticCondDict[latlongkey] = currentCcParams
        print("Length of dict", len(climaticCondDict))
        #rec_lat,rec_long = determine_rec_direction()
        rec_dir = determine_rec_direction()
        #if ((rec_lat == None) or (rec_long == None)):
        if rec_dir == None:
            print("Keep moving in the same direction as before")
            email_sub = "Keep moving in the same direction as before"
            #email_mesg = email_sub
            #send_email("kamal.nandan@gmail.com", "<password>", "gianluca.sabbatucci@student.ie.edu", "Keep moving in the same direction as before", "Keep moving in the same direction as before")
            #send_email_notification(config['SMTP.CONF.DETAILS']['smtp_recipient'], email_sub, email_mesg)
        else:
            print(">>>>>>>>>>>>>>>>>>>Go to coordinates>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(rec_dir)
            if config['SMTP.CONF.DETAILS']['send_email_notification'] ==  "YES":
                email_sub = "Go to coordinates: " + rec_dir
                email_mesg = email_sub
                send_email_notification(config['SMTP.CONF.DETAILS']['smtp_recipient'], email_sub, email_mesg)
    else:
        print("Empty tuple")
        
##
# Execution starts here
##
# create spark configuration
conf = SparkConf()
conf.setAppName("WeatherDataStreamApp")

# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# create the Streaming Context from the above spark context with interval size 2 seconds
ssc = StreamingContext(sc, 2)

# setting a checkpoint to allow RDD recovery
ssc.checkpoint("CheckpointWeatherDataStreamApp")

# Connect to Kafka topic # KAFKA_TOPIC and KAFKA_BROKER are defined at the top of the file
# dataStream = KafkaUtils.createDirectStream(ssc, [KAFKA_TOPIC],{"metadata.broker.list": KAFKA_BROKER})
dataStream = KafkaUtils.createDirectStream(ssc, [config['KAFKA']['kafka_topic']],{"metadata.broker.list": config['KAFKA']['kafkabroker_host'] + str(":") + str(config['KAFKA']['kafkabroker_port'])})
lines = dataStream.map(lambda x: x[1])

# Split the received data into words
record = lines.flatMap(lambda line: line.split(" "))

# process the received dstream data
record.foreachRDD(process_weather_data)

# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination()

