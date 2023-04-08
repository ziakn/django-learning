from django.db import models

# Create your models here.
class  Image(models.Model):
    # image = models.ImageField(upload_to='media/')
    id = models.AutoField(primary_key= True)
    author = models.IntegerField()
    status = models.IntegerField(default=1)
    salt = models.IntegerField()
    title = models.CharField(max_length=255, default='NULL')
    filename = models.CharField(max_length=255, default='NULL')
    extension = models.CharField(max_length=5, default='NULL')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

