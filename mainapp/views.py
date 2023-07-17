from django.shortcuts import render

# Create your views here.

def stockTracker(request):
    return render(request, 'mainapp/home.html')

def liveStocks(request):
    return render(request, 'mainapp/stocks.html')