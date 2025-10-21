from django.core.management.base import BaseCommand
from faker import Faker
import random

from bosh_sahifa.models import (
    Hudud, HududTranslation,
    AsosiyYonalish, AsosiyYonalishTranslation,
    YonalishAmaliyoti, YonalishAmaliyotiTranslation,
    Natijalar, NatijalarTranslation,
    BizningXizmatlarEhtiyojQoplaydi, BizningXizmatlarEhtiyojQoplaydiTranslation,
    DavolashUsuliTanlang, DavolashUsuliTanlangTranslation,
    Konsultatsiya
)
from shifokorlar.models import Shifokor
from shifoxonalar.models import Shifoxona

fake = Faker()

LANGS = ['uz', 'ru', 'en']


class Command(BaseCommand):
    help = "Seeds the database with fake data for bosh_sahifa models"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🌱 Seeding fake data..."))

        # ---------- HUDUD ----------
        for _ in range(5):
            hudud = Hudud.objects.create()
            for lang in LANGS:
                HududTranslation.objects.create(
                    hudud=hudud,
                    language=lang,
                    nomi=fake.city()
                )

        # ---------- ASOSIY YO‘NALISH ----------
        for _ in range(3):
            asosiy = AsosiyYonalish.objects.create(logo=f"bosh_sahifa/asosiy_yonalish/{fake.file_name()}")
            for lang in LANGS:
                AsosiyYonalishTranslation.objects.create(
                    yordam=asosiy,
                    language=lang,
                    title=fake.catch_phrase(),
                    text=fake.paragraph(nb_sentences=2)
                )

        # ---------- YONALISH AMALIYOTI ----------
        for asosiy in AsosiyYonalish.objects.all():
            for _ in range(2):
                amaliyot = YonalishAmaliyoti.objects.create(
                    asosiy_yonalish=asosiy,
                    logo=f"bosh_sahifa/yonalish_amaliyoti/{fake.file_name()}",
                    narx=random.randint(100, 1000)
                )
                for lang in LANGS:
                    YonalishAmaliyotiTranslation.objects.create(
                        narx_obj=amaliyot,
                        language=lang,
                        title=fake.job(),
                        text=fake.sentence()
                    )

        # ---------- NATIJALAR ----------
        for _ in range(5):
            natija = Natijalar.objects.create(
                logo=f"bosh_sahifa/natijalar/{fake.file_name()}",
                statistik_raqam=random.randint(100, 10000)
            )
            for lang in LANGS:
                NatijalarTranslation.objects.create(
                    natija=natija,
                    language=lang,
                    text=fake.sentence()
                )

        # ---------- BIZNING XIZMATLAR ----------
        for _ in range(4):
            xizmat = BizningXizmatlarEhtiyojQoplaydi.objects.create(
                icon=f"bosh_sahifa/bizning_xizmatlar/{fake.file_name()}"
            )
            for lang in LANGS:
                BizningXizmatlarEhtiyojQoplaydiTranslation.objects.create(
                    parent=xizmat,
                    language=lang,
                    title=fake.catch_phrase(),
                    text=fake.text(max_nb_chars=200)
                )

        # ---------- DAvOLASH USULI TANLANG ----------
        if Shifokor.objects.exists() and Shifoxona.objects.exists():
            for _ in range(5):
                davolash = DavolashUsuliTanlang.objects.create(
                    rating=round(random.uniform(3.0, 5.0), 1),
                    shifoxona=random.choice(Shifoxona.objects.all()),
                    davomiylik=random.randint(3, 14),
                    doktor=random.choice(Shifokor.objects.all()),
                    narx=random.randint(100, 2000)
                )
                for lang in LANGS:
                    DavolashUsuliTanlangTranslation.objects.create(
                        parent=davolash,
                        language=lang,
                        nomi=fake.word()
                    )

        # ---------- KONSULTATSIYA ----------
        hudud = Hudud.objects.first()
        yonalish = YonalishAmaliyoti.objects.first()
        for _ in range(5):
            Konsultatsiya.objects.create(
                hudud=hudud,
                yonalish_amaliyoti=yonalish,
                tel_raqam=f"+9989{random.randint(10000000, 99999999)}",
                is_checked=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("✅ Fake data successfully added!"))
