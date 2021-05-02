from django.contrib import admin
from empregado.models import *

class assalariadoAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','metodo_de_pagamento','salario')
    search_fields = ['nome']
    #fields = ['nome','endereco',('tipo','metodo_de_pagamento'),'sindicato',('salario','dia_do_pagamento')]

class horistaAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','metodo_de_pagamento','salario','valor_hora')
    search_fields = ['nome']

class comissionadoAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','metodo_de_pagamento','salario')
    search_fields = ['nome']

# Register your models here.
admin.site.register(Assalariado, assalariadoAdmin)
admin.site.register(Horista, horistaAdmin)
admin.site.register(Comissionado, comissionadoAdmin)
admin.site.register(Sindicato)
admin.site.register(Cartao_de_ponto)
admin.site.register(Venda)

