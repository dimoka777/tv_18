from _datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError


class Choice(models.Model):
    tv_name = models.CharField(verbose_name='Имя', max_length=255)
    tv_price = models.FloatField()

    def __str__(self):
        return "{}".format(self.tv_name)


class Post(models.Model):
    text = models.TextField()
    order_date = models.DateTimeField(default=datetime.now)
    post_dates = models.IntegerField()
    quantity_symbols = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    reception = models.BooleanField(default=False)
    choice = models.ForeignKey(Choice, related_name='posts', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}{}{}'.format(self.text, self.order_date, self.quantity_symbols, )


@receiver(pre_save, sender=Post)
def total_price(sender, instance, **kwargs):
    try:
        str_text = instance.text.replace(" ", "")
        instance.total_price = len(str_text) * instance.choice.tv_price
        instance.quantity_symbols = len(str_text)
    except:
        raise ValidationError('Choise is null')

