from django.db import models

# Create your models here.
class Empregado(models.Model):
    class Meta:
        abstract = True

    TIPO = [
        ('ASSALARIADO','Assalariado'),
        ('HORISTA','Horista'),
        ('COMISSIONADO','Comissionado')
    ]

    METODO = [
        ('MAOS','Cheque-Maos'),
        ('CORREIO','Cheque-Correio'),
        ('DEPOSITO','Deposito')
    ]

    nome = models.CharField(max_length = 40)
    endereco = models.CharField(max_length = 100)
    tipo = models.CharField(max_length=12,choices=TIPO,default='Assalariado')
    metodo_de_pagamento = models.CharField(max_length=8,choices=METODO,default='Cheque-Maos')
    sindicato = models.OneToOneField('Sindicato',on_delete=models.SET_NULL,null=True, blank=True)
    salario = models.FloatField()

    def __str__(self):
        return self.nome + " " + self.tipo + " " + self.endereco


class Assalariado(Empregado):
    dia_do_pagamento = models.DateField()

    class Meta:
        db_table = 'assalariado'
        verbose_name_plural = 'assalariados'


class Horista(Empregado):
    valor_hora = models.FloatField()
    cartao_de_ponto = models.OneToOneField('Cartao_de_ponto',on_delete=models.SET_NULL,null=True, blank=True)

    class Meta:
        db_table = 'horista'
        verbose_name_plural = 'horistas'


class Comissionado(Empregado):
    venda = models.ForeignKey('Venda',on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'comissionado'
        verbose_name_plural = 'comissionados'

        
class Sindicato(models.Model):
    nome_sindicato = models.CharField(max_length=20,default='Sindicato Basico')
    taxa = models.FloatField()
    valor_sindicato = models.FloatField()

    class Meta:
        db_table = 'sindicato'
        verbose_name_plural = 'sindicatos'
    
    def __str__(self):
        return self.nome_sindicato


class Cartao_de_ponto(models.Model):
    horas_trabalhadas = models.FloatField()
    dia = models.DateField()
    class Meta:
        db_table = 'cartao'
        verbose_name_plural = 'cartoes'
    def __str__(self):
        return "Cartão de ponto"



class Venda(models.Model):
    data_venda = models.DateField()
    valor = models.FloatField()
    percentual_na_venda = models.FloatField()
    def __str__(self):
        return "Venda"



