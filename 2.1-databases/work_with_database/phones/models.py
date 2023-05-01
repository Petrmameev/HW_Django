from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

