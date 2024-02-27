import requests
import selectorlib
import mailing
import sqlite3


class Event:
    def scrape(self, url):
        """Scrape the page source from the url"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        """Extracting required information"""
        extraction = selectorlib.Extractor.from_yaml_file("extract.yaml")
        information = extraction.extract(source)['events']
        return information


class Mail:
    def sendingmail(self, info):
        content = f"""\
    Subject: Event Scheduled please check the Ticket Portal.
        
    Event details - {info}
        """
        mailing.mailing(content)


class DB:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)

    def reading(self):
        # with open("database.txt",'r') as file:
        #     return file.read()
        cursor = self.connection.cursor()
        cursor.execute('select * from musicevent')
        eventslist = cursor.fetchall()
        return eventslist

    def appending(self, newitem):
        # with open("database.txt",'a') as file:
        #     file.writelines(information+'\n')
        cursor = self.connection.cursor()
        cursor.execute("insert into musicevent values(?)", newitem)
        self.connection.commit()
