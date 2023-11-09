from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    # this is ok
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # this is also ok
    return_rate = models.FloatField()
    # Semgrep finds this because old_fee ends in the word fee, which is in the regex above
    old_fee = models.FloatField()
    # match this
    price_inc = models.FloatField()
