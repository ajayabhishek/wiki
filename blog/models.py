from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
import os
from django.conf import settings


User=get_user_model()

class Article(models.Model):
    cat_id = models.CharField(max_length=200)
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    title=models.CharField(max_length=200)    
    content = RichTextUploadingField(blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    def _str_(self):
        return self.title

class category(models.Model):
    cat_id=models.ForeignKey(Article, on_delete=models.CASCADE,default=4)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    def _str_(self):
        return self.cat_name

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)
