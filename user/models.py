from django.db import models

# Create your models here.
class User(models.Model):
    name      = models.CharField(max_length=500)
    email     = models.EmailField(max_length=250)
    password  = models.CharField(max_length=250)
    location_is_agreed  = models.BooleanField()
    promotion_is_agreed = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'users'
    