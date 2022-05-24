
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
   path('' , home , name='home' ),
   path('login/' ,login  , name='login'),
   path('signup/' , signup ),
   path('add-todo/' , add_todo ),
   path('delete-todo/<int:id>' , delete_todo ),
   path('change-status/<int:id>/<str:status>' , change_todo ),
   path('logout/' , signout ),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'),
]
