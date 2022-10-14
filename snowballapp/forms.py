from django import forms
from .models import UsersModel#, Debts

'''
class DebtsForm(forms.ModelForm):
    class Meta:
        model = Debts 
        fields = "__all__"
        exclude = ['recmopmt', 'user']
'''

class UsersForm(forms.ModelForm):
    class Meta:
        model = UsersModel
        fields = ['AvailableMonthlyBudget', 'Principal', 'InterestRate', 'MinimumMonthlyPayment']