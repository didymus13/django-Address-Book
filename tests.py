"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import *

class CompanyTest (TestCase):
    
    def testCompanyCreate(self):
        c = Company()
        c.name = 'test corp'
        c.save()
        
        c2 = Company.objects.get(pk=c.id)
        self.assertEquals(c.name, c2.name)
    
    def testAssociateAddress(self):
        c = Company()
        c.name = 'test corp'
        c.save()
        
        a = CompanyAddress()
        a.street1 = '1234 fake street'
        a.city = 'fakeville'
        a.region = 'fake prov'
        a.country = 'fake country'
        a.postalCode = 'H0H 0H0'
        a.company = c
        a.save()
        
        self.assertEquals(1, c.companyaddress_set.count())
        for address in c.companyaddress_set.all():
            self.assertEquals(a.street1, address.street1)
    
    def testAssociateTelephone(self):
        c = Company()
        c.name = 'test corp';
        c.save()
        
        t = CompanyTelephone()
        t.number = '1-800-123-4567'
        t.company = c
        t.save()
        
        self.assertEquals(1, c.companytelephone_set.count())
        for telephone in c.companytelephone_set.all():
            self.assertEquals(t.number, telephone.number)
    
    def testAssociateEmail(self):
        c = Company()
        c.name = 'test corp'
        c.save()
        
        e = CompanyEmail()
        e.email = 'example@example.com'
        e.company = c
        e.save()
        
        self.assertEquals(1, c.companyemail_set.count())
        for email in c.companyemail_set.all():
            self.assertEquals(e.email, email.email)

class ContactTest (TestCase):
    def testContactCreate(self):
        c = Contact()
        c.firstname = 'mister'
        c.lastname = 'tester'
        c.save()
        
        c2 = Contact.objects.get(pk=c.id)
        self.assertEquals(c.firstname, c2.firstname)
        self.assertEquals(c.lastname, c2.lastname)
    
    def testAssociateAddress(self):
        c = Contact()
        c.firstname = 'mister'
        c.lastname = 'tester'
        c.save()
        
        a = ContactAddress()
        a.street1 = '1234 fake street'
        a.city = 'fakeville'
        a.region = 'fake prov'
        a.country = 'fake country'
        a.postalCode = 'H0H 0H0'
        a.contact = c
        a.save()
        
        self.assertEquals(1, c.contactaddress_set.count())
        for address in c.contactaddress_set.all():
            self.assertEquals(a.street1, address.street1)
    
    def testAssociateTelephone(self):
        c = Contact()
        c.firstname = 'mister'
        c.lastname = 'tester'
        c.save()
        
        t = ContactTelephone()
        t.number = '1-800-123-4567'
        t.contact = c
        t.save()
        
        self.assertEquals(1, c.contacttelephone_set.count())
        for telephone in c.contacttelephone_set.all():
            self.assertEquals(t.number, telephone.number)
    
    def testAssociateEmail(self):
        c = Contact()
        c.firstname = 'mister'
        c.lastname = 'tester'
        c.save()
        
        e = ContactEmail()
        e.email = 'example@example.com'
        e.contact = c
        e.save()
        
        self.assertEquals(1, c.contactemail_set.count())
        for email in c.contactemail_set.all():
            self.assertEquals(e.email, email.email)