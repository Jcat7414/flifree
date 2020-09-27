from django.contrib import admin
from .models import Project, Pledge, Update

# Register your models here.

admin.site.register(Project)
admin.site.register(Pledge)
admin.site.register(Update)