from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='portfolio/image')
    url=models.URLField(blank=True)
