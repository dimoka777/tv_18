from _datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse


class Post(models.Model):
    TV_CHOICE = (
        ('5CHAN', '5CHAN'),
        ('PIRAMIDA', 'PIRAMIDA'),
        ('ELTR', 'ELTR'),
        ('NARYN', 'NARYN'),
        ('CTV', 'CTV')
    )
    text = models.TextField()
    tv_choice = models.CharField(max_length=5, choices=TV_CHOICE)
    order_date = models.DateTimeField(default=datetime.now)
    post_dates = models.IntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    reception = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}{}{}{}'.format(self.text, self.tv_choice, self.order_date, self.price, )


@receiver(pre_save, sender=Post)
def total_price(sender, instance, **kwargs):
    instance.price = len(instance.text)

