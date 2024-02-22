from django.db import models

class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    tit = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='media', blank=True, null=True)

    
    
class Comentario(models.Model):
    id = models.AutoField(primary_key=True)   
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.CharField(max_length=200)
    