from piston.handler import BaseHandler
from piston.utils import rc, throttle

from addressbook.models import *

class ContactHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Contact
    
    def read(self, request, id=None):
        contacts = Contact.objects.all()
        if id:
            return contacts.get(pk=id)
        return contacts