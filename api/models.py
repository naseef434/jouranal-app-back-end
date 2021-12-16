from django.db import models

# Create your models here.
class Student(models.Model):
   contract_name = models.CharField(max_length=25, null=False, blank=False, unique=True)

   def __str__(self):
        return self.contract_name

class JournalEntry(models.Model):
    entryNumber = models.IntegerField(null=False, blank=False)
    file_name = models.CharField(max_length=100,null=False, blank=False,)
    date = models.DateField(auto_now=False, auto_now_add=False,)
    check_field = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name
 
class Debit(models.Model):
    journalEntry_id = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    account = models.IntegerField(null=False, blank=False, )
    debit = models.IntegerField(null=False, default=0 ,blank=False )
    credit = models.IntegerField(null=False, default=0 ,blank=False )
    discription = models.CharField(max_length=100)

    def __str__(self):
        return self.discription

class Credit(models.Model):
    journalEntry_id = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    account = models.IntegerField(null=False, blank=False, )
    debit = models.IntegerField(null=False, default=0 ,blank=False )
    credit = models.IntegerField(null=False, default=0 ,blank=False )
    discription = models.CharField(max_length=100)

    def __str__(self):
        return self.discription
     