from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class VipPost(models.Model):
    catlist = (
        ("Sport","Sport"),
        ("Business","Business"),
        ("Food","Food"),
        ("Tech","Tech"),
        ("Design","Design"),
        ("Travel","Travel"),
        ("Culture","Culture"),
        ("Politics","Politics"),
        ("Celebrity","Celebrity"),
        ("Other","Other"),
    )
    category = models.CharField(max_length=50, choices=catlist)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vip-post-detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("tranding-vip-post-detail", kwargs={"pk": self.pk})

class Post(models.Model):
    catlist = (
        ("Sport","Sport"),
        ("Business","Business"),
        ("Food","Food"),
        ("Tech","Tech"),
        ("Design","Design"),
        ("Travel","Travel"),
        ("Culture","Culture"),
        ("Politics","Politics"),
        ("Celebrity","Celebrity"),
        ("Other","Other"),
    )
    category = models.CharField(max_length=50, choices=catlist)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("tranding-post-detail", kwargs={"pk": self.pk})

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name