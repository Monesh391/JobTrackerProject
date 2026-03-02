from django.urls import path
from .views import JobListCreateView, JobDetailView, AnalyticsView
from .views import JobStatsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('jobs/stats/', JobStatsView.as_view(), name='job-stats'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]