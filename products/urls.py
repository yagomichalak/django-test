from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductsView.as_view(), name="list"),
    path('product/<slug>', views.ProductDetailView.as_view(), name="detail"),
]