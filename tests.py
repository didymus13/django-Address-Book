"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import *

class ContactTest (TestCase):
    def testContactBasicInfo(self):
        c = Contact(firstname='mistah', lastname='testah')
        self.assertEquals('mistah', c.firstname)
        self.assertEquals('testah', c.lastname)
        
    def testContactApiBasicList(self):
        c = Client()
        response = c.get('/addressbook/api/contacts/')
        self.assertContains(response.content, 'tester')

class AddressTest (TestCase):
    def testAddressBasicInfo(self):
        c = Contact(name='tester')
        a = Address(
            contact = c,
            addressType = 0,
            street1 = '123 fake st',
            street2 = 'po box 234',
            street3 = 'station abc',
            city = 'Testville',
            region = 'testprovince',
            country = 'canada',
            postalCode = 'H0H0H0',
            isDefault = True,
        )
        self.assertEquals('tester', a.contact.name)
        self.assertEquals('123 fake st', a.street1)
        self.assertEquals('po box 234', a.street2)
        self.assertEquals('station abc', a.street3)
        self.assertEquals('Testville', a.city)
        self.assertEquals('testprovince', a.region)
        self.assertEquals('canada', a.country)
        self.assertEquals('H0H0H0', a.postalCode)
        self.assertEquals('mailing', a.get_addressType_display())

class TelephoneNumberTest(TestCase):
    def testTelephoneBasicInfo(self):
        c = Contact(name='tester')
        p = TelephoneNumber(
            contact = c, 
            number = '1234567890', 
            extension='123', 
            numberType = 0,
            isDefault = True);
        self.assertEquals('tester', p.contact.name)
        self.assertEquals('1234567890', p.number)
        self.assertEquals('123', p.extension)
        self.assertEquals('telephone', p.get_numberType_display())
        self.assertTrue(p.isDefault)

        p.numberType = 1
        self.assertEquals('fax', p.get_numberType_display())
        
class EmailTest(TestCase):
    def testEmailBasicInfo(self):
        c = Contact(name='tester')
        e = Email(email='example@example.com', contact=c, isDefault=True)
        self.assertEquals('tester', e.contact.name);
        self.assertEquals('example@example.com', e.email)
        self.assertTrue(e.isDefault)
