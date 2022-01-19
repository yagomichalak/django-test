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
	context_object_name = 'general'

	#queryset = ProductsModel.objects.all().order_by('date_inserted')
	

	
	def setup(self, *args, **kwargs):
		super().setup(*args, **kwargs)

		self.context = {}
		self.context = {
			'all_products': ProductsModel.objects.filter(),
			'endpoint': 'http://localhost:8000'
		}
		
		self.render = render(
			self.request, self.template_name, self.context
		)

	def get(self, *args, **kwargs):
		return self.render

class ProductViewSet(viewsets.ModelViewSet):
	queryset = ProductsModel.objects.all().order_by('date_inserted')
	serializer_class = ProductSerializer
	http_method_names = ['get']