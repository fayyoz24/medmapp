from django.db import models

# Create your models here.
from users.models import User
from shifoxonalar.models import Shifoxona
from bosh_sahifa.models import YonalishAmaliyoti


class MamnunBemor(models.Model):
    mamnun = models.PositiveIntegerField()
    ijobiy_foiz = models.PositiveIntegerField()
    mamlakat_bemorlari = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Mamnun bemor"
        verbose_name_plural = "Mamnun bemorlar"

    def __str__(self):
        return f"Mamnun bemor {self.id} - Bemor: {self.bemor.username}"

class BemorFikri(models.Model):
    bemor = models.ForeignKey(User, on_delete=models.CASCADE)
    sharh_matni = models.TextField()
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)
    shifoxona = models.ForeignKey(Shifoxona, on_delete=models.CASCADE, null=True, blank=True)
    amaliyot = models.ForeignKey(YonalishAmaliyoti, on_delete=models.CASCADE, null=True, blank=True)
    baho = models.PositiveIntegerField(default=5)


    class Meta:
        verbose_name = "Bemorlar fikri"
        verbose_name_plural = "Bemorlar fikrlari"
        ordering = ["-yaratilgan_sana"]

    def __str__(self):
        return f"Fikr {self.id} - Bemor: {self.bemor.username}"