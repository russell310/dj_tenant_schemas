from django.contrib import admin
from .models import Client


# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
