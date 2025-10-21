
# Register your models here.
from django.contrib import admin
from .models import MamnunBemor, BemorFikri


@admin.register(MamnunBemor)
class MamnunBemorAdmin(admin.ModelAdmin):
    list_display = ("id", "mamnun", "ijobiy_foiz", "mamlakat_bemorlari")
    ordering = ("-id",)


@admin.register(BemorFikri)
class BemorFikriAdmin(admin.ModelAdmin):
    list_display = ("id", "bemor", "shifoxona", "amaliyot", "baho", "yaratilgan_sana")
    list_filter = ("baho", "yaratilgan_sana")
    search_fields = ("bemor__username", "sharh_matni")
    ordering = ("-yaratilgan_sana",)
