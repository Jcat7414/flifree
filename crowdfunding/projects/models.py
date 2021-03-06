from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

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
    needs_facilities = models.BooleanField()
    needs_resources = models.BooleanField()
    needs_exposure = models.BooleanField()
    needs_expertise = models.BooleanField()
    project_stage = models.CharField(max_length=10)
    project_story = models.TextField(max_length=5000)
    project_needs = models.TextField(max_length=5000)
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
    sup_facilities = models.BooleanField()
    sup_resources = models.BooleanField()
    sup_exposure = models.BooleanField()
    sup_expertise = models.BooleanField()
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
    