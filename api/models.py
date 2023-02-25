from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Work(models.Model):
    WORK_CHOICES = [
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    ]

    _id = models.AutoField(primary_key=True, editable=False)
    link = models.URLField(max_length=200)
    work_type = models.CharField(max_length=30,choices=WORK_CHOICES,default='Other')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.work_type)

class Artist(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    work = models.ManyToManyField(Work)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)





