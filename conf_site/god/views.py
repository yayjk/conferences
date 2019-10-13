from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    response = requests.get(
        'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

    conf_data = response.json()

    free_data = conf_data['free']
    free_conf = []

    for conf_no in range(len(free_data)):
        newDicts = {key: value for (key, value) in free_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue' or key == 'confUrl'}
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
        paid_conf.append(newDicts)

    return render(request, 'god/paid.html', {
        'paid': paid_conf
    })
