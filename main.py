import backend
import time

URL = "https://programmer100.pythonanywhere.com/tours/"

while True:
    source = backend.scrape(URL)
    information = backend.extract(source)
    database = backend.reading()
    rows = [i[0] for i in database]
    print(rows)
    if information != 'No upcoming tours':
        temptuple = ()
        newitem = information.split(',')
        transformed_info = "".join(newitem).strip()
        if transformed_info not in rows:
             backend.sendingmail(information)
             temptuple += (transformed_info,)
             backend.appending(temptuple)
    time.sleep(2)


