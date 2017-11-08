from __future__ import unicode_literals
from django.db import models



#Create your models here.
class Book(models.Model):
    novel = 'nov'
    document = 'doc'
    other = 'oth'
    type = (
        (novel,'one of novel'),
        (document,'documentation'),
        (other,'other')

    )
    title = models.CharField(max_length=25,verbose_name='Title')
    author = models.CharField(max_length=25,verbose_name='Author')
    publish_at=models.DateField()
    number_of_page=models.IntegerField()
    type_of_book =models.CharField(max_length=25,choices=type,default=novel)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.title