from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    department = models.CharField(choices=[("IT","IT"),("CSE","CSE"),("EEE","EEE"),("ECE","ECE")])
    marks = models.PositiveIntegerField(max_length=100)
    attendance = models.PositiveIntegerField(max_length=100)
    year = models.PositiveIntegerField()
    city = models.CharField()
    mentor = models.CharField()
    fees_paid = models.PositiveIntegerField()

    def __str__(self):
        return self.name
