from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name
    