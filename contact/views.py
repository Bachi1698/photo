from django.shortcuts import render

# Create your views here.

def contact(request):
    datas = {

    }
    return render(request,'pages/contact.html',datas)
