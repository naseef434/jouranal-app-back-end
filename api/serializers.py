from rest_framework import serializers
from . models import JournalEntry,Debit,Credit


class JournalEntrySerializer(serializers.ModelSerializer):
    debit = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    class Meta:
        model = JournalEntry
        fields = '__all__'

    def get_debit(self, obj):
        debits = obj.debit_set.all()
        return DebitSerilizer(debits, many=True).data

    def get_credit(self, obj):
        debits = obj.credit_set.all()
        return CreditSerializer(debits, many=True).data

class DebitSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = '__all__'

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'
