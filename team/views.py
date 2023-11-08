from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import  Team


class TeamListView (ListView):
    model: Team
    context_object_name = 'team_list' 
    template_name= 'team/team_listings.html'

    def get_queryset(self):
          return Team.objects.order_by('pk')



class TeamDetailView (DetailView):

    model: Team
    context_object_name = 'team' 
   
    template_name= 'team/team_detail.html'

    def get_queryset(self):
          return Team.objects.order_by('pk')
