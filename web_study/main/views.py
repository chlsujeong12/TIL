from django.shortcuts import render

#view에서 Model(post게시글)가져오기
from .models import Post

# Create your views here.
def index(request):
    return render (request,'main/index.html')

def blog(request):
 
    #모든 Post가져와 postlis에 저장
    postlist = Post.objects.all()
    #blog.html 페이지 열때 모든 Post인 postlist도 같이 가져옴

    return render(request, 'main/blog.html', {'postlist':postlist})
#blog의 게시글(posting)
def posting(request, pk):
    #게시글 중 pk를 이용해 하나의 게시글 검색
    post = post.objects.get(pk=pk)
    #posting.html페이지 열때, 찾아낸 게시글을 post라는 이름으로 가져옴
    return render(request, 'main.posting.html', {'post':post})