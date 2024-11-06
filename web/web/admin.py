
from django.contrib import admin
from .models import planestudios, cursos, bancopreguntas, bancorespuestas, bancoresultados



class cursosAdmin(admin.ModelAdmin):
    admin.site.register(planestudios)
    admin.site.register(cursos)


class diagosnosticosAdmin(admin.ModelAdmin):
    admin.site.register(bancopreguntas)
    admin.site.register(bancorespuestas)
    admin.site.register(bancoresultados)

