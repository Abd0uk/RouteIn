from django.db import models

# Create your models here.
class Goals(models.Model):
    title = models.CharField(max_length=300)
    desired_date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    