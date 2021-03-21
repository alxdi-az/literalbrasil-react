from django.db import models
from django.conf import settings
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from unidecode import unidecode


def post_capa_directory_path(instance, filename):
    titulo = unidecode(instance.titulo.replace(' ', '_').lower())
    return f'imagens/{titulo}/capa/{filename}'


def post_directory_path(instance, filename):
    post = unidecode(instance.post.titulo.replace(' ', '_').lower())
    return f'imagens/{post}/{filename}'


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.descricao


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=500)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    capa = models.ImageField(upload_to=post_capa_directory_path, null=True)

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    titulo = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to=post_directory_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo
