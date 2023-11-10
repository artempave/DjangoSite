from django.db import models
import os
from django.conf import settings
import datetime


class Articales(models.Model):
    @staticmethod
    def file_path(self, filename):
        media_path = settings.MEDIA_ROOT + 'articles/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        ext = filename.split('.')[-1]
        new_filename = f'{self.title}.{ext}'
        full_path = os.path.join(media_path, new_filename)
        return full_path

    def extension(self):
        name, extension = os.path.splitext(self.picture.name)
        return extension

    def image_extensions(self):
        return ['.jpg', '.png', '.jpeg', '.webp']

    title = models.CharField('название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    text = models.TextField('статья')
    time = models.DateTimeField('время публикации')
    picture = models.FileField(upload_to=file_path.__func__, null=True)
    def str(self):
        return self.title


class Custom_user(models.Model):
    @staticmethod
    def file_path(self, filename):
        media_path = settings.MEDIA_ROOT + 'articles/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        ext = filename.split('.')[-1]
        new_filename = f'{self.title}.{ext}'
        full_path = os.path.join(media_path, new_filename)
        return full_path

    def extension(self):
        name, extension = os.path.splitext(self.picture.name)
        return extension

    def image_extensions(self):
        return ['.jpg', '.png', '.jpeg', '.webp']

    title = models.CharField('название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    text = models.TextField('статья')
    time = models.DateTimeField('время публикации')
    picture = models.FileField(upload_to=file_path.__func__, null=True)
    avatar = models.FileField()
    def str(self):
        return self.title
