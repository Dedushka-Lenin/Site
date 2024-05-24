from django.shortcuts import render

from login_app.models import Users_info

def index_page(request):

    # new_user = Users_info(name="Черный негр", mail='228', password='1234', subscription='Non', balance='0')
    # new_user.save()

    # user = Users_info.objects.get(id=4)
    # user.name = 'Черный черный негр'
    # user.save()

    # user = Users_info.objects.get(id=5)
    # user.delete()


    # users = Users_info.objects.all()
    # print(users)

    # for i in users:
    #     print(i.name, i.mail, i.password, i.subscription, i.balance, i.id)

    # users = Users_info.objects.filter(balance=0)
    # print(users)

    return render(request, "index.html")

def info_page(request, path):
    return render(request, "info.html", {'path':path})