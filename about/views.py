from django.shortcuts import render

# Create your views here.

def archive(request):
    datas = {

    }
    return render(request,'pages/archive.html',datas)