from backend import *
import time

event = Event()
mail = Mail()
db = DB(dbname="demo.db")
URL = "https://programmer100.pythonanywhere.com/tours/"

while True:
    source = event.scrape(URL)
    information = event.extract(source)

    database = db.reading()
    rows = [i[0] for i in database]
    print(rows)
    if information != 'No upcoming tours':
        temptuple = ()
        newitem = information.split(',')
        transformed_info = "".join(newitem).strip()
        if transformed_info not in rows:
            mail.sendingmail(information)

            temptuple += (transformed_info,)
            db.appending(temptuple)
    time.sleep(2)
