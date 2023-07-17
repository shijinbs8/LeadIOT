from django.contrib import admin

from .models import Classroom,Bulb,Status,Motiondetection


admin.site.register(Classroom)
admin.site.register(Bulb)
admin.site.register(Status)
admin.site.register(Motiondetection)