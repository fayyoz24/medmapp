from django.contrib import admin
from .models import (Hudud, 
                HududTranslation,
                DavolashUsuli, 
                DavolashUsuliTranslation,
                Konsultatsiya, 
                KopTarmoqliTibbiyYordam,
                MashhurShifokorlar,
                OmmabopShifoxonalar,
                KafolatlanganArzonNarxlar,
                Natijalar,
                DavolashUsuliTanlang,
                BizningXizmatlarEhtiyojQoplaydi,

                )


class HududTranslationInline(admin.TabularInline):
    model = HududTranslation
    extra = 1

@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    inlines = [HududTranslationInline]
    list_display = ["id", "__str__"]

class DavolashUsuliTranslationInline(admin.TabularInline):
    model = DavolashUsuliTranslation
    extra = 1

@admin.register(DavolashUsuli)
class DavolashUsuliAdmin(admin.ModelAdmin):
    inlines = [DavolashUsuliTranslationInline]
    list_display = ["id", "__str__"]

@admin.register(Konsultatsiya)
class KonsultatsiyaAdmin(admin.ModelAdmin):
    list_display = ["id", "tel_raqam", "hudud", "davolash_usuli", "is_checked"]
    list_filter = ["is_checked", "hudud", "davolash_usuli"]
    search_fields = ["tel_raqam"]
    list_editable = ["is_checked"]
    
from django.contrib import admin
from .models import (
    KopTarmoqliTibbiyYordam,
    KopTarmoqliTibbiyYordamTranslation,
    OmmabopShifoxonalar,
    OmmabopShifoxonalarTranslation,
)


# ---------- KO‘P TARMOQ TIBBIY YORDAM ----------
class KopTarmoqliTibbiyYordamTranslationInline(admin.TabularInline):
    model = KopTarmoqliTibbiyYordamTranslation
    extra = 1


@admin.register(KopTarmoqliTibbiyYordam)
class KopTarmoqliTibbiyYordamAdmin(admin.ModelAdmin):
    inlines = [KopTarmoqliTibbiyYordamTranslationInline]
    list_display = ["id", "__str__"]
    search_fields = ["translations__title"]


# ---------- OMMABOP SHIFOXONALAR ----------
class OmmabopShifoxonalarTranslationInline(admin.TabularInline):
    model = OmmabopShifoxonalarTranslation
    extra = 1


@admin.register(OmmabopShifoxonalar)
class OmmabopShifoxonalarAdmin(admin.ModelAdmin):
    inlines = [OmmabopShifoxonalarTranslationInline]
    list_display = ["id", "__str__"]
    search_fields = ["translations__title"]


from django.contrib import admin
from .models import (
    KafolatlanganArzonNarxlar, 
    KafolatlanganArzonNarxlarTranslation,
    Natijalar,
    NatijalarTranslation
)

# ---------- INLINE TARJIMALAR ----------
class KafolatlanganArzonNarxlarTranslationInline(admin.TabularInline):
    model = KafolatlanganArzonNarxlarTranslation
    extra = 1


@admin.register(KafolatlanganArzonNarxlar)
class KafolatlanganArzonNarxlarAdmin(admin.ModelAdmin):
    list_display = ["id", "narx"]
    inlines = [KafolatlanganArzonNarxlarTranslationInline]


class NatijalarTranslationInline(admin.TabularInline):
    model = NatijalarTranslation
    extra = 1


@admin.register(Natijalar)
class NatijalarAdmin(admin.ModelAdmin):
    list_display = ["id", "statistik_raqam"]
    inlines = [NatijalarTranslationInline]

from django.contrib import admin
from .models import (
    BizningXizmatlarEhtiyojQoplaydi,
    BizningXizmatlarEhtiyojQoplaydiTranslation,
    MashhurShifokorlar,
    MashhurShifokorlarTranslation
)

# ===================== Bizning xizmatlar =====================
class BizningXizmatlarEhtiyojQoplaydiTranslationInline(admin.TabularInline):
    model = BizningXizmatlarEhtiyojQoplaydiTranslation
    extra = 1


@admin.register(BizningXizmatlarEhtiyojQoplaydi)
class BizningXizmatlarEhtiyojQoplaydiAdmin(admin.ModelAdmin):
    list_display = ["id"]
    inlines = [BizningXizmatlarEhtiyojQoplaydiTranslationInline]


# ===================== Mashhur shifokorlar =====================
class MashhurShifokorlarTranslationInline(admin.TabularInline):
    model = MashhurShifokorlarTranslation
    extra = 1


@admin.register(MashhurShifokorlar)
class MashhurShifokorlarAdmin(admin.ModelAdmin):
    list_display = ["id", "rating", "tajriba_yil", "jarrohlik_amaliyotlar_soni"]
    inlines = [MashhurShifokorlarTranslationInline]


admin.site.register(DavolashUsuliTanlang)
