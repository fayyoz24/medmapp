from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Hudud(models.Model):
    nomi = models.CharField(max_length=100)

    @classmethod
    def plural_name(cls):
        return "Hududlar"

    def __str__(self):
        return self.nomi

class DavolashUsuli(models.Model):
    nomi = models.CharField(max_length=100)

    @classmethod
    def plural_name(cls):
        return "Davolash usullari"

    def __str__(self):
        return self.nomi

class Konsultatsiya(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak (masalan: +998901234567)."
    )

    hudud = models.ForeignKey('Hudud', on_delete=models.CASCADE)
    davolash_usuli = models.ForeignKey('DavolashUsuli', on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=15, validators=[phone_validator])

    @classmethod
    def plural_name(cls):
        return "Konsultatsiya so'rovlari"

    def __str__(self):
        return self.tel_raqam
