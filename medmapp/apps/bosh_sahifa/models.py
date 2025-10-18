from django.db import models
from django.core.validators import RegexValidator

from django.db import models
from django.core.validators import RegexValidator


# ---------- HUDUD ----------
class Hudud(models.Model):
    class Meta:
        verbose_name = "Hudud"
        verbose_name_plural = "Hududlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().nomi if self.translations.exists() else "Hudud"


class HududTranslation(models.Model):
    hudud = models.ForeignKey(Hudud, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2,
        choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")],
    )
    nomi = models.CharField(max_length=100)

    class Meta:
        unique_together = ("hudud", "language")
        verbose_name = "Hudud (tarjima)"
        verbose_name_plural = "Hududlar (tarjimalar)"

    def __str__(self):
        return f"{self.nomi} ({self.language})"


# ---------- DAVOLASH USULI ----------
class DavolashUsuli(models.Model):
    class Meta:
        verbose_name = "Davolash usuli"
        verbose_name_plural = "Davolash usullari"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().nomi if self.translations.exists() else "Davolash usuli"


class DavolashUsuliTranslation(models.Model):
    davolash_usuli = models.ForeignKey(DavolashUsuli, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2,
        choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")],
    )
    nomi = models.CharField(max_length=100)

    class Meta:
        unique_together = ("davolash_usuli", "language")
        verbose_name = "Davolash usuli (tarjima)"
        verbose_name_plural = "Davolash usullari (tarjimalar)"

    def __str__(self):
        return f"{self.nomi} ({self.language})"


# ---------- KONSULTATSIYA ----------
class Konsultatsiya(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak (masalan: +998901234567)."
    )

    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    davolash_usuli = models.ForeignKey(DavolashUsuli, on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=15, validators=[phone_validator])
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Konsultatsiya"
        verbose_name_plural = "Konsultatsiyalar"

    def __str__(self):
        return self.tel_raqam


# ---------- KO‘P TARMOQLI TIBBIY YORDAM ----------
class KopTarmoqliTibbiyYordam(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/kop_tarmoqli_tibbiy_yordam/')

    class Meta:
        verbose_name = "Ko‘p tarmoqli tibbiy yordam"
        verbose_name_plural = "Ko‘p tarmoqli tibbiy yordamlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Tibbiy yordam"


class KopTarmoqliTibbiyYordamTranslation(models.Model):
    yordam = models.ForeignKey(KopTarmoqliTibbiyYordam, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("yordam", "language")
        verbose_name = "Tibbiy yordam (tarjima)"
        verbose_name_plural = "Tibbiy yordamlar (tarjimalar)"

    def __str__(self):
        return f"{self.title} ({self.language})"


# ---------- OMMABOP SHIFOXONALAR ----------
class OmmabopShifoxonalar(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/ommabop_shifoxonalar/')

    class Meta:
        verbose_name = "Ommabop shifoxona"
        verbose_name_plural = "Ommabop shifoxonalar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Shifoxona"


class OmmabopShifoxonalarTranslation(models.Model):
    shifoxona = models.ForeignKey(OmmabopShifoxonalar, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("shifoxona", "language")
        verbose_name = "Shifoxona (tarjima)"
        verbose_name_plural = "Shifoxonalar (tarjimalar)"

    def __str__(self):
        return f"{self.title} ({self.language})"


# ---------- KAFOLATLANGAN ARZON NARXLAR ----------
class KafolatlanganArzonNarxlar(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/kafolatlangan_arzon_narxlar/')
    narx = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Kafolatlangan arzon narx"
        verbose_name_plural = "Kafolatlangan arzon narxlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Narx"


class KafolatlanganArzonNarxlarTranslation(models.Model):
    narx_obj = models.ForeignKey(KafolatlanganArzonNarxlar, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("narx_obj", "language")
        verbose_name = "Narx (tarjima)"
        verbose_name_plural = "Narxlar (tarjimalar)"

    def __str__(self):
        return f"{self.title} ({self.language})"


# ---------- NATIJALAR ----------
class Natijalar(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/natijalar/')
    statistik_raqam = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"

    def __str__(self):
        return self.translations.first().text if self.translations.exists() else "Natija"


class NatijalarTranslation(models.Model):
    natija = models.ForeignKey(Natijalar, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    text = models.CharField(max_length=255)

    class Meta:
        unique_together = ("natija", "language")
        verbose_name = "Natija (tarjima)"
        verbose_name_plural = "Natijalar (tarjimalar)"

    def __str__(self):
        return f"{self.text} ({self.language})"

# ===================== Bizning xizmatlar =====================
class BizningXizmatlarEhtiyojQoplaydi(models.Model):
    icon = models.ImageField(upload_to='bosh_sahifa/bizning_xizmatlar/')

    def __str__(self):
        return f"{self.id} - Xizmat"

class BizningXizmatlarEhtiyojQoplaydiTranslation(models.Model):
    parent = models.ForeignKey(BizningXizmatlarEhtiyojQoplaydi, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    title = models.CharField(max_length=200)
    text = models.TextField()


# ===================== Mashhur shifokorlar =====================
class MashhurShifokorlar(models.Model):
    photo = models.ImageField(upload_to='bosh_sahifa/mashhur_shifokorlar/')
    rating = models.FloatField(default=5.0)
    tajriba_yil = models.PositiveIntegerField()
    jarrohlik_amaliyotlar_soni = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id} - Shifokor"

class MashhurShifokorlarTranslation(models.Model):
    parent = models.ForeignKey(MashhurShifokorlar, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    ism_familiya = models.CharField(max_length=200)
    mutaxassislik = models.CharField(max_length=200)
    maslahat = models.TextField()


# ===================== Davolash usuli tanlang =====================
class DavolashUsuliTanlang(models.Model):
    rating = models.FloatField(default=5.0)
    location = models.CharField(max_length=200)
    davomiylik = models.PositiveIntegerField(help_text="Davolash davomiyligi (kunlarda)")
    doktor = models.ForeignKey(MashhurShifokorlar, on_delete=models.CASCADE)
    narx = models.PositiveIntegerField(help_text="Davolash narxi $da")

    def __str__(self):
        return f"{self.id} - Davolash usuli"

class DavolashUsuliTanlangTranslation(models.Model):
    parent = models.ForeignKey(DavolashUsuliTanlang, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    nomi = models.CharField(max_length=100)