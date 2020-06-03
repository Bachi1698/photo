from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAddmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    list_filter = ('status',)
    list_per_page = 6
    date_hierachy = "date_add"

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class Categorie(CustomAddmin):
    list_display = ('nom','date_add','date_update','status','image_view')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info categorie",{"fields":["nom","description","image",]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class Video(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','video_view')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info categorie",{"fields":["titre","description","video",]}),
                  ("standard",{"fields":["status"]})
    ]
    def video_view(self,obj):
        return mark_safe("<iframe width='100' height='50' src='{url}'></iframe>".format(url=obj.video.url))

class Gallerie(CustomAddmin):
    list_display = ('date_add','date_update','status','image_view')   
    search_fields = ('date_add',)    
    ordering = ['date_add']    
    fieldsets = [
                  ("info categorie",{"fields":["image",]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class Video(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','video_view')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info categorie",{"fields":["titre","description","video",]}),
                  ("standard",{"fields":["status"]})
    ]
    def video_view(self,obj):
        return mark_safe("<iframe width='100' height='50' src='{url}'></iframe>".format(url=obj.video.url))

