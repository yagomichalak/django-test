from django.shortcuts import render
from django.views.generic import ListView
from . import models

from rest_framework import viewsets
from .serializers import ProductSerializer
from products.models import ProductsModel

# Create your views here.

class HomeView(ListView):
	""" View for the main page. """

	model = models.HomeOverview
	template_name = 'home/home.html'
	context_object_name = 'homeoverview'

class ProductViewSet(viewsets.ModelViewSet):
	queryset = ProductsModel.objects.all().order_by('date_inserted')
	serializer_class = ProductSerializer
	http_method_names = ['get']