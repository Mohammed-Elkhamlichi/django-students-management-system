from django.db import models
# Create your models here.
## Student Model.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    def __str__(self):
        result = str(self.first_name + " " + self.last_name)
        return result