from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)


class Address(models.Model):
    ADDRESS_TYPES = ((0, 'mailing'), (1, 'billing'), (2, 'shipping'),)

    contact = models.ForeignKey(Contact)
    addressType = models.PositiveIntegerField(choices=ADDRESS_TYPES, default=0)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    street3 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    postalCode = models.CharField(max_length=16)
    isDefault = models.BooleanField(default=False)

    
