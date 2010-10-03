from django.contrib import admin
from models import *

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Address, AddressAdmin)

class TelephoneNumberAdmin(admin.ModelAdmin):
    pass
admin.site.register(TelephoneNumber, TelephoneNumberAdmin)

class EmailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Email, EmailAdmin)
