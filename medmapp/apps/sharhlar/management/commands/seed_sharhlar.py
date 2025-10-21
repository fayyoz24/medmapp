from django.core.management.base import BaseCommand
from faker import Faker
import random

from sharhlar.models import MamnunBemor, BemorFikri
from users.models import User
from shifoxonalar.models import Shifoxona
from bosh_sahifa.models import YonalishAmaliyoti

fake = Faker()


class Command(BaseCommand):
    help = "Seeds the database with fake data for bemorlar (reviews and satisfaction)"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🌱 Seeding bemor data..."))

        # ---------- MAMNUN BEMORLAR ----------
        for _ in range(3):
            MamnunBemor.objects.create(
                mamnun=random.randint(1000, 5000),
                ijobiy_foiz=random.randint(70, 100),
                mamlakat_bemorlari=random.randint(2000, 10000)
            )

        self.stdout.write(self.style.SUCCESS("✅ Mamnun bemorlar added."))

        # ---------- BEMORLAR FIKRLARI ----------
        users = list(User.objects.all())
        shifoxonalar = list(Shifoxona.objects.all())
        amaliyotlar = list(YonalishAmaliyoti.objects.all())

        if not users or not shifoxonalar or not amaliyotlar:
            self.stdout.write(self.style.WARNING("⚠️ Not enough related data (users, shifoxonalar, amaliyotlar)!"))
            return

        for _ in range(10):
            BemorFikri.objects.create(
                bemor=random.choice(users),
                sharh_matni=fake.paragraph(nb_sentences=3),
                shifoxona=random.choice(shifoxonalar),
                amaliyot=random.choice(amaliyotlar),
                baho=random.randint(3, 5)
            )

        self.stdout.write(self.style.SUCCESS("✅ Bemorlar fikrlari added successfully!"))
