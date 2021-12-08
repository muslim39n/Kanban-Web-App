from django.urls import path

from .views import SignUpView, CustomUserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]