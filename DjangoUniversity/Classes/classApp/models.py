from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True)
    Duration = models.FloatField(default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Title
