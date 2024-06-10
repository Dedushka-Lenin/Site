import datetime
import json
import os

from .models import Lots

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


def get_lots():
    lots = Lots.objects.all()

    lots_inf = []

    for i in range(len(lots)):
        
            
        lots_inf.append({
            "name": lots[i].name,
            "price": lots[i].price,
            "Description": lots[i].Description,
            "path": lots[i].ing,
        })

    return lots_inf