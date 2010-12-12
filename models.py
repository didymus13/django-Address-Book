from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'companies'
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('companies.views.detail', [str(self.id)])

class Contact(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    company = models.ForeignKey(Company, null=True)
    
    def _makeFullName(self):
        return "%s %s" % (self.firstname, self.lastname)
    fullname = property(_makeFullName)
    
    def __unicode__(self):
        return self.fullname

class Address(models.Model):
    ADDRESS_TYPES = ((0, 'mailing'), (1, 'billing'), (2, 'shipping'),)

    addressType = models.PositiveIntegerField(choices=ADDRESS_TYPES, default=0)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    street3 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    postalCode = models.CharField(max_length=16)
    isDefault = models.BooleanField(default=False)

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.street1

    def get_absolute_url(self):
        return "/addressbook/api/contacts/%d/addresses/%d" % (self.contact.id, self.id)

class ContactAddress(Address):
    contact = models.ForeignKey(Contact)
    
    @models.permalink
    def get_absolute_url(self):
        return('contacts.views.address_detail', [str(self.id)])

class CompanyAddress(Address):
    company = models.ForeignKey(Company)
    
    @models.permalink
    def get_absolute_url(self):
        return('companies.views.address_detail', [str(self.id)])

class TelephoneNumber(models.Model):
    TELEPHONE_TYPE = ((0, 'telephone'), (1, 'fax'))

    number = models.CharField(max_length=255)
    extension = models.CharField(max_length=255, blank=True, null=True)
    numberType = models.PositiveIntegerField(choices=TELEPHONE_TYPE, default=0)
    isDefault = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number
    
    class Meta:
        abstract = True

class ContactTelephone(TelephoneNumber):
    contact = models.ForeignKey(Contact)
    
    @models.permalink
    def get_absolute_url(self):
        return('contacts.views.telephone_detail', [str(self.id)])

class CompanyTelephone(TelephoneNumber):
    company = models.ForeignKey(Company)
    
    @models.permalink
    def get_absolute_url(self):
        return('companies.views.telephone_detail', [str(self.id)])

class Email(models.Model):
    email = models.EmailField()
    isDefault = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.email

class ContactEmail(Email):
    contact = models.ForeignKey(Contact)
    
    @models.permalink
    def get_absolute_url(self):
        return('contacts.views.email_detail', [str(self.id)])

class CompanyEmail(Email):
    company = models.ForeignKey(Company)
    
    @models.permalink
    def get_absolute_url(self):
        return('companies.views.email_detail', [str(self.id)])