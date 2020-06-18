from django.db import models
# Create your models here.


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
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    title = models.TextField(verbose_name='title', max_length=30, blank=False)
    comment = models.TextField(verbose_name='comment', max_length=150)
    slug = models.SlugField(max_length=40)
    deadline = models.DateTimeField(verbose_name='deadline')
    priority = models.PositiveSmallIntegerField(verbose_name='priority', blank=False, choices=priority_list)
    is_finished = models.BooleanField(verbose_name='done', default=False)
    tags = models.ManyToManyField(Tag)
