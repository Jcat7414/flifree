from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="allProjects"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeList.as_view()),
    path('updates/', views.UpdateList.as_view()),
    path('updates/<int:pk>/', views.UpdateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)