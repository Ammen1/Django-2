from django.db import models

class Car(models.Model):
    name  = models.CharField(max_length=length, ${blank=True, null=True})
    
    

    class Meta:
        verbose_name = _("cR")
        verbose_name_plural = _("Cars this line is responsible for the conflict of the code")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

