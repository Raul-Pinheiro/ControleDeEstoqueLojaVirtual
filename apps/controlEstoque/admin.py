from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Produtos

class Listando_Produtos(admin.ModelAdmin):
    list_display=('id','produto','categoria','publicada')
    list_display_links=('id','produto','categoria')
    list_editable=('publicada',)



admin.site.register(Produtos,Listando_Produtos)
