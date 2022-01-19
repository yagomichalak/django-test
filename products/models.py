from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here.

class ProductsModel(models.Model):
	""" Model for the Products. """

	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)
	date_inserted = models.DateTimeField(auto_now_add=True)


	def save(self, *args, **kwargs):
		if not self.slug:
			# Get current timestamp
			epoch = datetime.utcfromtimestamp(0)
			the_time = (datetime.utcnow() - epoch).total_seconds()
			slug = f'{slugify(self.name)}-{slugify(self.language)}-{slugify(the_time)}'
			self.slug = slug

		super().save(*args, **kwargs)

		def __str__(self):
			return f"{self.name}"

	class Meta:
		verbose_name = 'Products'
		verbose_name_plural = 'Product'