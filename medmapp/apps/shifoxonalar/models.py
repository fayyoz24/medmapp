from django.db import models
# Create your models here.

class Davlat(models.Model):
    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().nomi if self.translations.exists() else "Davlat"


class DavlatTranslation(models.Model):
    davlat = models.ForeignKey(Davlat, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    nomi = models.CharField(max_length=100)

    class Meta:
        unique_together = ("davlat", "language")
        verbose_name = "Davlat (tarjima)"
        verbose_name_plural = "Davlatlar (tarjimalar)"

    def __str__(self):
        return f"{self.nomi} ({self.language})"


# ===================== SHAHAR =====================
class Shahar(models.Model):
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Shahar"
        verbose_name_plural = "Shaharlar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().nomi if self.translations.exists() else "Shahar"


class ShaharTranslation(models.Model):
    shahar = models.ForeignKey(Shahar, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    nomi = models.CharField(max_length=100)

    class Meta:
        unique_together = ("shahar", "language")
        verbose_name = "Shahar (tarjima)"
        verbose_name_plural = "Shaharlar (tarjimalar)"

    def __str__(self):
        return f"{self.nomi} ({self.language})"


class Shifoxona(models.Model):
    logo = models.ImageField(upload_to='bosh_sahifa/ommabop_shifoxonalar/')
    shahar = models.ForeignKey(Shahar, on_delete=models.CASCADE)
    asosiy_yonalish = models.ManyToManyField("bosh_sahifa.AsosiyYonalish")

    class Meta:
        verbose_name = "shifoxona"
        verbose_name_plural = "shifoxonalar"
        ordering = ["id"]

    def __str__(self):
        return self.translations.first().title if self.translations.exists() else "Shifoxona"

    def save(self, *args, **kwargs):
        # Only compress if the image is new or changed
        if self.logo and hasattr(self.logo, 'file'):
            # Compress before saving
            new_image = compress_image(self.logo, quality=70)
            self.logo.save(self.logo.name, new_image, save=False)

        super().save(*args, **kwargs)

class ShifoxonaTranslation(models.Model):
    shifoxona = models.ForeignKey(Shifoxona, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian"), ("en", "English")])
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        unique_together = ("shifoxona", "language")
        verbose_name = "Shifoxona (tarjima)"
        verbose_name_plural = "Shifoxonalar (tarjimalar)"

    def __str__(self):
        return f"{self.title} ({self.language})"