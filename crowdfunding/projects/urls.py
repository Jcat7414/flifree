from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects/<project_owner>/', views.FounderProjectList.as_view()),
    path('projects/<int:pk>/<pledges>/', views.ProjectPledgeList.as_view()),
    # path('projects/<int:pk>/pledges/', views.ProjectPledgeList.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('pledges/<pledge_supporter>/', views.SupporterPledgeList.as_view()),
    path('updates/', views.UpdateList.as_view()),
    path('updates/<int:pk>/', views.UpdateDetail.as_view()),
    path('updates/<update_author>/', views.FounderUpdateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)