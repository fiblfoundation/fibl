
from django.urls import path, include, re_path
from lottery.views import client


app_name = 'lottery'

urlpatterns = [
    path('', client, name='client'),

]