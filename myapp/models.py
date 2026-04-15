from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=[('done','Done'),('notdone','Not Done')])