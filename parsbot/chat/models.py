from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from parsbot.models import BaseCreateUpdateModel


class Product(BaseCreateUpdateModel):
    WAITING = 'waiting'
    WATCHING = 'watching'
    STOPPED = 'stopped'

    PRODUCT_STATUSES = (
        (WAITING, 'Waiting'),
        (WATCHING, 'Watching'),
        (STOPPED, 'Stoped')
    )
    title = models.CharField(max_length=255, verbose_name='Products')
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    url = models.URLField(verbose_name='Product URL')
    status = models.CharField(choices=PRODUCT_STATUSES, default=WAITING, max_length=16)


class ProductHistory(models.Model):
    create_at = models.DateTimeField(auto_created=True)

    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, related_name='history')
    price = models.DecimalField(max_digits=19, decimal_places=2)
