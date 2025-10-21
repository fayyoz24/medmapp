from django.core.management.base import BaseCommand
from faker import Faker
import random

from shifoxonalar.models import (
    Davlat, DavlatTranslation,
    Shahar, ShaharTranslation,
    Shifoxona, ShifoxonaTranslation
)
from bosh_sahifa.models import AsosiyYonalish

fake = Faker()
LANGS = ["uz", "ru", "en"]


class Command(BaseCommand):
    help = "Seeds fake data for Davlat, Shahar, and Shifoxona models with translations"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🌱 Seeding davlat, shahar, va shifoxonalar..."))

        yonalishlar = list(AsosiyYonalish.objects.all())
        if not yonalishlar:
            self.stdout.write(self.style.WARNING("⚠️ Please seed AsosiyYonalish first (run `seed_data`)."))
            return

        # ---------- DAVLAT ----------
        davlatlar = []
        for _ in range(3):
            davlat = Davlat.objects.create()
            for lang in LANGS:
                DavlatTranslation.objects.create(
                    davlat=davlat,
                    language=lang,
                    nomi=fake.country()
                )
            davlatlar.append(davlat)

        # ---------- SHAHRLAR ----------
        shaharlar = []
        for davlat in davlatlar:
            for _ in range(random.randint(2, 4)):
                shahar = Shahar.objects.create(davlat=davlat)
                for lang in LANGS:
                    ShaharTranslation.objects.create(
                        shahar=shahar,
                        language=lang,
                        nomi=fake.city()
                    )
                shaharlar.append(shahar)

        # ---------- SHIFOXONALAR ----------
        for _ in range(5):
            shahar = random.choice(shaharlar)
            shifoxona = Shifoxona.objects.create(
                logo=f"bosh_sahifa/ommabop_shifoxonalar/{fake.file_name()}",
                shahar=shahar
            )
            # Assign 1–3 random yo‘nalishlar
            selected_yonalishlar = random.sample(yonalishlar, random.randint(1, min(3, len(yonalishlar))))
            shifoxona.asosiy_yonalish.set(selected_yonalishlar)

            # Add translations
            for lang in LANGS:
                ShifoxonaTranslation.objects.create(
                    shifoxona=shifoxona,
                    language=lang,
                    title=fake.company(),
                    text=fake.paragraph(nb_sentences=2)
                )

        self.stdout.write(self.style.SUCCESS("✅ Fake davlatlar, shaharlar, va shifoxonalar successfully added!"))
