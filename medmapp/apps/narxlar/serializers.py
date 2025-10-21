from rest_framework import serializers
from bosh_sahifa.models import YonalishAmaliyoti
from shifoxonalar.models import Shifoxona


class TranslationMixin:
    """Reusable mixin for language-based translation resolution."""
    def get_language(self):
        request = self.context.get("request")
        return request.headers.get("Accept-Language", "uz") if request else "uz"

    def get_translation(self, obj):
        lang = self.get_language()
        translation = next((t for t in obj.translations.all() if t.language == lang), None)
        if not translation and obj.translations.exists():
            translation = obj.translations.first()
        return translation


class ShifoxonaSerializer(TranslationMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    asosiy_yonalish = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Shifoxona
        fields = ["id", "logo", "shahar", "asosiy_yonalish", "title", "text"]

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None


class YonalishAmaliyotiSerializer(TranslationMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = YonalishAmaliyoti
        fields = ["id", "asosiy_yonalish", "image", "title", "text"]

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None
