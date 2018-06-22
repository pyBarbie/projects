from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog-id'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    path('<int:pk>/create/', views.CommentCreate.as_view(), name='create'),
]
