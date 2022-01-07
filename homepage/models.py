from django.db import models

# Create your models here.

# class <model name> (models.Model):

class Coffee(models.Model):
    
    
    """
    field1 = models.FieldType()...
    field1 = models.FieldType()...
    field1 = models.FieldType()...
    
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ..
    논리형 : BooleanField
    시간/날짜 : DataTimeFiled
    """

    def __str__(self):
        return self.name
    name = models.CharField(default = "", max_length = 30)
    price = models.IntegerField(default = 0)
    is_ice = models.BooleanField(default = False)
    
    