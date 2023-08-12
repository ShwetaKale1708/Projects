from django.contrib import admin
from .models import Candidate, Userinfo
# Register your models here.
admin.site.register(Userinfo)
admin.site.register(Candidate)