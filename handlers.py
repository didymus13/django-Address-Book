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

class CompanyHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ()
    model = Company
    
    def read(self, request, company_id=None):
        company = Company.objects
        if company_id:
            return company.get(pk=company_id)
        return company.all()

class CompanyTelephoneHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ()
    model = CompanyTelephone
    
    def read(self, request, company_id, telephone_id=None):
        company = Company.objects.get(pk=company_id)
        tel = CompanyTelephone.objects
        if telephone_id:
            return tel.get(pk=telephone_id)
        return tel.filter(company = company)

class CompanyAddressHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ()
    model = CompanyAddress
    
    def read(self, request, company_id, address_id=None):
        company = Company.objects.get(pk=company_id)
        address = CompanyAddress.objects
        if address_id:
            return address.get(pk=address_id)
        return address.filter(company = company)
    
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