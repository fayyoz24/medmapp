from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shifokor, ShifokorTranslation


class ShifokorTranslationInline(admin.TabularInline):
    model = ShifokorTranslation
    extra = 1


@admin.register(Shifokor)
class ShifokorAdmin(admin.ModelAdmin):
    list_display = ["id", "get_name", "rating", "shifoxona"]
    inlines = [ShifokorTranslationInline]

    def get_name(self, obj):
        first_translation = obj.translations.first()
        return first_translation.ism_familiya if first_translation else "—"
    get_name.short_description = "Ism Familiya"


# @admin.register(ShifokorTranslation)
# class ShifokorTranslationAdmin(admin.ModelAdmin):
#     list_display = ["ism_familiya", "language", "parent"]
#     list_filter = ["language"]
#     search_fields = ["ism_familiya", "mutaxassislik"]
