#!/usr/bin/python3
#this is a comment .!/usr/bin/env python3


import feedparser
import pandas as pd
import time
import numpy as np
import sys
import logging
import csv


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#from subprocess import check_output
#import sys


with open('feed_links.csv', mode='r') as infile:
    reader = csv.reader(infile)
    urls = {rows[0]:rows[1] for rows in reader}

#urls = {}
#urls["Technology"] = 'https://www.google.com/alerts/feeds/04633522030720328702/17953401794911713837'
#urls["Xbox"] =  'https://www.google.com/alerts/feeds/04633522030720328702/9761777365347078087'
#urls["Video Games OR gaming"]  = 'https://www.google.com/alerts/feeds/04633522030720328702/9669040427288917831'
#urls["Playstation"] = 'https://www.google.com/alerts/feeds/04633522030720328702/15206837917531560928'
#urls["e sports"] = "https://www.google.com/alerts/feeds/04633522030720328702/8442039481667620914"
#urls["CNN - Technology"] = 'http://rss.cnn.com/rss/edition_technology.rss'
#urls["CNN - Science and Space"] = 'http://rss.cnn.com/rss/edition_space.rss'
#urls["CNN - Africa"] = 'http://rss.cnn.com/rss/edition_africa.rss'
#urls["CNN - World"] = 'http://rss.cnn.com/rss/edition_world.rss'
#urls["Reuters UK: Technology News"] = 'http://feeds.reuters.com/reuters/technologyNews'
#urls["Reuters UK: Top News"] = ''


#feed_name = sys.argv[1]
#url = sys.argv[2]

db = 'data/feeds.csv'

#checks every hour
sleep_time = 60 * 60 # 1/60 * 3600 * 1000

#
# function to get the current time
#
def current_time_millis():
    return int(round(time.time() * 1000))



def read_file(filepath):
    """Reads a book and returns string"""
    s = []
    csv.writer()
    with open (filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if(len(row) > 0):
                s.append(row)
    return s

def load_lookup():
    """
        Reads the data/feeds.csv file and loads all values in it into Pandas DataFrame lookup.
        If the file does not exist it returns an empty DataFrame.
    """
    lookup = None
    try:
        lookup = pd.read_csv(db, names = ["stamp", "title", "url", "summary","topic"], encoding='utf-8')
    except:
        logging.error("Failed to read file: ./data/feeds.csv")

    if lookup is None:
        lookup = pd.DataFrame(columns = ["stamp", "title", "url", "summary","topic"])

    return lookup

def post_is_in_db(title):
    """Checks if string value `title` exists in the 'titles' column of lookup"""
    try:
        return title in lookup.title.values
    except:
        logging.error("Exception lookup")

#logging.debug("URL:\t" + url)
#lookup = load_lookup()

while True:
    lookup = load_lookup()
    logging.debug("Lookup:\t" + str(len(lookup)))
    posts_to_save = []
    current_timestamp = current_time_millis()

    for url in urls:
        logging.debug("Topic:\t" + url)
        #
        # get the feed data from the url
        #
        feed = feedparser.parse(urls[url])

        for post in feed.entries:
                # if post is already in the database, skip it
                # TODO check the time
            row = [None] * 5
            row[0] = str(current_timestamp)
            row[1] = post.title
            row[2] = post.link
            row[3] = post.summary
            row[4] = url

            if not post_is_in_db(post.title):
                posts_to_save.append(row)

        logging.debug("New Posts to save:\t" + str(len(posts_to_save)))

    if(len(posts_to_save) > 0):
        df = pd.DataFrame(posts_to_save, columns=["stamp", "title", "url", "summary","topic"])
        lookup = lookup.append(df)
        lookup.to_csv(db, header=False, sep=',',encoding='utf-8')
    logging.debug("Sleeping")
    lookup = None
    posts_to_save = None
    time.sleep(sleep_time)