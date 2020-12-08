from django.urls import path
from . import views


urlpatterns=[    
    path('dashboard',views.dashboard,name='dashboard'),
    path('display_produtos',views.produtos,name='produtos'),    
    path('formulario/produtos',views.formulario_produtos,name="formulario_produtos"),
    path('cadastra_produto',views.produto_banco,name='produto_banco'),
    path('edita_produto/<int:produto_id>',views.edita_produto,name="edita_produto"),
    path('deleta_produto/<int:produto_id>',views.deleta_produto,name='deleta_produto'),
    path('atualizando_produto>',views.atualiza_produto,name='atualiza_produto'), 

]