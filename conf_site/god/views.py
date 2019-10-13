from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    response = requests.get(
        'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

    conf_data = response.json()

    paid_data = conf_data['paid']
    free_data = conf_data['free']
    paid_conf = []
    free_conf = []

    for conf_no in range(len(free_data)):
        newDicts = {key: value for (key, value) in free_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue'}
        newDicts['status'] = 'free'
        free_conf.append(newDicts)

    for conf_no in range(len(paid_data)):
        newDicts = {key: value for (key, value) in paid_data[conf_no].items(
        ) if key == 'imageURL' or key == 'confEndDate' or key == 'confStartDate' or key == 'confName' or key == 'venue'}
        newDicts['status'] = 'paid'
        paid_conf.append(newDicts)

    return render(request, 'god/index.html', {
        'paid': paid_conf,
        'free': free_conf
    })
