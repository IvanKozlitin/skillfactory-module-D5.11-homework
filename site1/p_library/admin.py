from django.contrib import admin
from .models import (Book, Author, PublishingHouse)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_release', 'ISBN')
    list_filter = ('copy_count', 'year_release',)
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country')
    list_filter = ('country',)


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_filter = ('works',)
    list_display = ('name', 'phone', 'email', 'city', 'country', 'works')
