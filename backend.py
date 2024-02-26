import requests
import selectorlib
import mailing
import sqlite3

connection = sqlite3.connect("demo.db")
cursor = connection.cursor()

def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    """Extracting required information"""
    extraction = selectorlib.Extractor.from_yaml_file("extract.yaml")
    information = extraction.extract(source)['events']
    return information

def sendingmail(info):
    content = f"""\
Subject: Event Scheduled please check the Ticket Portal.
    
Event details - {info}
    """
    mailing.mailing(content)

def reading():
    # with open("database.txt",'r') as file:
    #     return file.read()
    cursor.execute('select * from musicevent')
    eventslist = cursor.fetchall()
    return eventslist
def appending(newitem):
    # with open("database.txt",'a') as file:
    #     file.writelines(information+'\n')
    cursor.execute("insert into musicevent values(?)",newitem)
    connection.commit()

