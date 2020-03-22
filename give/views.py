from django.shortcuts import render
from django.views.generic import TemplateView 

class GivepageView(TemplateView): 
    template_name = 'give/give_page.html'

# Create your views here.
