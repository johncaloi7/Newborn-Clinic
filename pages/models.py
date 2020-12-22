from django.db import models

# Create your models here.
class Detail(models.Model):
    header = models.CharField(max_length=20, default="Page details")
    # home page communicate with us details
    home_comm_paragraph = models.TextField(max_length=400)
    #  we care for you details
    home_care_paragraph = models.TextField(max_length=400)
    # we'll be on time paragraph
    home_ontime_paragraph = models.TextField(max_length=400)
    # vision details
    vision_paragraph = models.TextField(max_length=400)

    # about page
    about_first_paragraph = models.TextField()
    about_second_paragraph = models.TextField()


    def __str__(self):
        return self.header