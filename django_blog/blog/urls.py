from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('users/', views.ListUserView.as_view(), name='user-list'),
    path('users/<int:id>/', views.post_list, name='user-detail'),
    path('<int:pk>/', views.DetailPostView.as_view(), name='post-detail'),
    path('create/', views.create_post, name='create-post'),
    path('<int:pk>/update/', views.update_post, name='update-post')

]
