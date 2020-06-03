from django.shortcuts import render
from . import models
from about import models as siteinfo_models

# Create your views here.
def index(request):
    gallerie = models.Gallerie.objects.filter(status=True)
    photo_recent = models.Photo.objects.all().order_by('-date_add')[:4]
    photo_recents = models.Photo.objects.all().order_by('-date_add')[:3]
    site_info = siteinfo_models.SiteInfo.objects.filter(status=True)[:1].get()
    datas = {
        'gallerie':gallerie,
        'photo_recent':photo_recent,
        'photo_recents':photo_recents,
        'site_info':site_info,

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
    
