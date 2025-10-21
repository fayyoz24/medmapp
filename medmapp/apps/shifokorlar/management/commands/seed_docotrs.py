from django.core.management.base import BaseCommand
from faker import Faker
import random

from shifokorlar.models import Shifokor, ShifokorTranslation
from shifoxonalar.models import Shifoxona
from bosh_sahifa.models import AsosiyYonalish

fake = Faker()
LANGS = ['uz', 'ru', 'en']


class Command(BaseCommand):
    help = "Seeds fake data for Shifokor (doctors) and translations"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🌱 Seeding fake shifokorlar..."))

        # Ensure dependencies exist
        shifoxonalar = list(Shifoxona.objects.all())
        yonalishlar = list(AsosiyYonalish.objects.all())

        if not shifoxonalar or not yonalishlar:
            self.stdout.write(self.style.WARNING("⚠️ Please add some Shifoxona and AsosiyYonalish before seeding."))
            return

        for _ in range(8):
            shifoxona = random.choice(shifoxonalar)
            shifokor = Shifokor.objects.create(
                photo=f"bosh_sahifa/shifokorlar/{fake.file_name()}",
                rating=round(random.uniform(3.5, 5.0), 1),
                tajriba_yil=random.randint(3, 25),
                jarrohlik_amaliyotlar_soni=random.randint(50, 500),
                shifoxona=shifoxona,
                rezyume=f"bosh_sahifa/shifokorlar/rezyume/{fake.file_name(extension='pdf')}",
            )
            # Assign 1–3 random yonalis
