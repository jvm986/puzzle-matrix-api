from django.contrib import admin
from puzzle import models

admin.site.register(models.Word)
admin.site.register(models.Category)
admin.site.register(models.Group)
admin.site.register(models.Puzzle)
