
from rest_framework import serializers

from products.models import ProductsModel


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductsModel
		fields = ('name', 'date_inserted', 'description', 'slug')