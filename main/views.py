from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


def index_view(request):
    return render(request, "index.html")

def date(request):
    data = {
        'date': datetime.now()
    }
    return render(request, 'datetime.html', context=data)

