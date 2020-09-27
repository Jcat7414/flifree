from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/createuser/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/founders/', views.FoundersList.as_view()),
    path('users/supporters/', views.SupportersList.as_view()),
    path('users/staff/', views.StaffList.as_view()),
    path('users/newsletter/', views.NewsletterList.as_view()),
    path('users/admin/<int:pk>/', views.AdminUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)