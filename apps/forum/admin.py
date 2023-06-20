from django.contrib import admin
from .models import Tag, School, Section, CustomUser, Post, PostType, Comment, Reaction, ReactPost, SavePost, Report

# Register your models here.

admin.site.register(Tag)
admin.site.register(School)
admin.site.register(Section)
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(PostType)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(ReactPost)
admin.site.register(SavePost)
admin.site.register(Report)