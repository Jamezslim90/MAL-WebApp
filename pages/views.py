from django.shortcuts import render
from django.views.generic import TemplateView 



class HomePageView(TemplateView):

    template_name = 'pages/index.html'



class AboutPageView(TemplateView):
    
    template_name = 'pages/about.html'



class ContactPageView(TemplateView):
    
    template_name = 'pages/contact.html'


class ServicePageView(TemplateView):
    
    template_name = 'pages/services.html'


class VideoPageView(TemplateView):
    
    template_name = 'pages/video.html'