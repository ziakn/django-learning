from django.db import models

class  category(models.Model):
    id = models.AutoField(primary_key= True)
    author = models.IntegerField(default='NULL')
    title = models.CharField(max_length=255, default='NULL')
    parent_id = models.IntegerField(default=0)
    cover_id = models.IntegerField(default='NULL')
    status = models.IntegerField(default=1)
    slug = models.SlugField(default="", null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
