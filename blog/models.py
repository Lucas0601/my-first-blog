# Importações necessárias do Django
from django.conf import settings
from django.db import models
from django.utils import timezone

# Definição do modelo Post
class Post(models.Model):
    # ForeignKey para o autor da postagem (relacionado ao modelo de usuário definido em settings)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Título da postagem, com um limite de 200 caracteres
    title = models.CharField(max_length=200)
    
    # Texto da postagem, campo de texto longo
    text = models.TextField()
    
    # Data de criação da postagem, com um valor padrão definido como a hora atual
    create_date = models.DateTimeField(default=timezone.now)
    
    # Data de publicação da postagem, inicialmente em branco (ainda não publicada)
    published_date = models.DateTimeField(blank=True, null=True)

    # Método para publicar a postagem, definindo a data de publicação como a hora atual
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Representação textual do objeto Post, retornando o título da postagem
    def __str__(self):
        return self.title
