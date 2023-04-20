from django.db import models


# Vai sobreescrever o método get_queryset 
# que é o método raiz de todo manager
class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)
    
    def phones(self):
        return self.filter(kind=self.model.PHONE)


class KindContactManager(models.Manager):
    def get_queryset(self):
        return KindQuerySet(self.model, using=self._db)
    
    def emails(self):
        return self.get_queryset().emails()
    
    def phones(self):
        return self.get_queryset().phones()
    

# class PeriodManager(models.Manager):
#     MIDDAY = '12:00'

#     def at_morning(self):
#         return self.filter(start__lt=self.MIDDAY) # lt = less than
    
#     def at_afternoon(self):
#         return self.filter(start__gte=self.MIDDAY) # gte = greater than or equal
    

class PeriodQuerySet(models.QuerySet):
    MIDDAY = '12:00'

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY) # lt = less than
    
    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY) # gte = greater than or equal
    

PeriodManager = models.Manager.from_queryset(PeriodQuerySet) # Cria uma Classe Manager.
