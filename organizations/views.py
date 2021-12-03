from django.shortcuts import render
from django.views.generic import ListView

from .models import Organization

class OrganizationListView(ListView):
    model = Organization
    template_name='orgs.html'
