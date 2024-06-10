from django.shortcuts import render, redirect
from django.views import View

from controll_app.utils import comparison, time, get_lots

from .models import Lots

import json


# Create your views here.

class Auction(View):

    def get(self, request):

        with open('controll_auction/auction/auction.json', encoding = "utf-8") as f:
            file_content = f.read()
            templates = json.loads(file_content)


        if comparison(templates['end']): is_going_on = False
        elif not comparison(templates['start']): is_going_on = False
        else: is_going_on = True

        context = {
            'is_going_on': is_going_on,
            'end': time(templates['end']),
            'auction_step': templates['auction_step'],
            'lots': get_lots(),
        }

        return render(request, 'auction/auction.html', context=context)
    


def place_a_bet(request):
    auction_step = int(request.POST.get('auction_step' ,1))

    name = request.POST.get('name' ,1)
    bid = int(request.POST.get(name ,1))

    price = Lots.objects.get(name=name)


    if price.price < bid and (bid - price.price) > auction_step:

        price.price = bid

        price.save()

    # print(name, bid, price.price)


    return redirect('auction')