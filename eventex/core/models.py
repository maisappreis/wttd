from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
    

class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    # Explicitamente instâncias o manager padrão do Django.
    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value
    
# A classe Activity é uma Classe Abstrata, é a base para os modelos de TALK e COURSE.
# Quando 2 classes possuem muitas coisas em comum, é conveniente usar essa Herança de Classe.
# Assim ela recebe esse 'abstract = True'.
# Modelos Abstratos não possuem tabela no banco.
# Classes Abstratas são para modelos sem conecxão um com outro, mas que possuem similiridade

# class Activity(models.Model):
#     title = models.CharField('título', max_length=200)
#     start = models.TimeField('início', blank=True, null=True)
#     description = models.TextField('descrição', blank=True)
#     speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

#     objects = PeriodManager()

#     class Meta:
#         abstract = True
#         verbose_name = 'palestra'
#         verbose_name_plural = 'palestras'

#     def __str__(self):
#         return self.title

# class Talk(Activity):
#   pass

class Talk(models.Model): # Modelo Concreto.
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()

    class Meta:
        ordering = ['start']
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title

# Mas existe a Multi Table Inheritance, em que há relação entre tabelas.
# Uma fica sendo a extensão da outra.
# Assim, todo Course seria um Talk.

# Como alterar o Modelo sem fazer com que tudo do banco de dados, já cadastrados em produção seja excluído.
# 1 - Renomear Course para CourseOld.
# 2 - Fazer o Course herdar de Talk, e não se Activity.
# 3 - Arrumar os testes do modelo.
# 4 - Migrar os dados de CourseOld para o nosso novo Course.
# Comando: `manage makemigrations --empty -n course_abc_to_mti core` (Abstract to Multi Table Inheritance)
# 5 - Editar o arquivo gerado pela migração
# 6 - Roda as migrações


# class CourseOld(Activity):
#     slots = models.IntegerField() # Course possui esse campo extra.

#     class Meta:
#         verbose_name = 'curso'
#         verbose_name_plural = 'cursos'


class Course(Talk):
    slots = models.IntegerField() # Course possui esse campo extra.

    objects = PeriodManager()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'


