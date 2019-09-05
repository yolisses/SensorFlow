from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import *

admin.site.register(User)
admin.site.register(Enviroment)
admin.site.register(Board)
admin.site.register(Type)
admin.site.register(Sensor)
admin.site.register(Data)