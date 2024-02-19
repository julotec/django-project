from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('author_details/<int:author_id>/', views.author_detail, name='author_detail'),
    path('scrape/', views.scrape_quotes, name='scrape_quotes')
]

