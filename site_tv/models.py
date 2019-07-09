from _datetime import datetime
from django.db import models
from django.urls import reverse


class Post(models.Model):
    TV_CHOICE = (
        ('KTRK', 'KTRK'),
        ('RTR', 'RTR'),
        ('ORT', 'ORT'),
        ('NBT', 'NBT'),
        ('APRIL', 'APRIL')
    )
    text = models.TextField()
    tv_choice = models.CharField(max_length=5, choices=TV_CHOICE)
    order_date = models.DateTimeField(default=datetime.now)
    post_dates = models.IntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    reception = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}{}{}{}'.format(self.text, self.tv_choice, self.order_date, self.price, )
