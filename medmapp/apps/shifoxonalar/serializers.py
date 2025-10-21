from rest_framework import serializers
from .models import Davlat, Shahar, Shifoxona


# ------------------ BASE TRANSLATION MIXIN ------------------
class TranslationMixin:
    def get_language(self):
        request = self.context.get("request")
        if request:
            return request.headers.get("Accept-Language", "uz")
        return "uz"

    def get_translation(self, obj):
        lang = self.get_language()
        # Use already-prefetched translations to avoid DB hits
        translation = next((t for t in obj.translations.all() if t.language == lang), None)
        if not translation and obj.translations.exists():
            translation = obj.translations.first()
        return translation


# ------------------ DAVLAT ------------------
class DavlatSerializer(TranslationMixin, serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()

    class Meta:
        model = Davlat
        fields = ["id", "nomi"]

    def get_nomi(self, obj):
        tr = self.get_translation(obj)
        return tr.nomi if tr else None


# ------------------ SHAHAR ------------------
class ShaharSerializer(TranslationMixin, serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()
    davlat_id = serializers.IntegerField(source="davlat.id", read_only=True)

    class Meta:
        model = Shahar
        fields = ["id", "davlat_id", "nomi"]

    def get_nomi(self, obj):
        tr = self.get_translation(obj)
        return tr.nomi if tr else None


# ------------------ SHIFOXONA ------------------
class ShifoxonaSerializer(TranslationMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    shahar_id = serializers.IntegerField(source="shahar.id", read_only=True)
    asosiy_yonalish = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Shifoxona
        fields = ["id", "logo", "shahar_id", "asosiy_yonalish", "title", "text"]

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None
