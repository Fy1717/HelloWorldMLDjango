from django.urls import path
from .views import *

urlpatterns = [
    path('index/', post_index, name='index'),
    path('detail/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('update/', post_update, name='update'),
    path('delete/', post_delete, name='delete'),
]