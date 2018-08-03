from django.urls import path
from ezpars.views import *

urlpatterns = [
    path('download_jobs/', get_adzuna),
    path('github_jobs/', GithubJob.as_view()),
    path('show_jobs/', JobsView.as_view())
]
