"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


class ContactTest (TestCase):
    def testContactBasicInfo(self):
        c = Contact(name='tester')
        self.assertEquals('tester', c.name)

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
            isDefault = 1,
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

