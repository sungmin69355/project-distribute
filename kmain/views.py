from django.shortcuts import render, get_object_or_404,redirect, redirect
from django.core.paginator import Paginator
from .models import Post
from .models import Kimchi

def home(request):
    return render(request, 'index.html')

def card(request):
    kimchis = Kimchi.objects 
    kimchi_list = Kimchi.objects.all() #블로그 모든 글들 대상으로
    paginator = Paginator(kimchi_list, 12) #블로그 객체 3개를 한페이지로 자르기
    page = request.GET.get('page') #rq된 페이지가 뭔지를 알아내고 (rq페이지를 변수에 담다)
    posts = paginator.get_page(page) #rq된 페이지를 얻어온뒤 rt해준다
    return render(request, 'archive.html', {'kimchis' : kimchis, 'posts' : posts})


def detail(request, kimchi_id):
    kimchi_detail = get_object_or_404(Kimchi, pk = kimchi_id)
    #이용자가 원한 몇번 블로그 객체
    return render(request, 'detail.html',{'kimchi' : kimchi_detail})

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    return render(request, "review.html", {
        'post_list' : qs,
        'q' : q,
    })


def post_like(request, pk):
  post = get_object_or_404(Post, pk=pk)
  # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
  post_like, post_like_created = post.like_set.get_or_create(user=request.user)

  if not post_like_created:
    post_like.delete()

    return redirect('post:post_list')