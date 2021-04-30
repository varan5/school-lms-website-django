from django.db import models
from django.contrib.auth.models import User
import os

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    extension = filename.split('.')[-1]
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, extension)
    return os.path.join(upload_to, filename)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to=path_and_rename, blank=True)
    
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username