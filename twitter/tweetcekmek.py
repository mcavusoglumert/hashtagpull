import tweepy
import json
import time
import operator
import schedule
import smtplib
from datetime import datetime
from private import consumer_key,consumer_secret

def hashtag():
    tarih = str(datetime.now())
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.starttls()
    conn.login('mcavusoglumert@gmail.com', 'mwbdejngxxrhakam')
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    hashtag_response = api.trends_place(23424969)
    hashtag_result = hashtag_response[0].get("trends", [])[0: 10]
    print("Başlatılıyor...")
    time.sleep(2)
    result = ""
    
    for tweet in hashtag_result:
        if tweet["tweet_volume"] is None:
            tweet["tweet_volume"] = 0

    for tweet in sorted(hashtag_result, key=lambda tweet: tweet.get("tweet_volume"), reverse=True):
        a = tweet["name"]
        b = tweet["tweet_volume"]
        if b == 0:
            b = "-- < 10K"
        else:
            b = "-- < " + str(b)
        result += f"{a} {b}\n"
    conn.sendmail("mcavusoglumert@gmail.com","mcavusoglumert@gmail.com", "Subject:" + tarih + "\n\n" + result)
        
schedule.every().day.at("12:00").do(hashtag) and schedule.every().day.at("23:59").do(hashtag)

while True:
    schedule.run_pending()
    print("Çalışıyor")
    time.sleep(10)