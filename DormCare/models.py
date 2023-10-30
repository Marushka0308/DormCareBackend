from django.db import models

class User(models.Model):
    registration_number = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    room_number = models.CharField(max_length=255, blank=True, null=True)
    hostel_block = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Complaints(models.Model):
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    complaints = models.CharField(max_length=255)
    likes = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.complaints

class Announcements(models.Model):
    announcement = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.announcement