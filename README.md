**First exercice is composed of one file**

* Ex1.ipynb


**Second exercice is composed of two files**

It is about Spark Streaming API

* exserver.py
* exclient.ipynb

To run this exercice :

1. First, run :  `nc -lk 12345` this command is used to open a network connection using the tool `nc` (which stands for "netcat") in listening mode on port 12345 

2. Then, run : `python exserver.py` to stream tweets and exposed them on port 12345

3. Right after, run the third cell in the notebook exclient.ipynb to get the tweets from this TCP connection and store the hashtags in a list with two functions created beforehand.
When done, interrupt the third cell of the notebook and run the fourth cell in order to stop the session.

4. Finally, finish to execute the rest of the notebook, it creates another Spark session in order to count and order the most popular hashtags.