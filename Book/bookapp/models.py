from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    Author = models.CharField()
    Category = models.CharField(choices=[("Fiction","Fiction"),("Science","Science"),("History","History")])
    Price = models.PositiveIntegerField()
    published_date = models.DateField()
    is_available = models.CharField(choices=[("Yes","Yes"),("No","No")])

    def __str__(self):
        return self.title