from django.shortcuts import render
from .models import Album
# Create your views here.

def index(request):
    # if request.method == "POST":
    #     pm = request.POST.get("maker")
    #     ps = request.POST.get("subject")
    #     ppic = request.FILES.get("pic")
    #     Album(maker=pm, subject=ps, pic=ppic)

    a = Album.objects.all()
    context = {
        "aset" : a
    }    
    return render(request, 'album/index.html', context)

   