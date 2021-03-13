from django.contrib import admin

from .models import Computer, Cpu, Gpu
# Register your models here.

class ComputerModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']
    list_filter = ['gpu', 'cpu']

    class Meta:
        medel = Computer


class CpuModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']

    class Meta:
        medel = Cpu
        

class GpuModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']

    class Meta:
        medel = Gpu

admin.site.register(Computer, ComputerModelAdmin)
admin.site.register(Cpu, CpuModelAdmin)
admin.site.register(Gpu, GpuModelAdmin)