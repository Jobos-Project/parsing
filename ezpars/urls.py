from django.urls import path, include, re_path
from ezpars.views import *

urlpatterns = [
    path('jobs/', get_adzuna)
]
