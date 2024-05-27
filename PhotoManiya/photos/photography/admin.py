from django.contrib import admin

from photography.models import PhotoCategory, Post, Pictures, Like

admin.site.register(PhotoCategory)
admin.site.register(Post)
admin.site.register(Pictures)
admin.site.register(Like)
