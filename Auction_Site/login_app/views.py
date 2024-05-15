from django.shortcuts import render

def index_page(request):
    return render(request, "index.html")

def info_page(request):
    return render(request, "info.html")