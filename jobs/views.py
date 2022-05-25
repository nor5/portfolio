from django.shortcuts import render
from .models import Job
# Create your views here.
def allJobs(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})
   
def selectJob(request, id_job):
   
    try:

      Selectjob = Job.objects.filter(id=id_job)

     
    except Job.DoesNotExist:
            raise Http404

    return render (request, 'jobs/jobdetails.html', {'selectjob': Selectjob })