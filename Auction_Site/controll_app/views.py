from django.shortcuts import render
from django.views import View

from controll_app.utils import get_lots, context_generator

from .models import Lots


# Create your views here.

class Auction(View):

    def get(self, request):

        context = {
            'lots': get_lots(),
            'type': 'auction'
        }

        return render(request, 'auction/auction.html', context=context)
    

class Product(View):

    def get(self, request, lot):

        context = context_generator(lot)

        return render(request, 'auction/auction.html', context=context)
    


def place_a_bet(request):
    auction_step = int(request.POST.get('auction_step' ,1))
    mail = request.POST.get('mail' ,1)

    name = request.POST.get('name' ,1)
    
    bid = request.POST.get(name ,1)

    if not bid == '':
        bid = int(bid)
        lot = Lots.objects.get(name=name)

        if lot.price < bid and (bid - lot.price) >= auction_step:
            lot.price = bid
            lot.recipient = mail

            lot.save()

            context = context_generator(name)

            return render(request, 'auction/auction.html', context=context)
        
        context = context_generator(name, f'Ваша ставка должна быть больше предыдущей, минимум на {auction_step}')

        return render(request, 'auction/auction.html', context=context)
    
    context = context_generator(name, 'Поле ввода не должно быть пустым')

    return render(request, 'auction/auction.html', context=context)