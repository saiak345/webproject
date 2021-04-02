from django.db import models

# Create your models here.
class student(models.Model):
    name= models.CharField(max_length=1000)
    fname=models.CharField(max_length=1000)
    classname=models.IntegerField()
    contact=models.CharField(max_length=1000)
    class Meta:
        ordering=('id',)
        def __str__(self):
            return self.name
