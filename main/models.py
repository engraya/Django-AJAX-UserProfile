from django.db import models

# Create your models here.


class Profile(models.Model):
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    age = models.IntegerField()
    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.firstName

