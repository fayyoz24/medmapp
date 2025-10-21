from django.contrib import admin
from .models import (
    Davlat, DavlatTranslation,
    Shahar, ShaharTranslation,
    Shifoxona, ShifoxonaTranslation
)


# ---- Inline Tarjima Classlar ----
class DavlatTranslationInline(admin.TabularInline):
    model = DavlatTranslation
    extra = 1


class ShaharTranslationInline(admin.TabularInline):
    model = ShaharTranslation
    extra = 1


class ShifoxonaTranslationInline(admin.TabularInline):
    model = ShifoxonaTranslation
    extra = 1


# ---- Asosiy Adminlar ----
@admin.register(Davlat)
class DavlatAdmin(admin.ModelAdmin):
    list_display = ["id", "get_nomi"]
    inlines = [DavlatTranslationInline]

    def get_nomi(self, obj):
        t = obj.translations.first()
        return t.nomi if t else "—"
    get_nomi.short_description = "Davlat nomi"


@admin.register(Shahar)
class ShaharAdmin(admin.ModelAdmin):
    list_display = ["id", "get_nomi", "davlat"]
    list_filter = ["davlat"]
    inlines = [ShaharTranslationInline]

    def get_nomi(self, obj):
        t = obj.translations.first()
        return t.nomi if t else "—"
    get_nomi.short_description = "Shahar nomi"


@admin.register(Shifoxona)
class ShifoxonaAdmin(admin.ModelAdmin):
    list_display = ["id", "get_title", "shahar"]
    list_filter = ["shahar"]
    search_fields = ["translations__title"]
    inlines = [ShifoxonaTranslationInline]

    def get_title(self, obj):
        t = obj.translations.first()
        return t.title if t else "—"
    get_title.short_description = "Shifoxona nomi"


# # ---- Translation Admins ----
# @admin.register(DavlatTranslation)
# class DavlatTranslationAdmin(admin.ModelAdmin):
#     list_display = ["nomi", "language", "davlat"]
#     list_filter = ["language"]
#     search_fields = ["nomi"]


# @admin.register(ShaharTranslation)
# class ShaharTranslationAdmin(admin.ModelAdmin):
#     list_display = ["nomi", "language", "shahar"]
#     list_filter = ["language"]
#     search_fields = ["nomi"]


# @admin.register(ShifoxonaTranslation)
# class ShifoxonaTranslationAdmin(admin.ModelAdmin):
#     list_display = ["title", "language", "shifoxona"]
#     list_filter = ["language"]
#     search_fields = ["title"]
