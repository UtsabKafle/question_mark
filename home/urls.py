
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('a',archive),
    path('p/<id>',page_view)
]