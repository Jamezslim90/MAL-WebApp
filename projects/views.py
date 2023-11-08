from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import  Project


class ProjectListView (ListView):
    model: Project
    context_object_name = 'project_list' 
    template_name= 'projects/project_listings.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)

       
        # How many leads we have in total
        commercial = Project.objects.filter(category=2)
        institutional = Project.objects.filter(category=3)
        religious = Project.objects.filter(category=4)
        residential = Project.objects.filter(category=1)

        context.update({
            "commercial": commercial,
            "institutional": institutional,
            "religious": religious,
            "residential": residential
        })
        return context


class ProjectDetailView (DetailView):

    model: Project
    context_object_name = 'project' 
   
    template_name= 'projects/project_detail.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')
