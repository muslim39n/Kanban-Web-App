from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Organization

class OrganizationListView(ListView):
    model = Organization
    template_name='orgs.html'

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'org_detail.html'
