from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    emailId= models.EmailField()
    contact= models.CharField(max_length=200)
    access=models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.name
