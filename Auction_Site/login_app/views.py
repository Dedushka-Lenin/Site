from django.shortcuts import render

def index_page(request):
    return render(request, "index.html")

def info_page(request, path):
    return render(request, "info.html", {'path':path})