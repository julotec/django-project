from django.contrib import admin
from django.urls import path, include
from noteapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('noteapp.urls')),
    path('users/', include('users.urls')),
    path('scrape/', views.scrape_quotes, name='scrape_quotes'),
    path('author_details/<int:author_id>/', views.author_detail, name='author_detail'),
    
]