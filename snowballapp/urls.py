from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/debts')),
    path('debts',views.debts, name='home'),
    path('repayments', views.repayments, name='repayments'),
    path('altrepayments', views.altrepayments, name='altrepayments')
]