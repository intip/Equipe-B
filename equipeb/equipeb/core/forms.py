#coding: utf8

from django import forms
from equipeb.core.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription

