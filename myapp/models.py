from django.db import models
from accounts.models import Users
# Create your models here.

class Channel(models.Model):
    owner=models.ForeignKey(Users, on_delete=models.CASCADE, related_name='channels')
    titel=models.CharField(max_length=150)
    description=models.TextField()
    avatar=models.ImageField(upload_to='photoes')
    created_at=models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    channel=models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='video')
    video_file=models.FileField(upload_to='videos/')
    titel=models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    owner=models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments')
    video=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='channels')
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    owner=models.ForeignKey(Users, on_delete=models.CASCADE, related_name='like')
    video=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='like')
    created_at=models.DateTimeField(auto_now_add=True)




    