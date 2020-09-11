from django.shortcuts import render
from django_plotly_dash.consumers import send_to_pipe_channel


def home(requests):
    return render(requests, 'testapp/home.html')