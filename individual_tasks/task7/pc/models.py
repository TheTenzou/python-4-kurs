from django.db import models

# Create your models here.

class Cpu(models.Model):
    name = models.CharField(max_length=30)
    core_count = models.IntegerField()
    core_clock = models.FloatField()
    _hash = models.IntegerField()

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Gpu(models.Model):
    name = models.CharField(max_length=30)
    core_count = models.IntegerField()
    core_clock = models.FloatField()
    vram = models.IntegerField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Computer(models.Model):
    name = models.CharField(max_length=30)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name