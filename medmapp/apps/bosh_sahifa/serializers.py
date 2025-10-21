from rest_framework import serializers
from .models import (
    Hudud, AsosiyYonalish, YonalishAmaliyoti, Natijalar,
    BizningXizmatlarEhtiyojQoplaydi, DavolashUsuliTanlang,
    Konsultatsiya
)


# =================== HUDUD ===================
class HududSerializer(serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()

    class Meta:
        model = Hudud
        fields = ["id", "nomi"]

    def get_language(self):
        request = self.context.get("request")
        if request:
            return request.headers.get("Accept-Language", "uz")
        return "uz"

    def get_nomi(self, obj):
        lang = self.get_language()
        translation = obj.translations.filter(language=lang).first()
        return translation.nomi if translation else None


# =================== ASOSIY YO‘NALISH ===================
class AsosiyYonalishSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = AsosiyYonalish
        fields = ["id", "logo", "title", "text"]

    def get_language(self):
        request = self.context.get("request")
        if request:
            return request.headers.get("Accept-Language", "uz")
        return "uz"

    def get_translation(self, obj):
        lang = self.get_language()
        return obj.translations.filter(language=lang).first()

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None


# =================== YONALISH AMALIYOTI ===================
class YonalishAmaliyotiSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    narx = serializers.IntegerField()
    logo = serializers.ImageField()

    class Meta:
        model = YonalishAmaliyoti
        fields = ["id", "logo", "narx", "title", "text"]

    def get_language(self):
        req = self.context.get("request")
        return req.headers.get("Accept-Language", "uz") if req else "uz"

    def get_translation(self, obj):
        return obj.translations.filter(language=self.get_language()).first()

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None


# =================== NATIJALAR ===================
class NatijalarSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = Natijalar
        fields = ["id", "logo", "statistik_raqam", "text"]

    def get_language(self):
        req = self.context.get("request")
        return req.headers.get("Accept-Language", "uz") if req else "uz"

    def get_text(self, obj):
        lang = self.get_language()
        tr = obj.translations.filter(language=lang).first()
        return tr.text if tr else None


# =================== BIZNING XIZMATLAR ===================
class BizningXizmatlarSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = BizningXizmatlarEhtiyojQoplaydi
        fields = ["id", "icon", "title", "text"]

    def get_language(self):
        req = self.context.get("request")
        return req.headers.get("Accept-Language", "uz") if req else "uz"

    def get_translation(self, obj):
        return obj.translations.filter(language=self.get_language()).first()

    def get_title(self, obj):
        tr = self.get_translation(obj)
        return tr.title if tr else None

    def get_text(self, obj):
        tr = self.get_translation(obj)
        return tr.text if tr else None


# =================== DAVOLASH USULI TANLANG ===================
class DavolashUsuliTanlangSerializer(serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()
    shifoxona = serializers.StringRelatedField()
    doktor = serializers.StringRelatedField()

    class Meta:
        model = DavolashUsuliTanlang
        fields = ["id", "nomi", "rating", "davomiylik", "narx", "shifoxona", "doktor"]

    def get_language(self):
        req = self.context.get("request")
        return req.headers.get("Accept-Language", "uz") if req else "uz"

    def get_nomi(self, obj):
        tr = obj.translations.filter(language=self.get_language()).first()
        return tr.nomi if tr else None

class KonsultatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultatsiya
        fields = ["id", "hudud", "yonalish_amaliyoti", "tel_raqam"]
        extra_kwargs = {
            "tel_raqam": {"required": True},
            "hudud": {"required": True},
            "yonalish_amaliyoti": {"required": True},
        }

    def create(self, validated_data):
        # is_checked har doim default False bo'ladi
        konsultatsiya = Konsultatsiya.objects.create(**validated_data)
        return konsultatsiya
