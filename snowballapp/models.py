from django.db import models

class UsersModel(models.Model):
    AvailableMonthlyBudget = models.IntegerField(help_text="", null=True)
    Principal = models.IntegerField(help_text="", null=True)
    InterestRate = models.IntegerField(help_text="", null=True)
    MinimumMonthlyPayment = models.IntegerField(help_text="", null=True)
    
    #def __str__(self):
    #    return self.AvailableMonthlyBudget

'''
class Debts(models.Model):
    user = models.ForeignKey("snowballapp.Users", verbose_name=("users"), on_delete=models.CASCADE)
    principal = models.IntegerField(help_text="Enter the principal amount for this debt.")
    interest = models.IntegerField(help_text="Enter the interest rate for this debt.")
    minmopmt = models.IntegerField(help_text="Enter the minimum monthly payment required for this debt.")
    recmopmt = models.IntegerField(null=True)

    def __str__(self):
        return self.principal
'''