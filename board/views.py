from django.shortcuts import render, redirect
from .models import Board
from django.core.paginator import Paginator

# Create your views here.

def unlikey(request, bpk): 
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail", bpk)

def likey(request, bpk): 
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:detail", bpk)

def index(request):
    # print(dir(request.user.is_authenticated))
    # print(dir(request.user.is_anonymous))  
    kw = request.GET.get("kw","")  
    cate = request.GET.get("cate","")
    page = request.GET.get("page", 1)
    if kw :
        if cate == "sub" :
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri": 
            try :
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except : 
                b = Board.objects.none()
        elif cate == "con":
            b = Board.objects.filter(content__contains=kw)
    else :   
        b = Board.objects.all()

    b = b.order_by("-pubdate")   #최신글이 앞으로, 반대는 pubdate

    pag = Paginator(b, 3)
    obj = pag.get_page(page)
    context = {
        "bset" : obj,
        "cate" : cate,
        "kw" : kw,
    }
    
    
    return render(request, "board/index.html", context)

def create(request):
    if request.method =="POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        Board(subject=s, content=c, writer=request.user).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def delete(reqeust, bpk):
    b = Board.objects.get(id=bpk)
    if b.writer == reqeust.user:
            b.delete()
    else:
        pass #경고메시지
    return redirect("board:index")

def detail(request, bpk):

    if request.user.is_anonymous:
        return redirect("acc:login")

    b= Board.objects.get(id=bpk)
    context = {
        "b" : b
    }
    return render(request, "board/detail.html", context)


