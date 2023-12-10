from django.contrib import admin

# Register your models here.
from .models import (
    Certificados,
    Comisiones,
    GruposFamiliares,
    Parentescos,
    Perfiles,
    Socios,
    TipoCertificados,
    TipoComisiones
)

admin.site.register(Certificados)
admin.site.register(Comisiones)
admin.site.register(GruposFamiliares)
admin.site.register(Parentescos)
admin.site.register(Perfiles)
admin.site.register(Socios)
admin.site.register(TipoCertificados)
admin.site.register(TipoComisiones)