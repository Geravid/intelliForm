"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]"""

# myapp/urls.py
from django.urls import path
from .views import form_view

urlpatterns = [
    path('', form_view, name='index'),
]