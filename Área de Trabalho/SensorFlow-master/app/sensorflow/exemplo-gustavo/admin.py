from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Producer)
admin.site.register(models.Actor)
admin.site.register(models.Director)
admin.site.register(models.Evaluation)
admin.site.register(models.Movie)
admin.site.register(models.Cast)