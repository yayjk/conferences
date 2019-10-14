from django.shortcuts import render
from .models import confDB
import requests
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.


class SearchView(ListView):
    model = confDB
    template_name = "god/search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = confDB.objects.filter(
            Q(confEndDate=query) | Q(confStartDate__icontains=query) | Q(
                confName__icontains=query) | Q(venue__icontains=query) | Q(status__icontains=query)
        )

        return object_list


def home(request):
    response = requests.get(
        'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

    conf_data = response.json()

    free_data = conf_data['free']
    free_conf = []

    for conf_no in range(len(free_data)):
        newDicts = {key: value for (key, value) in free_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue' or key == 'confUrl'}
        if not newDicts['imageURL'].startswith("\""):
            newDicts['imageURL'] = "\"" + newDicts['imageURL'] + "\""
        free_conf.append(newDicts)

    return render(request, 'god/index.html', {
        'free': free_conf
    })


def paid(request):
    response = requests.get(
        'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

    conf_data = response.json()

    paid_data = conf_data['paid']
    paid_conf = []

    for conf_no in range(len(paid_data)):
        newDicts = {key: value for (key, value) in paid_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue' or key == 'confUrl'}
        if not newDicts['imageURL'].startswith("\""):
            newDicts['imageURL'] = "\"" + newDicts['imageURL'] + "\""
        paid_conf.append(newDicts)

    return render(request, 'god/paid.html', {
        'paid': paid_conf
    })


'''
def save_to_db(request):
    response = requests.get(
        'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

    conf_data = response.json()
    paid_data = conf_data['paid']
    free_data = conf_data['free']
    paid_conf = []
    free_conf = []

    for conf_no in range(len(free_data)):
        newDicts = {key: value for (key, value) in free_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue' or key == 'confUrl'}
        if not newDicts['imageURL'].startswith("\""):
            newDicts['imageURL'] = "\"" + newDicts['imageURL'] + "\""
        newDicts['status'] = 'free'
        free_conf.append(newDicts)

    for conf_no in range(len(paid_data)):
        newDicts = {key: value for (key, value) in paid_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue' or key == 'confUrl'}
        if not newDicts['imageURL'].startswith("\""):
            newDicts['imageURL'] = "\"" + newDicts['imageURL'] + "\""
        newDicts['status'] = 'paid'
        paid_conf.append(newDicts)

    for each_conf in free_conf:
        m = confDB(**each_conf)
        m.save()

    for each_conf in paid_conf:
        m = confDB(**each_conf)
        m.save()

    message = 'ok'

    return HttpResponse(message)
'''
