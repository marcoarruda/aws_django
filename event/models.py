from __future__ import unicode_literals

from django.db import models

class Subscription(models.Model):
  subscription_name = models.CharField(max_length=200)
  subscription_email = models.CharField(max_length=200)
  subscription_datetime = models.DateTimeField('subscription date and time')

  def __str__(self):
    return self.subscription_name
