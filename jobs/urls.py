from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.allJobs, name='alljobs'),
    path('projects/<int:id_job>', views.selectJob, name='details'),
]
