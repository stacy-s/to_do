from time import time

from django.conf import settings
from django.db import models
# Create your models here.
from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + str(int(time()))


class Tag:
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=30)
    name = models.TextField(verbose_name='name', max_length=15)


class Task(models.Model):
    priority_list = [
        (1, 'low'),
        (2, 'medium'),
        (3, 'high'),
    ]
    id = models.AutoField(primary_key=True, null=False)
    creation_datetime = models.DateTimeField(auto_now_add=True, null=False)
    title = models.TextField(verbose_name='title', max_length=30, blank=False, null=False)
    comment = models.TextField(verbose_name='comment', max_length=150, null=False)
    slug = models.SlugField(max_length=50, null=False)
    deadline = models.DateField(verbose_name='deadline')
    priority = models.PositiveSmallIntegerField(verbose_name='priority', blank=False, choices=priority_list, null=False)
    is_finished = models.BooleanField(verbose_name='done', default=False, null=False)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
