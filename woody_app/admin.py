from django.contrib import admin

# Register your models here.
from .models import Project, Gasto, Costo, Ingreso
# Register your models here.

admin.site.register(Project)
admin.site.register(Gasto)
admin.site.register(Costo)
admin.site.register(Ingreso)