import socket
import sys
import requests
import requests_oauthlib
import json
from kafka import SimpleProducer, KafkaClient
import time

###################################################
# My own access tokens
####################################################
ACCESS_TOKEN = '28778811-sw3jVlgjtS14kvquuo765rjaIYvCE0iMpTsDXdiRs'
ACCESS_SECRET = 'HBGjT0uixYSC6PXvyewvBuFmHv4FYtU6UmsDG98khY'
CONSUMER_KEY = '2VsrZwlSbtToGYbpHe42hmB36'
CONSUMER_SECRET = 'vuXhfCmMVMwecUzV3hwK8vvkGWZnAM5wtEDvzMMenq6rH8yFqe'

my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)

####################################################
# Kafka Producer
####################################################
twitter_topic="twitter_topic"
client = KafkaClient("10.128.0.2:9092")
producer = SimpleProducer(client)

def get_tweets():
    print("#########################get_tweets called################################")
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    #query_data = [('language', 'en'), ('locations', '-130,-20,100,50'),('track','#')]
    #query_data = [('language', 'en'), ('locations', '-3.7834,40.3735,-3.6233,40.4702'),('track','#')]
    query_data = [('language', 'en'), ('locations', '-3.7834,40.3735,-3.6233,40.4702'),('track','Madrid')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    #print("Query url is", query_url)
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response

def send_tweets_to_kafka(http_resp):
    print("########################send_tweets_to_kafka called#################################")
    for line in http_resp.iter_lines():
        print("reading tweets")
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print ("------------------------------------------")
            tweet_text = tweet_text + '\n'
            producer.send_messages(twitter_topic, tweet_text.encode())
            #time.sleep(0.2)
        except:
            print("Error received")
            e = sys.exc_info()[0]
            print("Error: %s" % e)
    print("Done reading tweets")


def send_tweets_to_spark(http_resp, tcp_connection):
    print("########################send_tweets_to_spark called#################################")
    for line in http_resp.iter_lines():
        print("reading tweets")
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print ("------------------------------------------")
            #tcp_connection.send(tweet_text + '\n')
        except Exception as e:
            print("Error received")
            e1 = sys.exc_info()[0]
            print("Error e: %s" % str(e))
            print("Error e1: %s" % str(e1))
    print("Done reading tweets")




#TCP_IP = "localhost"
#TCP_IP = "0.0.0.0"
#TCP_PORT = 10001
#conn = None
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)
#print("Waiting for TCP connection...")
#conn, addr = s.accept()
#print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_kafka(resp)

