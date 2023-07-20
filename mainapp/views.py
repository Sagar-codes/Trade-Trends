from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse


# Create your views here.

def stockTracker(request):
    stockPicker = tickers_nifty50()
    # print(stockPicker)
    return render(request, 'mainapp/home.html', {'stockPicker': stockPicker})


def liveStocks(request):
    stockpicker = request.GET.getList('stockpicker')
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker:
        details = get_quote_table(i)
        data.update(details)
        if i in available_stocks:
            pass
        else:
            return HttpResponse("No Stocks Found")
        print(data)
    return render(request, 'mainapp/stocks.html')
