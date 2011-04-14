"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import *
import simplejson

class CompanyTest (TestCase):   
    
    def setUp(self):
        self.c = Company(name='test corp')
        self.c.save()
        self.client = Client()
    
    def testAssociateAddress(self):
        a = CompanyAddress()
        a.street1 = '1234 fake street'
        a.city = 'fakeville'
        a.region = 'fake prov'
        a.country = 'fake country'
        a.postalCode = 'H0H 0H0'
        a.company = self.c
        a.save()
        
        self.assertEquals(1, self.c.companyaddress_set.count())
        for address in self.c.companyaddress_set.all():
            self.assertEquals(a.street1, address.street1)
    
    def testAssociateTelephone(self):
        t = CompanyTelephone()
        t.number = '1-800-123-4567'
        t.company = self.c
        t.save()
        
        self.assertEquals(1, self.c.companytelephone_set.count())
        for telephone in self.c.companytelephone_set.all():
            self.assertEquals(t.number, telephone.number)
    
    def testAssociateEmail(self):
        e = CompanyEmail()
        e.email = 'example@example.com'
        e.company = self.c
        e.save()
        
        self.assertEquals(1, self.c.companyemail_set.count())
        for email in self.c.companyemail_set.all():
            self.assertEquals(e.email, email.email)
            
    def testCompanyApi(self):
        getResponse = self.client.get('/addressbook/api/company/')
        self.assertContains(getResponse, self.c.name )
        getDetailResponse = self.client.get('/addressbook/api/company/%s/' % (self.c.id, ))
        self.assertContains(getDetailResponse, self.c.name )
    
    def testCompanyTelephoneApi(self):
        t = CompanyTelephone(company=self.c, number='123-456-7890')
        t.save()
        getResponse = self.client.get('/addressbook/api/company/%s/telephone/' % (self.c.id, ))
        self.assertContains(getResponse, t.number) 
        getDetailResponse = self.client.get('/addressbook/api/company/%s/telephone/%s/' % (self.c.id, t.id))
        self.assertContains(getDetailResponse, t.number) 
        
    def testCompanyAddress(self):
        a = CompanyAddress(company=self.c, street1='123 fake st', city='fakeville', 
                           region='fakeprov', country='fakenation', postalCode='12345')
        a.save()
        
        getResponse = self.client.get('/addressbook/api/company/%s/address/' % (self.c.id))
        self.assertContains(getResponse, a.street1)
        getDetailResponse = self.client.get('/addressbook/api/company/%s/address/%s/' % (self.c.id, a.id))
        self.assertContains(getDetailResponse, a.street1)

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