from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_details, name='article_details'),
]
