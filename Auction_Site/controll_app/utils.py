import datetime
import json
import os

def comparison(date):

    date = date.split('-')

    current_time = datetime.datetime.now()

    year_now = current_time.year
    month_now = current_time.month
    day_now = current_time.day
    hour_now = current_time.hour

    if year_now > int(date[0]):
        return(True)
    elif year_now < int(date[0]):
        return(False)

    if month_now > int(date[1]):
        return(True)
    elif month_now < int(date[1]):
        return(False)
    
    if day_now > int(date[2]):
        return(True)
    elif day_now < int(date[2]):
        return(False)

    if hour_now > int(date[3]):
        return(True)
    elif hour_now < int(date[3]):
        return(False)

    return(False)


def time(date):
    date = date.split('-')

    return f'{date[2]}.{date[1]}.{date[0]}({date[3]}:00)'


def get_subdirectories(directory):
    lots = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    for i in range(len(lots)):

        with open(f'static/controll_auction/auction/{lots[i]}/description.json', encoding = "utf-8") as f:
                file_content = f.read()
                templates = json.loads(file_content)
            
        lots[i] = {
            "name": templates['name'],
            "price": templates['price'],
            "Description": templates['Description'],
            "path":f'controll_auction/auction/{lots[i]}/image.png',
        }


    return lots