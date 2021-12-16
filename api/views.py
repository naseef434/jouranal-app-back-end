from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . models import JournalEntry,Debit,Credit
from . serializers import JournalEntrySerializer ,DebitSerilizer, CreditSerializer
# Create your views here.

class JournalEntryView(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    
    def create(self ,request):
        debit = request.data.pop('debit')
        credit = request.data.pop('credit')
        obj = JournalEntry.objects.create(**request.data)
        for item in debit:
            deb_obj = Debit.objects.create(journalEntry_id=obj, **item)
        for item in credit:
            deb_obj = Credit.objects.create(journalEntry_id=obj, **item)
        return Response(data=self.serializer_class(obj).data)

class DebitView(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerilizer

class CreditView(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
