from background_task import background
from .views import get_adzuna, GithubJob


@background(schedule=7200)
def task():
    get_adzuna()
    GithubJob.get()