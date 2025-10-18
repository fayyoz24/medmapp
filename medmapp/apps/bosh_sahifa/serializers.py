from rest_framework import serializers
from .models import (Hudud, HududTranslation, 
                        DavolashUsuli, 
                        DavolashUsuliTranslation, 
                        Konsultatsiya,
                        KopTarmoqliTibbiyYordam,
                        OmmabopShifoxonalar,
                        KafolatlanganArzonNarxlar,
                        Natijalar,
                        DavolashUsuliTanlang,
                        BizningXizmatlarEhtiyojQoplaydi,
                        BizningXizmatlarEhtiyojQoplaydiTranslation,
                        MashhurShifokorlar,
                        MashhurShifokorlarTranslation,
                        KopTarmoqliTibbiyYordamTranslation,
                        OmmabopShifoxonalarTranslation,
                        KafolatlanganArzonNarxlarTranslation,
                        NatijalarTranslation
)

# ---------- Tarjima serializerlari ----------
class HududTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HududTranslation
        fields = ["language", "nomi"]


class DavolashUsuliTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DavolashUsuliTranslation
        fields = ["language", "nomi"]


# ---------- Asosiy serializerlar ----------
class HududSerializer(serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()

    class Meta:
        model = Hudud
        fields = ["id", "nomi"]

    def get_nomi(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.nomi if translation else obj.translations.first().nomi if obj.translations.exists() else None


class DavolashUsuliSerializer(serializers.ModelSerializer):
    nomi = serializers.SerializerMethodField()

    class Meta:
        model = DavolashUsuli
        fields = ["id", "nomi"]

    def get_nomi(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.nomi if translation else obj.translations.first().nomi if obj.translations.exists() else None


class KonsultatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultatsiya
        fields = ["id", "hudud", "davolash_usuli", "tel_raqam"]
        extra_kwargs = {
            "tel_raqam": {"required": True},
            "hudud": {"required": True},
            "davolash_usuli": {"required": True},
        }

    def create(self, validated_data):
        # is_checked har doim default False bo'ladi
        konsultatsiya = Konsultatsiya.objects.create(**validated_data)
        return konsultatsiya

# ---------- KO‘P TARMOQ TIBBIY YORDAM ----------
class KopTarmoqliTibbiyYordamSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    logo = serializers.ImageField(read_only=True)

    class Meta:
        model = KopTarmoqliTibbiyYordam
        fields = ["id", "logo", "title", "text"]

    def get_title(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.title if translation else obj.translations.first().title if obj.translations.exists() else None

    def get_text(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.text if translation else obj.translations.first().text if obj.translations.exists() else None


# ---------- OMMABOP SHIFOXONALAR ----------
class OmmabopShifoxonalarSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    logo = serializers.ImageField(read_only=True)

    class Meta:
        model = OmmabopShifoxonalar
        fields = ["id", "logo", "title", "text"]

    def get_title(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.title if translation else obj.translations.first().title if obj.translations.exists() else None

    def get_text(self, obj):
        lang = self.context.get("lang", "uz")
        translation = obj.translations.filter(language=lang).first()
        return translation.text if translation else obj.translations.first().text if obj.translations.exists() else None



# ---------- KAFOLATLANGAN ARZON NARXLAR ----------
class KafolatlanganArzonNarxlarTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafolatlanganArzonNarxlarTranslation
        fields = ["language", "title", "text"]


class KafolatlanganArzonNarxlarSerializer(serializers.ModelSerializer):
    translations = KafolatlanganArzonNarxlarTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = KafolatlanganArzonNarxlar
        fields = ["id", "logo", "narx", "translations"]


# ---------- NATIJALAR ----------
class NatijalarTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatijalarTranslation
        fields = ["language", "text"]


class NatijalarSerializer(serializers.ModelSerializer):
    translations = NatijalarTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Natijalar
        fields = ["id", "logo", "statistik_raqam", "translations"]



# ===================== Bizning xizmatlar =====================
class BizningXizmatlarEhtiyojQoplaydiTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BizningXizmatlarEhtiyojQoplaydiTranslation
        fields = ["language", "title", "text"]


class BizningXizmatlarEhtiyojQoplaydiSerializer(serializers.ModelSerializer):
    translations = BizningXizmatlarEhtiyojQoplaydiTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = BizningXizmatlarEhtiyojQoplaydi
        fields = ["id", "icon", "translations"]


# ===================== Mashhur shifokorlar =====================
class MashhurShifokorlarTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MashhurShifokorlarTranslation
        fields = ["language", "ism_familiya", "mutaxassislik", "maslahat"]


class MashhurShifokorlarSerializer(serializers.ModelSerializer):
    translations = MashhurShifokorlarTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = MashhurShifokorlar
        fields = ["id", "photo", "rating", "tajriba_yil", "jarrohlik_amaliyotlar_soni", "translations"]
