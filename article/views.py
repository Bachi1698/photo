from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {

    }
    return render(request,'pages/index.html',datas)

def category(request):
    datas = {

    }
    return render(request,'pages/category.html',datas)

def blog(request):
    datas = {

    }
    return render(request,'pages/blog.html',datas)

def single(request):
    datas = {

    }
    return render(request,'pages/single-blog.html',datas)
    
