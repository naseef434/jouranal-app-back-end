from django.contrib import admin
from . models import Student,JournalEntry,Debit,Credit

# Register your models here.
admin.site.register(Student)
admin.site.register(JournalEntry)
admin.site.register(Debit)
admin.site.register(Credit)