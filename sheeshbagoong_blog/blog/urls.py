from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('post/create/', post_create_view, name='post_create'),
    path('post/<slug:slug>/', post_detail_view, name='post_detail'),
    path('post/<slug:slug>/edit/', post_edit_view, name='post_edit'),
    path('post/<slug:slug>/delete/', post_delete_view, name='post_delete'),
]
