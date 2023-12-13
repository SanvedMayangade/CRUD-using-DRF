from django.urls import path
from .views import *

urlpatterns = [
  path('',get, name='create'),
  path('post-data', post_data, name='post'),
  path('update-data/<int:pk>', update_data, name='update'),
  path('delete-data/<int:pk>',delete_data, name='delete'),
  

]