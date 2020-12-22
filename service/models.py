from django.db import models

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    price = models.IntegerField()
    inclusion_one = models.CharField(max_length=100, blank=True)
    inclusion_two = models.CharField(max_length=100, blank=True)
    inclusion_three = models.CharField(max_length=100, blank=True)
    inclusion_four = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_title