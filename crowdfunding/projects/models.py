from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

FACILITIES = "Facilities"
RESOURCES = "Resources"
EXPOSURE = "Exposure"
EXPERTISE = "Expertise"
NEEDS = [
    (FACILITIES, "Facilities"),
    (RESOURCES, "Resources"),
    (EXPOSURE, "Exposure"),
    (EXPERTISE, "Expertise")
]

START = "Start"
TRIAL = "Trial"
ADJUST = "Adjust"
RETAIL = "Retail"
STAGES = [
    (START, "Start"),
    (TRIAL, "Trial"),
    (ADJUST, "Adjust"),
    (RETAIL, "Retail")
]

class Update(models.Model):
    update_content = models.TextField(max_length=5000, verbose_name="project update")
    update_date = models.DateTimeField(verbose_name="updated on")
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='updates',
        verbose_name="project"
    )
    update_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="project_update_author"
    )

class Project(models.Model):
    project_name = models.CharField(max_length=100, verbose_name="project", default="New Project")
    project_intro = models.TextField(max_length=500, verbose_name="introduction", default="A brief intro to the Project goes here.")
    project_goal = models.IntegerField(verbose_name="project goal", default=12)
    category = models.CharField(max_length=20, verbose_name="needs", choices=NEEDS, default=EXPERTISE)
    project_stage = models.CharField(max_length=10, verbose_name="stage", choices=STAGES, default=START)
    project_story = models.TextField(max_length=5000, verbose_name="story", default="The project owners background story goes here.")
    project_faq = models.TextField(max_length=5000, verbose_name="FAQ", default="A list of FAQ goes here.")
    project_image = models.URLField(verbose_name="project image", default="https://via.placeholder.com/300.jpg")
    is_open = models.BooleanField(verbose_name="project status")
    date_created = models.DateTimeField(verbose_name="project commenced")
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "project_owner"
    )

class Pledge(models.Model):
    pledge_quantity = models.IntegerField(verbose_name="amount pledged", default=1)
    pledge_description = models.CharField(max_length=200, verbose_name="description of pledge", default="All the details about what is being promised to be given do here.")
    anonymous = models.BooleanField(verbose_name="maintain privacy")
    terms_privacy = models.BooleanField(verbose_name="accept Terms and Privacy", default=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges',
        verbose_name="project"
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="pledge_supporter"
    )
    is_fulfilled = models.BooleanField(verbose_name="promise fulfilled", default=False)



