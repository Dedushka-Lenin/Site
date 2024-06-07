from django.shortcuts import render
from django.views import View

from controll_app.utils import comparison, time, get_subdirectories

import json

# Create your views here.

class Auction(View):

    def get(self, request):

        with open('static/controll_auction/auction/auction.json', encoding = "utf-8") as f:
            file_content = f.read()
            templates = json.loads(file_content)


        if comparison(templates['end']): is_going_on = False
        elif not comparison(templates['start']): is_going_on = False
        else: is_going_on = True

        context = {
            'is_going_on': is_going_on,
            'end': time(templates['end']),
            'auction_step': templates['auction_step'],
            'lots': get_subdirectories('static/controll_auction/auction'),
        }

        

        return render(request, 'auction/auction.html', context=context)