from django.shortcuts import render
import googletrans


# Create your views here.

def index(request):

    b =request.GET.get("bf", "")
 
    context = {
        "ndict" : googletrans.LANGUAGES,
        "fr" : "en",
        "to" : "ko"
    }
 

    if b :
        f = request.GET.get("fr","")
        t = request.GET.get("to", "")
        tr = googletrans.Translator()
        result = tr.translate(b, src=f, dest=t)
        context.update({
            "af" : result.text,
            "bf" : b,
            "fr" : f,
            "to" : t
        })

    return render(request, "trans/index.html", context)