from django.contrib import admin
from empregado.models import *

class assalariadoAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','metodo_de_pagamento','salario')
    search_fields = ['nome']
    fields = ['nome','endereco',('tipo','metodo_de_pagamento'),'sindicato',('salario','dia_do_pagamento')]



# Register your models here.
admin.site.register(Assalariado, assalariadoAdmin)
admin.site.register(Horista)
admin.site.register(Comissionado)
admin.site.register(Sindicato)
admin.site.register(Cartao_de_ponto)
admin.site.register(Venda)

