from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models

# Create your views here.

class ProductsView(ListView):
	""" View for all products. """

	model = models.ProductsModel
	template_name = 'products/list.html'
	context_object_name = 'products'
	ordering = ['date_inserted']


class ProductDetailView(DetailView):
	""" View for a specific product. """

	model = models.ProductsModel
	template_name = 'products/detail.html'
	context_object_name = 'product'
	slug_url_kwarg = 'slug'