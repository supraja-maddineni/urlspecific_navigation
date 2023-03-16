from django.urls import path
from mi.views import *
app_name='nothing'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]