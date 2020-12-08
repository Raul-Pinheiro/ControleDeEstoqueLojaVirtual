from django.urls import path 
from . import views



urlpatterns=[
    path('produtos',views.lojavirtual,name='lojavirtual'),
    path('detalhes/<int:produto_id>',views.detalhes,name='detalhes'),
    path('busca-produto', views.busca_produto,name='busca_produto'),
    path('categoria/<slug:_categoria>',views.busca_categoria,name='busca_categoria'),
]