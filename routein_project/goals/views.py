from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Goals
# Create your views here.

class GoalsCreateView(CreateView):
    model = Goals
    fields = '__all__'
    template_name = 'goals.html'
