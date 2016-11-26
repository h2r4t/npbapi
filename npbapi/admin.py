from django.contrib import admin
from .models import Scores, pastScore, Mail

admin.site.register(Scores)
admin.site.register(pastScore)
admin.site.register(Mail)

# Register your models here.
