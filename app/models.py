from django.utils import timezone

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

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
  
  
#One to Many Relationship

class AppReview(models.Model):
  app = models.ForeignKey(AppVariaty, on_delete = 
  models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default = timezone.now)
  
  
  def __str__(self):
    return f'{self.user.username} review of {self.app.name}'
  
  
# Many to Many Relationship

class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=200)
  chai_varieties = models.ManyToManyField(AppVariaty, related_name = 'stores')
  
  def __str__(self):
    return self.name


# one  to one relationship

class AppCertificate(models.Model):
  app = models.OneToOneField(AppVariaty, on_delete=models.CASCADE, related_name='certificate')
  issued_by = models.CharField(max_length=100)
  issue_date = models.DateField()
  valid_until = models.DateField()
  
  def __str__(self):
    return f'Certificate for {self.app.name} issued by {self.issued_by}'