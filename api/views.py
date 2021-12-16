from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import JournalEntry,Debit,Credit
#from . serializers import JournalEntrySerializer ,DebitSerilizer, CreditSerializer
from . serializers import *
from rest_framework import generics


# Create your views here.

class JournalEntryView(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    
    def create(self ,request):
        #copy debit array from request .data
        debit = request.data.pop('debit')
        #copy credit array from request .data
        credit = request.data.pop('credit')
        #create journal Entry obj with request .data except debit and credit array
        obj = JournalEntry.objects.create(**request.data)
        
        for item in debit:
            deb_obj = Debit.objects.create(journalEntry_id=obj, **item)
        for item in credit:
            deb_obj = Credit.objects.create(journalEntry_id=obj, **item)
        return Response(data=self.serializer_class(obj).data)

class JournalEntryViewEdit(APIView):
    def patch(self,request,id):
        data = request.data
         #copy debit array from request .data
        debit = data.pop('debit')
        #copy credit array from request .data
        credit =data.pop('credit')
        #update data 
        JournalEntry.objects.filter(id=id).update(**request.data)
        jrnentry = JournalEntry.objects.get(id=id) 
        for item in debit:
            Debit.objects.filter(id=item["id"]).update(**item)
        serializer = JournalEntrySerializerEdit(jrnentry)
        return Response(serializer.data)
        # print(jrnentry.entryNumber)
        # return Response("hello")

class CreatejournalEntry(generics.CreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializerEdit 
    def create(self, request,  **kwargs):
        try:
            response = super().create(request, **kwargs)
            return Response({'status':'success','response_code': 200,'data': response.data})
        except Exception as e:
            message = str(e)     
            return Response({'status':'error','response_code':500,"message":message})    

class DebitView(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerilizer

class CreditView(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
