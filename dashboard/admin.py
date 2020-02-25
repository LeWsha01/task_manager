from django.contrib import admin

from dashboard import models

admin.site.register(models.Project)
admin.site.register(models.Issue)
