from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from . import models
import os

from rest_framework import viewsets
from .serializers import ProductSerializer
from products.models import ProductsModel
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from utils import utils

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


		products_json = {}
		
		p = os.path.join(settings.STATIC_ROOT, ('assets/json/products.json'))
		with open(p, 'r', encoding="utf-8") as f:
			f = f.read().strip()\
			.replace("'", '"')\
			.replace('datetime.datetime', '"datetime.datetime')\
			.replace(')', ')"')\
			.replace('datetime.date(', '"datetime.date(')\
			.replace(', tzinfo=<UTC>', '')

			products_json = json.loads(f)


			products_json = utils.format_date(products_json)
			products_json = utils.group_products(products_json)
			print(products_json)



		self.context = {
			'all_products': ProductsModel.objects.filter(),
			'endpoint': 'http://localhost:8000',
			'all_products_json': products_json
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