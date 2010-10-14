from piston.handler import BaseHandler
from piston.utils import rc, throttle

from addressbook.models import *

class ContactHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Contact
    fields = ('pk', 'firstname', 'lastname', 
              ('addresses', ('pk', ) ), 
              ('telephoneNumbers', ('pk', ) ), 
              ('emailAddresses', ('pk', ) ),
              )
    
    def read(self, request, contact=None):
        contacts = Contact.objects.all()
        if contact:
            return contacts.get(pk=contact)
        return contacts
    
class AddressHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Address
    
    def read(self, request, contact, address=None):
        if address:
            return Address.objects.get(pk=address)
        return Address.objects.filter(contact=contact)
    
class TelephoneHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = TelephoneNumber
    
    def read(self, request, contact, telephone=None):
        if telephone:
            return TelephoneNumber.objects.get(pk=telephone)
        return TelephoneNumber.objects.filter(contact=contact)

class EmailHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Email
    
    def read(self, request, contact, email=None):
        if email:
            return Email.objects.get(pk=email)
        return Email.objects.filter(contact=contact)