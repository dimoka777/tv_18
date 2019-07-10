from _datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse


class Choice(models.Model):
    tv_name = models.CharField(verbose_name='Имя', max_length=255)
    tv_price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}".format(self.tv_name)


class Post(models.Model):
    tv_choice = models.ForeignKey('Choice', related_name='posts', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    order_date = models.DateTimeField(default=datetime.now)
    post_dates = models.IntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    reception = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}{}{}'.format(self.text, self.order_date, self.price, )


@receiver(pre_save, sender=Post)
def total_price(sender, instance, **kwargs):
    instance.price = len(instance.text)

