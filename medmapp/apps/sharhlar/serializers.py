from rest_framework import serializers
from .models import MamnunBemor, BemorFikri


class MamnunBemorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamnunBemor
        fields = ["id", "mamnun", "ijobiy_foiz", "mamlakat_bemorlari"]


class BemorFikriSerializer(serializers.ModelSerializer):
    bemor_ismi = serializers.CharField(source="bemor.username", read_only=True)
    shifoxona_nomi = serializers.SerializerMethodField()
    amaliyot_nomi = serializers.SerializerMethodField()

    class Meta:
        model = BemorFikri
        fields = [
            "id",
            "bemor_ismi",
            "sharh_matni",
            "yaratilgan_sana",
            "shifoxona_nomi",
            "amaliyot_nomi",
            "baho",
        ]

    def get_shifoxona_nomi(self, obj):
        if obj.shifoxona:
            tr = obj.shifoxona.translations.first()
            return tr.title if tr else str(obj.shifoxona)
        return None

    def get_amaliyot_nomi(self, obj):
        if obj.amaliyot:
            tr = obj.amaliyot.translations.first()
            return tr.title if tr else str(obj.amaliyot)
        return None
