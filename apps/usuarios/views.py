from django.shortcuts import render,redirect,get_object_or_404
from .models import CriaAdm ,CriaFuncionario
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Renderiza a página inicial
def index(request):
    dados={
        'title': 'Home'
    }
    return render(request,'index.html',dados)


#Renderiza Página de cadastro
def cadastro(request):
    dados={
        'title': 'Cadastro',
    }
    return render(request,'cadastro.html',dados)


#Renderiza página de login
def login(request): 
     
    dados={
        'title':'Login',        
    }
    return render(request,'login.html',dados)

    
def dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm):
    dados={
        'title': 'Cadastro',
        'value_cadastro_empresa':cadastro_empresa,
        'value_cadastro_cnpj':cadastro_cnpj,
        'value_cadastro_plano':cadastro_plano,
        'value_cadastro_codigo_autenticacao':cadastro_codigo_autenticacao,
        'value_cadastro_user_admin':cadastro_user_admin,
        'value_cadastro_email_admin':cadastro_email_admin,
        'value_cadastro_senha_admin':cadastro_senha_admin,
        'value_cadastro_senha_confirm':cadastro_senha_confirm

    }
    return render(request,'cadastro.html',dados)

#Grava dados do cadastro num banco de dados
def cadastro_db(request):
    if request.method=='POST':

        cadastro_empresa = request.POST['cadastro_empresa']
        cadastro_cnpj = request.POST['cadastro_cnpj']
        cadastro_plano = request.POST['cadastro_plano']
        cadastro_codigo_autenticacao = request.POST['cadastro_codigo_autenticacao']
        cadastro_user_admin = request.POST['cadastro_user_admin']     
        cadastro_email_admin = request.POST['cadastro_email_admin']
        cadastro_senha_admin = request.POST['cadastro_senha_admin']
        cadastro_senha_confirm = request.POST['cadastro_senha_confirm']

        email_CriaAdm=CriaAdm.objects.filter(cadastro_email_admin=cadastro_email_admin).exists()
        cnpj_CriaAdm=CriaAdm.objects.filter(cadastro_cnpj=cadastro_cnpj).exists()
        auth_CriaAdm=CriaAdm.objects.filter(cadastro_codigo_autenticacao=cadastro_codigo_autenticacao).exists()
        user_CriaAdm=CriaAdm.objects.filter(cadastro_user_admin=cadastro_user_admin).exists()  
        username=User.objects.filter(username=cadastro_user_admin).exists()
        user_email= User.objects.filter(email=cadastro_email_admin).exists()   
        


        if cadastro_empresa=='':
            messages.error(request,'Nome da empresa em branco')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)

        if cadastro_cnpj=='' or cnpj_CriaAdm:
            messages.error(request,'CNPJ em branco ou já cadastrado')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)

        if auth_CriaAdm or cadastro_codigo_autenticacao=='':
            messages.error(request,'Código de atenticação já usado ou em branco')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)

        if user_CriaAdm or cadastro_user_admin=='' or username:
            messages.error(request,'Esse usuário já existe')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)

        if cadastro_senha_admin != cadastro_senha_confirm or cadastro_senha_admin=='' or cadastro_senha_confirm=='':
            messages.error(request,'Senhas não são iguais')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)
        
        if email_CriaAdm or cadastro_email_admin=='' or user_email :
            messages.error(request,'Email já cadastrado ou em branco')            
            return dados(request,cadastro_empresa,cadastro_cnpj,cadastro_plano,cadastro_codigo_autenticacao,\
                    cadastro_user_admin,cadastro_email_admin,cadastro_senha_admin,cadastro_senha_confirm)
        
        else:
            
            administrador= CriaAdm.objects.create(cadastro_empresa=cadastro_empresa,cadastro_cnpj=cadastro_cnpj,cadastro_plano=cadastro_plano,\
                cadastro_codigo_autenticacao=cadastro_codigo_autenticacao,cadastro_user_admin=cadastro_user_admin,\
                cadastro_email_admin=cadastro_email_admin)
            administrador.save()

            banco=CriaAdm.objects.all()
            
            user=User.objects.create_user(username=cadastro_user_admin,email=cadastro_email_admin,password= cadastro_senha_admin)
            user.save()
            messages.success(request,'Cadastro efetuado') 
            return redirect('login')

#Autentica o login
def authLogin(request):
    
    if request.method=='POST':
       
        tipo=request.POST['login_tipo']
        email=request.POST['email_acesso']
        senha=request.POST['login_senha']       
            
       
        
        if tipo=='Administrador':
            adm_email=User.objects.filter(email=email).exists() 
            if adm_email:
                nome=User.objects.filter(email=email).values_list('username',flat=True).get()              
                              
                user= auth.authenticate(request,username=nome,password=senha)

                if user is not None:
                    auth.login(request,user) 
                    messages.success(request,'Login efetuado com sucesso')                 
                    return redirect('dashboard')
          
                else:
                    messages.error(request,'Verifique seus dados e tente novamente')                                                      
                    dados={
                        'title':'Login',
                        'value_email':email,
                        'value_senha':senha,       
                    }
                    return render(request,'login.html',dados)
        
                           
        
        if tipo=='Funcionario':
            messages.error(request,'Impossivel realizar essa ação')      
            return redirect('login')
        else:
            messages.error(request,'Verifique seus dados e tente novamente')                                                      
            dados={
                'title':'Login',
                'value_email':email,
                'value_senha':senha,       
            }
            return render(request,'login.html',dados)


#Autentica o logout
def logout(request):
    auth.logout(request)
    messages.success(request,'Logout efetuado') 
    return redirect('login')

#Paginas do footer

def localize(request):
    dados={
        'title':'Localize-se',
    }
    return render(request,'mapas.html',dados)


def suporte(request):
    return render(request,'suporte.html')