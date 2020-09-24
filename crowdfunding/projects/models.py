from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.db.models import Count, Sum


class Update(models.Model):
    update_name = models.CharField(max_length=100)
    update_content = models.TextField(max_length=5000)
    update_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='updates',
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="update_author"
    )


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_intro = models.TextField(max_length=500)
    project_goal = models.IntegerField()
    category = models.CharField(max_length=20)
    project_stage = models.CharField(max_length=10)
    project_story = models.TextField(max_length=5000)
    project_faq = models.TextField(max_length=5000)
    project_image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_amended = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "project_owner"
    )


class Pledge(models.Model):
    pledge_quantity = models.IntegerField()
    pledge_description = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    terms_privacy = models.BooleanField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="pledge_supporter",
        verbose_name="supporter"
    )
    is_fulfilled = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges',
        verbose_name="project pledges"
    )

    @property
    def percent_pledged(self):
        return ((int(self.pledge_quantity) / int(self.project.project_goal)) * 100)
    