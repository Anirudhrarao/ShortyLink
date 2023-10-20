from django.db import models
from django.contrib.auth.models import User

class ShortenedURL(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    long_url = models.URLField(max_length=200,verbose_name="Long URL")
    short_code = models.CharField(max_length=20,unique=True,verbose_name="Short code")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created at")

    def __str__(self):
        return self.short_code

    