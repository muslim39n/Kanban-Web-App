from django.urls import path

from .views import (
    OrganizationDetailView,
    OrganizationListView,

)

urlpatterns = [
    path('all/', OrganizationListView.as_view(), name='orgs-all'),
    path('<int:pk>/', OrganizationDetailView.as_view(), name='org-detail')
]