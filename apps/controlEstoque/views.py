from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from controlEstoque.models import Produtos

# Create your views here.
     
def dashboard(request):
    if request.user.is_authenticated:
     
        usuario=request.user.username
        
        dados={
            'title':'Dashboard',
            'produtos':produtos,
            'usuario':usuario
        }       
        return render(request,'estoque/dashboard.html',dados)
    else:
        
        return redirect('login')

def produtos(request):
    if request.user.is_authenticated:   
        id=request.user.id      
        usuario=request.user.username
         
        produtos=Produtos.objects.filter(vendedor_auth=id)
        dados={
            'title':'Display Produtos', 
            'usuario':usuario,
            'produtos':produtos
                
        }
        return render(request,'estoque/produtos.html',dados)
    else:
        return redirect('login')


def formulario_produtos(request):
    if request.user.is_authenticated:
          
        usuario=request.user.username
        dados={
            'title':'Formulário de produtos', 
            'usuario':usuario,
                
        }
        return render(request,'estoque/formulario_produtos.html',dados)
    else:
        return redirect('login')

def produto_banco(request):
    if request.method=='POST':
        vendedor_auth=get_object_or_404(User,pk=request.user.id)    
        produto=request.POST['produto']
        medida=	request.POST['medida']
        categoria=request.POST['categoria']
        descricao= request.POST['descricao']		
        quantidade_por_embalagem=request.POST['quantidade_por_embalagem']
        foto_produto=request.FILES['foto_produto']
        valor_venda=request.POST['valor_venda']
        publicada=request.POST['publicada']
        
        cadastro=Produtos.objects.create(vendedor_auth=vendedor_auth,produto=produto,\
            medida=medida,categoria=categoria,descricao=descricao,quantidade_por_embalagem=quantidade_por_embalagem,\
                foto_produto=foto_produto,valor_venda=valor_venda,publicada=publicada)
        cadastro.save()
        return redirect('produtos')
    else:
        return redirect('dashboard')


def deleta_produto(request,produto_id):
    if request.user.is_authenticated:

        produto_id=get_object_or_404(Produtos,pk=produto_id)
        produto_id.delete()                   
           
        return redirect('dashboard')
    else:
        
        return redirect('login')


def edita_produto(request,produto_id):
    if request.user.is_authenticated:
        produto=get_object_or_404(Produtos,pk=produto_id)
        dados={
            'title':'Editando produtos',
            'produto':produto,
        }
        return render(request,'estoque/edita_produto.html',dados)
    else:
        
        return redirect('login')


def atualiza_produto(request):
    if request.method=='POST':

        produto_id=request.POST['produto_id']

        atualiza_produto=Produtos.objects.get(pk=produto_id)

        atualiza_produto.produto=request.POST['produto']
        atualiza_produto.medida=request.POST['medida']
        atualiza_produto.categoria=request.POST['categoria']
        atualiza_produto.descricao=request.POST['descricao']
        atualiza_produto.valor_venda=request.POST['valor_venda']
        atualiza_produto.quantidade_por_embalagem=request.POST['quantidade_por_embalagem']
        
        if 'foto_produto' not in request.FILES:
            pass
        else:        
            atualiza_produto.foto_produto=request.FILES['foto_produto']
      
       
        atualiza_produto.publicada=request.POST['publicada']
        
        atualiza_produto.save()
        
        return redirect('produtos')
