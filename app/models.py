from django.utils import timezone

from django.contrib import admin
from django.db import models

# Register your models here.
class AppVariaty(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL','KIWI'),
    ('PL','PLAIN'),
    ('EL','ELACHI'),
  ]
  name = models.CharField(max_length= 100)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length = 2, choices = CHAI_TYPE_CHOICE)
  description = models.TextField(default="Good Chai")
  
  
  def __str__(self):
    return self.name