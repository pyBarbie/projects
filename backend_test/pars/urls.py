from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.UrlsListView.as_view(), name='home-page'),
    path('parse/<int:id>/', views.parse, name='parse-detail')
]
