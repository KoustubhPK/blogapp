from django.contrib import admin
from .models import VipPost, Post, ContactUs

# Register your models here.

admin.site.register(VipPost)
admin.site.register(Post)
admin.site.register(ContactUs)