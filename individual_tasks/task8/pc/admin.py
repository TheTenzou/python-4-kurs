from django.contrib import admin

from .models import Computer, Cpu, Gpu
# Register your models here.

admin.site.register(Computer)
admin.site.register(Cpu)
admin.site.register(Gpu)