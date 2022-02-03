from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src ="{obj.photo.url}" width="50">')
        return '_'

    get_photo.short_discription = 'фото'


class CategoryPhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class WorkPostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'photo', 'get_photo')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src ="{obj.photo.url}" width="50">')
        return '_'
    get_photo.short_discription = 'фото'

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'start_time', 'end_time', 'number', 'email', 'instagram', 'name')


class ProcedureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'slug', 'time')


admin.site.register(CategoryPost, CategoryPostAdmin)
admin.site.register(CategoryPhoto, CategoryPhotoAdmin)
admin.site.register(WorkPhotos, WorkPostsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Procedure, ProcedureAdmin)
