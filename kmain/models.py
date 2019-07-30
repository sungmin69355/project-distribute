from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) #제목 받아오기
    content = models.TextField()             # 내용 받아오기
    image = models.FileField()              #이미지 받아오기

class Kimchi(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/', default='test')
    body = models.TextField()

    def __str__(self):
        return self.title