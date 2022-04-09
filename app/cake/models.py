from django.db import models


class Cake(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128)

    def __str__(self):
        return self.name


