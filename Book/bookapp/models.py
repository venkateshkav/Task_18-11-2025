from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    category = models.CharField(choices=[("Fiction","Fiction"),("Science","Science"),("History","History")])
    price = models.FloatField()
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    