from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import (DetailView)

from . import models

class SensorCreateView(CreateView):
    model= models.Sensor
    template_name='HTML/sensores.html'
    fields= ['name']
    sucess_url = reverse_lazy('sensor-list')

class SensorListView(ListView):

    model= models.Sensor
    template_name= 'HTML/sensores.html'