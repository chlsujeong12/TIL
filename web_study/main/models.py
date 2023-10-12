from django.db import models

# Create your models here.
#게시글(post)엔 제목(postname),내용(contents)이 존재

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    #게시글의 제목(postname)이 post object (1)대신하기
    def __str__(self):
        return self.postname