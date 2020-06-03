from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('single', views.single, name='single'),
]