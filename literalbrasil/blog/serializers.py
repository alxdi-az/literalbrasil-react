from django.db import models
from rest_framework import serializers
from .models import Post
from .models import Categoria
from .models import Imagem


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk', 'descricao')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'autor', 'categoria', 'titulo', 'resumo',
                  'texto', 'data_criacao', 'data_publicacao', 'capa')


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ('pk', 'titulo', 'imagem', 'post')
