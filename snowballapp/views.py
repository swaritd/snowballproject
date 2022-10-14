from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import UsersModel
from .forms import UsersForm

def debts(request):
    if request.method == 'POST':
        users_form = UsersForm(request.POST)
        if users_form.is_valid():
            users_form.save()
            messages.success(request, ("Saved."))
        else:
            messages.error(request, ("Error."))

        return redirect("/debts")
    users_form = UsersForm()
    users = UsersModel.objects.all()

    return render(request=request, template_name="debtspage.html", context={'users_form':users_form, 'users':users})
     

def repayments(request):
    usersqs = UsersModel.objects.all()
    totalinterest = 0
    minpmt = 0
    intrt = 0
    principal = 0
    if usersqs.exists():
        msg = "Your Repayments: "
        for x in usersqs:
            totalinterest += x.Principal * ((x.InterestRate)/100)
            principal += x.Principal
            minpmt += x.MinimumMonthlyPayment
            totalcashleft = x.AvailableMonthlyBudget - minpmt
            if x.InterestRate > intrt:
                intrt = x.InterestRate
                owed = x.Principal * (1+((x.InterestRate)/100))
                withextrapay = (x.MinimumMonthlyPayment + (totalcashleft-x.MinimumMonthlyPayment))
                term = owed/withextrapay

        totalcashleft = x.AvailableMonthlyBudget - minpmt
        due = principal + totalinterest
        
    else:
        msg = "Please go back and enter a debt to continue"
        totalinterest = "N/A"
        minpmt = "N/A"
        intrt = "N/A"
        term = "N/A"
        totalcashleft = "N/A"
        principal = "N/A"
        due = "N/A"


    return render(request, 'repaymentspage.html', {"msg":msg,"totalinterest":totalinterest,"minpmt":minpmt, "intrt":intrt, "term":term, "totalcashleft":totalcashleft, "principal":principal, "due":due})



def altrepayments(request):
    users = list(UsersModel.objects.all())
    usersqs = list(users)
    length = len(usersqs)
    item = usersqs[0].Principal

    if len(usersqs) > 0:
        msg = "Your Repayments: "


        def answer(x):

            totalinterest = 0
            totalprincipal = 0
            totalminpmt = 0

            intrt = 0

            totalinterest += x.Principal * ((x.InterestRate)/100)
            totalprincipal += x.Principal
            totalminpmt += x.MinimumMonthlyPayment
            if x.InterestRate > intrt:
                intrt = x.InterestRate
                owed = x.Principal * (1+((x.InterestRate)/100))
                withextrapay = (x.MinimumMonthlyPayment + (x.AvailableMonthlyBudget-x.MinimumMonthlyPayment))
                term = owed/withextrapay

            totalcashleft = x.AvailableMonthlyBudget - totalminpmt
            due = totalprincipal + totalinterest

            return render(request, 'repaymentspage.html', {"msg":msg,"totalinterest":totalinterest,"totalminpmt":totalminpmt, "intrt":intrt, "term":term, "totalcashleft":totalcashleft, "totalprincipal":totalprincipal, "due":due})

        counter = 0
        while counter < length:
            thisobject = usersqs[counter]
            result = map(answer, thisobject)
            counter += 1
        
    else:
        msg = "Please go back and enter a debt to continue"
        totalinterest = 0
        totalminpmt = 0
        intrt = 0
        term = 0
        totalcashleft = 0
        totalprincipal = 0
        due = 0

        return render(request, 'repaymentspage.html', {"msg":msg,"totalinterest":totalinterest,"totalminpmt":totalminpmt, "intrt":intrt, "term":term, "totalcashleft":totalcashleft, "totalprincipal":totalprincipal, "due":due})

    msg = "didnt work:("
    return render(request, 'repaymentspage.html', {"msg":item})