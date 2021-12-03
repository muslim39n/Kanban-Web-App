from django.urls import path

from .views import OrganizationListView

urlpatterns = [
    path('all/', OrganizationListView.as_view(), name='orgs-all'),
]