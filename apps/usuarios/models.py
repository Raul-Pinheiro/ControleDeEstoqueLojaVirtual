from django.db import models

# Create your models here.

#cadastro_senha_confirm models.TextField()
class CriaAdm(models.Model):

    cadastro_empresa = models.TextField()
    cadastro_cnpj = models.TextField()
    cadastro_plano = models.TextField()
    cadastro_codigo_autenticacao = models.TextField()
    cadastro_user_admin = models.TextField()   
    cadastro_email_admin = models.TextField()
    

    def __str__(self):
        return self.cadastro_empresa

class CriaFuncionario(models.Model):

    administrador = models.ForeignKey(CriaAdm,on_delete=models.CASCADE)
    funcionario = models.TextField()
    email=models.TextField()
    pw=models.TextField()
    
    def __str__(self):
        return self.funcionario