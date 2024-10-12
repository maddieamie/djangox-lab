from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import CustomModel

class CustomModelListView(ListView):
    model = CustomModel
    template_name = 'pages/news/model_list.html'

class CustomModelDetailView(DetailView):
    model = CustomModel
    template_name = 'pages/news/model_detail.html'
