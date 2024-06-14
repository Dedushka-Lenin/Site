from django.template.loader import render_to_string
from controll_app.utils import comparison
from django.core.mail import EmailMessage

from controll_app.models import Lots

def startup_routine():
    pass

    def transition():

        lots = Lots.objects.all()
        
        for i in range(len(lots)):
            
            if lot.end == False:
                lot = Lots.objects.get(name=lots[i].name)

                lot.end = comparison(lots[i].end_time)

                lot.save()

            if lot.end == True:

                print(i, lot.id)

                lot = {
                    'name': lot.name,
                    'price': lot.price,
                    'Description': lot.Description,
                    'ing': lot.ing,
                    'recipient': lot.recipient,
                }


    def send_email_for_verify(user):

        context = {
            "user": user,
        }


        messag = render_to_string(
            'examination/examination.html',
            context=context,
        )

        email = EmailMessage(
            "Verify email",
            messag,
            to=[user],
        )

        email.send()

    # send_email_for_verify('admin@admin.com')   
    
transition()