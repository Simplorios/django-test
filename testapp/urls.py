from . import views

from django.urls import path
from .dashapp import app

urlpatterns = [
    path('', views.home),
]
