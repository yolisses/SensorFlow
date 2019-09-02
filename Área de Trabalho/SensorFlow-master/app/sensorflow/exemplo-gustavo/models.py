from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Producer(models.Model):

    name = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produtora'
        verbose_name_plural = 'Produtoras'


class Actor(models.Model):

    SEXO = (
        (1,'Masculino'),
        (2,'Feminino')
    )

    name = models.CharField(max_length=100, verbose_name='Nome')
    date_of_birth = models.DateTimeField('Data de Nascimento', auto_now=True)
    nationality = models.CharField(max_length=30, verbose_name='Nacionalidade')
    photo = models.ImageField(verbose_name='Foto', upload_to='accounts/%Y/%m/%d', default='default/44939342_1004064873112118_861463258668728320_n.jpg')
    oscar = models.IntegerField(verbose_name="Quantidade de Oscar")
    genre = models.IntegerField(choices = SEXO, verbose_name = 'Gênero')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

class Director(models.Model):

    SEXO = (
        (1,'Masculino'),
        (2,'Feminino')
    )

    name = models.CharField(max_length=100, verbose_name='Nome')
    nationality = models.CharField(max_length=30, verbose_name='Nacionalidade')
    photo = models.ImageField(verbose_name='Foto', upload_to='accounts/%Y/%m/%d', default='default/44939342_1004064873112118_861463258668728320_n.jpg')
    oscar = models.IntegerField(verbose_name="Quantidade de Oscar")
    genre = models.IntegerField(choices = SEXO, verbose_name='Gênero')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'

class Movie(models.Model):
    
    CLASSIFICACAO = (
        (1,'Livre'),
        (2,'10 anos'),
        (3,'12 anos'),
        (4,'14 anos'),
        (5,'16 anos'),
        (6,'18 anos')
    )

    name = models.CharField(max_length=100, verbose_name='Nome do Filme')
    synopsis = models.TextField(max_length=300, verbose_name="Sinopse do Filme")
    duration = models.IntegerField(verbose_name="Duração do Filme")
    classification = models.IntegerField(choices = CLASSIFICACAO, verbose_name='Classificação Indicativa')
    oscar = models.IntegerField(verbose_name="Quantidade de Oscar")
    year = models.IntegerField(verbose_name="Ano de Lançamento")
    nationality = models.CharField(max_length=30, verbose_name='Nacionalidade')
    box_office = models.IntegerField(verbose_name="Bilheteria do Filme")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Produtora', related_name='movies')
    categories = models.ManyToManyField(Category, verbose_name='Gêneros', related_name='movies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

class Evaluation(models.Model):

    rating = models.IntegerField(verbose_name='Nota do Filme')
    comment = models.TextField(max_length=200, verbose_name="Comentário")
    date = models.DateTimeField(auto_now = True, verbose_name="Data da Publicação")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Filme', related_name='evaluetions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuário', related_name='evaluetions')

    def __str__(self):
        return f'{self.user.first_name} - {self.movie.name} - {self.comment}'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

class Cast(models.Model):

    name = models.CharField(max_length = 100, verbose_name='Nome do Personagem')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Filme', related_name='filme')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ator', related_name='ator')

    def __str__(self):
        return '%s (%s)' % (self.name, self.actor.name)

    class Meta:
        verbose_name = 'Elenco'
        verbose_name_plural = 'Elencos'