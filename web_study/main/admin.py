# Register your models here.
#관리자가 게시글에 접근할 권리를 준다.
#게시글 게시, 삭제, 수정, 저장 등 여러 작업을 할수 있게 해준다.

from django.contrib import admin

#게시글 (post) Model을 불러온다.
from . models import Post

#관리자(admin)가 게시글(Post)에 접근가능
admin.site.register(Post)