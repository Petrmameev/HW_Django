import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        CONTENT = list(csv.DictReader(f))
        paginator = Paginator(CONTENT, 10)
        current_number = int(request.GET.get('page', 1))
    context = {
        'bus_stations': paginator.get_page(current_number),
        'page': paginator.get_page(current_number)
    }
    return render(request, 'stations/index.html', context)
