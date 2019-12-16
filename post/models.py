from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name= 'PROJE ')
    content = models.TextField(verbose_name= 'Tanım')
    publishing_date = models.DateTimeField(verbose_name= 'Yayımlanma Tarihi', auto_now_add=True)

    def __str__(self):
        return self.title