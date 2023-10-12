from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #URL:포트 ->ㅡ먀ㅜㅎ페이지(posting)
    path('', views.index, name='index'),
    #URL:포트/blog접속 ->blog페이지(posting)
    path('blog/',views.blog, name='blog'),
    #URL:포트/blog/숫자로 접속 ->게시글-세부페이지(posting)
    path('blog/<int:pk>',views.posting, name="posting")
]

