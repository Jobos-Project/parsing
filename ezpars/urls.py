from django.urls import path, include, re_path
from ezpars.views import *

urlpatterns = [
    path('download_jobs/', get_adzuna),
    path('show_jobs/', JobsView.as_view())
]
