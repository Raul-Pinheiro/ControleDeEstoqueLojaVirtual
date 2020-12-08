from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Produtos(models.Model):  

    vendedor_auth=models.ForeignKey(User,on_delete=models.CASCADE)    
    produto=models.CharField(max_length=200)
    medida=models.CharField(max_length=200)	
    categoria=models.CharField(max_length=200)	
    descricao=models.TextField(max_length=200)  		
    quantidade_por_embalagem=models.IntegerField()  
    foto_produto=models.ImageField(upload_to='img/%d/%m/%Y/',blank= True) 
    valor_venda=models.CharField(max_length=200)  
    publicada=models.BooleanField(default=False)
    

    def __str__(self):
        return self.produto