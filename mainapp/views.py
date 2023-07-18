from django.shortcuts import render
from yahoo_fin.stock_info import *

# Create your views here.

def stockTracker(request):
    stockPicker = tickers_nifty50()
    print(stockPicker)
    return render(request, 'mainapp/home.html', {'stockPicker':stockPicker})

def liveStocks(request):
    return render(request, 'mainapp/stocks.html')