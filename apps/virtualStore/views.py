from django.shortcuts import render,redirect,get_object_or_404
from controlEstoque.models import Produtos
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def lojavirtual(request):
    """ renderiza loja_virtual com os produtos cadastrados no banco de dados"""
    produtos=Produtos.objects.order_by('categoria').filter(publicada='True')

    paginator=Paginator(produtos,8)
    page=request.GET.get('page')
    produtos_por_pagina=paginator.get_page(page)  
   
    dados={
        'title':'Vitrine',
        'produtos':produtos_por_pagina,       
        'categorias':categorias(),
    }

    return render(request,'lojavirtual/lojavirtual.html',dados)

def detalhes(request,produto_id):
    detalhes=get_object_or_404(Produtos,pk=produto_id)   
   
    dados={
        'title':'Detalhes',
        'detalhes':detalhes,
        'categorias':categorias(),
        
      
    }
    return render(request,'lojavirtual/detalhes.html',dados)


def busca_produto(request):    
    lista_categorias=['Tecnologia','Bebidas','Escritório','Livraria','Casa e Cozinha']
    if request.method=='GET':

       busca_produto=request.GET['buscar']

       filtro=Produtos.objects.filter(publicada=True)
    
       filtro=filtro.filter(Q(produto__icontains=busca_produto)|Q(categoria=busca_produto))

       paginator=Paginator(filtro,4)
       page=request.GET.get('page')
       produtos_por_pagina=paginator.get_page(page)

      
    dados={
        'title':'Busca',
        'produtos':produtos_por_pagina,
        'categorias':categorias(),
        
    }
        

    return render(request,'lojavirtual/buscar.html',dados)


def busca_categoria(request,_categoria):

    filtrando_categorias=Produtos.objects.filter(publicada=True)
    filtrando_categorias=filtrando_categorias.filter(categoria__icontains=_categoria)

    dados={
        'title':'Categorias',
        'categoria_produto':filtrando_categorias,
        'categorias':categorias(),
    }
    
    return render(request,'lojavirtual/categorias.html',dados)

def categorias():
    """ retorna todas as categorias existentes no banco sem repetí-las"""
    categorias=Produtos.objects.values('categoria').distinct('categoria').order_by('categoria')     
        
    return categorias
        



