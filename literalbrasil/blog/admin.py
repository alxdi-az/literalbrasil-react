from django.contrib import admin
from .models import Post
from .models import Categoria
from .models import Imagem

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Imagem)
