from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    contact_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField(null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Skill(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        unique_together = ['title','user']


class Education(models.Model):
    course = models.CharField(max_length=100)
    passed_year = models.CharField(max_length=10,blank=True,null=True)
    institution = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        unique_together = ['course','user']

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        unique_together = ['job_title','user']