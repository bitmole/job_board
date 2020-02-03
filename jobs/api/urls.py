from django.urls import path
from jobs.api.views import job_list_create_api_view, job_detail_api_view

urlpatterns = [
        path('jobs', job_list_create_api_view, name='job-list'),
        path('jobs/<int:pk>', job_detail_api_view, name='job-detail'),
]
