from django.contrib import admin
from .models import (Hudud, 
                HududTranslation,
                Konsultatsiya, 
                AsosiyYonalish,
                AsosiyYonalishTranslation,
                YonalishAmaliyoti,
                YonalishAmaliyotiTranslation,
                Natijalar,
                NatijalarTranslation,
                BizningXizmatlarEhtiyojQoplaydi,
                BizningXizmatlarEhtiyojQoplaydiTranslation,
                DavolashUsuliTanlang,
                DavolashUsuliTanlangTranslation
                )


class HududTranslationInline(admin.TabularInline):
    model = HududTranslation
    extra = 1

@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    inlines = [HududTranslationInline]
    list_display = ["id", "__str__"]

# class DavolashUsuliTranslationInline(admin.TabularInline):
#     model = DavolashUsuliTranslation
#     extra = 1

# @admin.register(DavolashUsuli)
# class DavolashUsuliAdmin(admin.ModelAdmin):
#     inlines = [DavolashUsuliTranslationInline]
#     list_display = ["id", "__str__"]

@admin.register(Konsultatsiya)
class KonsultatsiyaAdmin(admin.ModelAdmin):
    list_display = ["id", "tel_raqam", "hudud", "is_checked"]
    list_filter = ["is_checked", "hudud"]
    search_fields = ["tel_raqam"]
    list_editable = ["is_checked"]
    

# ---------- KO‘P TARMOQ TIBBIY YORDAM ----------
class AsosiyYonalishTranslationInline(admin.TabularInline):
    model = AsosiyYonalishTranslation
    extra = 1


@admin.register(AsosiyYonalish)
class AsosiyYonalishAdmin(admin.ModelAdmin):
    inlines = [AsosiyYonalishTranslationInline]
    list_display = ["id", "__str__"]
    search_fields = ["translations__title"]


# ---------- INLINE TARJIMALAR ----------
class YonalishAmaliyotiTranslationTranslationInline(admin.TabularInline):
    model = YonalishAmaliyotiTranslation
    extra = 1


@admin.register(YonalishAmaliyoti)
class YonalishAmaliyotiAdmin(admin.ModelAdmin):
    list_display = ["id", "narx"]
    inlines = [YonalishAmaliyotiTranslationTranslationInline]


class NatijalarTranslationInline(admin.TabularInline):
    model = NatijalarTranslation
    extra = 1


@admin.register(Natijalar)
class NatijalarAdmin(admin.ModelAdmin):
    list_display = ["id", "statistik_raqam"]
    inlines = [NatijalarTranslationInline]


# ===================== Bizning xizmatlar =====================
class BizningXizmatlarEhtiyojQoplaydiTranslationInline(admin.TabularInline):
    model = BizningXizmatlarEhtiyojQoplaydiTranslation
    extra = 1


@admin.register(BizningXizmatlarEhtiyojQoplaydi)
class BizningXizmatlarEhtiyojQoplaydiAdmin(admin.ModelAdmin):
    list_display = ["id"]
    inlines = [BizningXizmatlarEhtiyojQoplaydiTranslationInline]
