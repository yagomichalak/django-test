from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class HomeView(ListView):
	""" View for the main page. """

	model = models.HomeOverview
	template_name = 'home/home.html'
	context_object_name = 'homeoverview'