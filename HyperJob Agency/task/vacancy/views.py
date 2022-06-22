from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

# Create your views here.
class MyResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/index.html', {'resumes': models.Resume.objects.all()})


