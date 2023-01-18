import socket
import time
import tweepy
import log

class tweetSender(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send(tweet.text.encode())
        print(tweet.text)
        time.sleep(0.001)
        c.close()

printer = tweetSender(log.token)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
host = socket.gethostname()
port = 12345 #define the port

s.bind((host, port)) #bind to port

s.listen(5)
printer.sample()