from django.db import models

# Create your models here.
class Slider(models.Model):
    img = models.ImageField(upload_to = 'static/Images')
    Title = models.CharField(max_length=250)
    Description = models.TextField()

    def __str__(self):
        return self.Title


class Post(models.Model):
    img = models.ImageField(upload_to = 'static/Images')
    Title = models.CharField(max_length=250)
    Description = models.TextField()

    def __str__(self):
        return self.Title


class Contact(models.Model):
    Company_name = models.CharField(max_length=200)
    Address = models.TextField()
    Location = models.TextField()

    def __str__(self):
        return self.Company_name
