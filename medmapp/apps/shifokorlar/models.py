from django.db import models

# Create your models here.
# ===================== Mashhur shifokorlar =====================
class Shifokor(models.Model):
    photo = models.ImageField(upload_to='bosh_sahifa/shifokorlar/')
    rating = models.FloatField(default=5.0)
    tajriba_yil = models.PositiveIntegerField()
    jarrohlik_amaliyotlar_soni = models.PositiveIntegerField()
    shifoxona = models.ForeignKey("shifoxonalar.Shifoxona", on_delete=models.CASCADE)
    rezyume = models.FileField(upload_to='bosh_sahifa/shifokorlar/rezyume/')
    yonalish = models.ManyToManyField("bosh_sahifa.AsosiyYonalish")

    class Meta:
        verbose_name = "Shifokor"
        verbose_name_plural = "Shifokorlar"
        ordering = ["id"]

    def __str__(self):
        return f"{self.id} - Shifokor"

class ShifokorTranslation(models.Model):
    parent = models.ForeignKey(Shifokor, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')])
    ism_familiya = models.CharField(max_length=200)
    maslahat = models.TextField()

    class Meta: 
        unique_together = ("parent", "language")
        verbose_name = "Shifokor (tarjima)"
        verbose_name_plural = "Shifokorlar (tarjimalar)"

    def __str__(self):
        return f"{self.ism_familiya} ({self.language})"