from django.urls import path, include
from . import views
from django.conf.urls import url

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)


app_name = 'homepage'

urlpatterns = [
    path('', views.HomeView.as_view(), name="overview"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]