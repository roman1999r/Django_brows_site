import datetime
import uuid

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
from django.urls import reverse

"""
Category model:
title, slug

WorkPhotos

title, slug, created_at, photo, category


Post
title, slug, content,created_at, photo, views, category
"""


class CategoryPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категорія поста'
        verbose_name_plural = 'Категорії постів'
        ordering = ['title']


class CategoryPhoto(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категорія фото'
        verbose_name_plural = 'Категорії фото'
        ordering = ['title']


class WorkPhotos(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, default=uuid.uuid1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(CategoryPhoto, on_delete=models.PROTECT, related_name='workphotos')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('workphotos', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-created_at']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, default=uuid.uuid1)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(CategoryPost, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-created_at']


class Procedure(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, default=uuid.uuid1)
    name = models.CharField(max_length=255)
    time = models.TimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('procedure', kwargs={"slug": self.slug})


class Event(models.Model):
    title = models.ForeignKey(Procedure, on_delete=models.PROTECT, related_name='event')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, default=uuid.uuid1)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank= True, null= True)
    name = models.TextField(max_length=255)
    number = models.TextField(max_length=15)
    email = models.EmailField(max_length=50)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={"slug": self.slug})
