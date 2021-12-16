from django.contrib import admin
from django.urls import path,include
#from . import views
from . views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('journal', JournalEntryView)
router.register('debit', DebitView)
router.register('credit', CreditView)
# router.register('journal-edit/<int:id>', JournalEntryViewEdit)


urlpatterns = [
    path('api/', include(router.urls)),
    path('journal-edit/<int:id>', JournalEntryViewEdit.as_view()),
    path('create-journal-entry',CreatejournalEntry.as_view())
#     path('create-static-group',CreateStaticGroup.as_view(),name="create-static-group"),
# 
]