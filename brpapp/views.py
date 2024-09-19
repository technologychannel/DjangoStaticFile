from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"brpapp/index.html")


def service(request):
    return render(request,"brpapp/service.html")

