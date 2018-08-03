from django.urls import path, include, re_path

urlpatterns = [
    path('api/', include('ezpars.urls'))
]
