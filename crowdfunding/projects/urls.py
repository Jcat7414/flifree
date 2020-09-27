from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/createproject/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('projects/owner/<project_owner>/', views.FounderProjectList.as_view()),
    path('projects/facilities/', views.FacilitiesProjectList.as_view()),
    path('projects/resources/', views.ResourcesProjectList.as_view()),
    path('projects/exposure/', views.ExposureProjectList.as_view()),
    path('projects/expertise/', views.ExpertiseProjectList.as_view()),
    path('projects/stage/start/', views.StartProjectList.as_view()),
    path('projects/stage/trial/', views.TrialProjectList.as_view()),
    path('projects/stage/adjust/', views.AdjustProjectList.as_view()),
    path('projects/stage/retail/', views.RetailProjectList.as_view()),
    path('projects/<int:pk>/pledgesfor/<pledges>/', views.ProjectPledgeList.as_view()),
    path('projects/<int:pk>/updatesfor/<updates>/', views.ProjectUpdateList.as_view()),
    path('projects/<int:pk>/pledged/', views.ProjectPledgeAmount.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/createpledge/', views.PledgeList.as_view()),
    path('pledges/amounts/', views.PledgeAmountList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('pledges/<pledge_supporter>/', views.SupporterPledgeList.as_view()),
    path('updates/', views.UpdateList.as_view()),
    path('updates/createupdate/', views.UpdateList.as_view()),
    path('updates/<int:pk>/', views.UpdateDetail.as_view()),
    path('updates/<update_author>/', views.FounderUpdateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)