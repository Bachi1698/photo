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

class SocialCountAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info social",{"fields":["nom","lien","icone"]}),
                  ("standard",{"fields":["status"]})
    ]

class SiteInfoAdmin(CustomAddmin):
    list_display = ('email','date_add','date_update','map_url','status','logo_view')
    search_fields = ('email',)
    ordering = ['email']
    fieldsets = [
                 ("info site",{"fields":["email","map_url","logo"]}),
                 ("standard",{"fields":["status"]})
    ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))
