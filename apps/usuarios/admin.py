from django.contrib import admin

# Register your models here.
from .models import CriaAdm,CriaFuncionario

class Listando_Admin(admin.ModelAdmin):
    list_display=('id','cadastro_empresa')
    list_display_links=('id','cadastro_empresa')

class Listando_Funcionarios(admin.ModelAdmin):
    list_display=('id','administrador','funcionario')
    list_display_links=('id','funcionario')



admin.site.register(CriaAdm,Listando_Admin )
admin.site.register(CriaFuncionario,Listando_Funcionarios)