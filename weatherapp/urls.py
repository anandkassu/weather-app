from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='home'),
    url('delete/<city_name>/', views.delete_city, name='delete_city'),
]