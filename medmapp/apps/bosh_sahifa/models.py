from django.db import models
from django.core.validators import RegexValidator
from shifokorlar.models import Shifokor
from shifoxonalar.models import Shifoxona
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


# ---------- KONSULTATSIYA ----------
class Konsultatsiya(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak (masalan: +998901234567)."
    )

    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    yonalish_amaliyoti = models.ForeignKey("YonalishAmaliyoti", on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=15, validators=[phone_validator])
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Konsultatsiya"
        verbose_name_plural = "Konsultatsiyalar"

    def __str__(self):
        return self.tel_raqam


# ---------- ASOSIY YO‘NALISH ----------
class AsosiyYonalish(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/asosiy_yonalish/')

    class Meta:
        verbose_name = "Asosiy yo‘nalish"
        verbose_name_plural = "Asosiy yo‘nalishlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Asosiy yo‘nalish"
    
    def save(self, *args, **kwargs):
        # Only compress if the image is new or changed
        if self.logo and hasattr(self.logo, 'file'):
            # Compress before saving
            new_image = compress_image(self.logo, quality=70)
            self.logo.save(self.logo.name, new_image, save=False)

        super().save(*args, **kwargs)

class AsosiyYonalishTranslation(models.Model):
    yordam = models.ForeignKey(AsosiyYonalish, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("yordam", "language")
        verbose_name = "Tibbiy yordam (tarjima)"
        verbose_name_plural = "Tibbiy yordamlar (tarjimalar)"

    def __str__(self):
        return f"{self.title} ({self.language})"

# ---------- KAFOLATLANGAN ARZON NARXLAR ----------
class YonalishAmaliyoti(models.Model):
    asosiy_yonalish = models.ForeignKey(AsosiyYonalish, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='bosh_sahifa/yonalish_amaliyoti/')
    narx = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Yonalish amaliyoti"
        verbose_name_plural = "Yonalish amaliyotlari"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Narx"

    def save(self, *args, **kwargs):
        # Only compress if the image is new or changed
        if self.logo and hasattr(self.logo, 'file'):
            # Compress before saving
            new_image = compress_image(self.logo, quality=70)
            self.logo.save(self.logo.name, new_image, save=False)

        super().save(*args, **kwargs)

class YonalishAmaliyotiTranslation(models.Model):
    narx_obj = models.ForeignKey(YonalishAmaliyoti, related_name="translations", on_delete=models.CASCADE)

    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("narx_obj", "language")
        verbose_name = "Yonalish amaliyoti (tarjima)"
        verbose_name_plural = "Yonalish amaliyotlari (tarjimalar)"

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
    
    def save(self, *args, **kwargs):
        # Only compress if the image is new or changed
        if self.logo and hasattr(self.logo, 'file'):
            # Compress before saving
            new_image = compress_image(self.logo, quality=70)
            self.logo.save(self.logo.name, new_image, save=False)
        
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        # Only compress if the image is new or changed
        if self.icon and hasattr(self.icon, 'file'):
            # Compress before saving
            new_image = compress_image(self.icon, quality=70)
            self.icon.save(self.icon.name, new_image, save=False)

        super().save(*args, **kwargs)

        
class BizningXizmatlarEhtiyojQoplaydiTranslation(models.Model):
    parent = models.ForeignKey(BizningXizmatlarEhtiyojQoplaydi, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    title = models.CharField(max_length=200)
    text = models.TextField()


# ===================== Davolash usuli tanlang =====================
class DavolashUsuliTanlang(models.Model):
    rating = models.FloatField(default=5.0)
    shifoxona = models.ForeignKey(Shifoxona, on_delete=models.CASCADE)
    davomiylik = models.PositiveIntegerField(help_text="Davolash davomiyligi (kunlarda)")
    doktor = models.ForeignKey(Shifokor, on_delete=models.CASCADE)
    narx = models.PositiveIntegerField(help_text="Davolash narxi $da")

    def __str__(self):
        return f"{self.id} - Davolash usuli"

class DavolashUsuliTanlangTranslation(models.Model):
    parent = models.ForeignKey(DavolashUsuliTanlang, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    nomi = models.CharField(max_length=100)