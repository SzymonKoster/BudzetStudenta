from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from matplotlib.style import context
from .models import EntertainmentInfo, ExpenseInfo,SavingsInfo, StudyInfo, TravelsInfo
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
import matplotlib.pyplot as plt
from django.db.models import Q
# Create your views here.


def index(request):
    expense_items = ExpenseInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0), default=0))
        expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expenses=Sum('cost',filter=Q(cost__lt=0), default=0))
        fig,ax=plt.subplots()
        ax.bar(['Wydatki','Zarobki'], [abs(expense_total['expenses']),budget_total['budget']],color=['red','green'])
        ax.set_title('Twoje całkowite wydatki  vs  Twoje całkowite zarobki')
        plt.savefig('budget_app/static/budget_app/expense.jpg')
    except TypeError:
        print('No data.')
    context = {'expense_items':expense_items,'budget':budget_total['budget'],'expenses':abs(expense_total['expenses'])}
    return render(request,'budget_app/index.html',context=context)

def add_item(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('app')

def remove_item(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    record = ExpenseInfo.objects.get(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    record.delete()
    return HttpResponseRedirect('app')

def edit_item(request):
    name = request.POST['expense_name']
    new_name = request.POST['expense_name']
    new_expense_cost = request.POST['cost']
    new_expense_date = request.POST['expense_date']
    record = ExpenseInfo.objects.filter(user_expense=request.user).filter(expense_name=name)
    record.expense_name=new_name
    record.cost=new_expense_cost
    record.date_added=new_expense_date
    record.update()
    # record.update(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user )
    return HttpResponseRedirect('app')    






def entertainment_view(request):
    entertainment_items = EntertainmentInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        entertainment_total = EntertainmentInfo.objects.filter(user_expense=request.user).aggregate(entertainment=Sum('cost',filter=Q(cost__gt=0), default=0))
        fig,ax=plt.subplots()
        ax.bar(['Rozrywka'], [abs(entertainment_total['entertainment'])],color=['violet'])
        ax.set_title('Twoje całkowite koszty związane z rozrywką')
        plt.savefig('budget_app/static/budget_app/entertainment.jpg')
    except TypeError:
        print('No data.')
    context = {'entertainment_item':entertainment_items,'entertainment':entertainment_total['entertainment']}
    return render(request,'budget_app/entertainment.html',context=context)

def add_entertainment(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    EntertainmentInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('entertainment')


def remove_entertainment(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    record = EntertainmentInfo.objects.get(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    record.delete()
    return HttpResponseRedirect('entertainment')

def edit_entertainment(request):
    name = request.POST['expense_name']
    new_name = request.POST['expense_name']
    new_expense_cost = request.POST['cost']
    new_expense_date = request.POST['expense_date']
    record = EntertainmentInfo.objects.filter(user_expense=request.user).filter(expense_name=name)
    record.expense_name=new_name
    record.cost=new_expense_cost
    record.date_added=new_expense_date
    record.update()
    # record.update(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user )
    return HttpResponseRedirect('entertainment') 










def study_view(request):
    study_items = StudyInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        study_total = StudyInfo.objects.filter(user_expense=request.user).aggregate(study=Sum('cost',filter=Q(cost__gt=0), default=0))
        fig,ax=plt.subplots()
        ax.bar(['Nauka'], [abs(study_total['study'])],color=['pink'])
        ax.set_title('Twoje całkowite koszty związane z nauką')
        plt.savefig('budget_app/static/budget_app/study.jpg')
    except TypeError:
        print('No data.')
    context = {'study_item':study_items,'study':study_total['study']}
    return render(request,'budget_app/study.html',context=context)

def add_study(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    StudyInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('study')

def remove_study(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    record = StudyInfo.objects.get(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    record.delete()
    return HttpResponseRedirect('study')

def edit_study(request):
    name = request.POST['expense_name']
    new_name = request.POST['expense_name']
    new_expense_cost = request.POST['cost']
    new_expense_date = request.POST['expense_date']
    record = StudyInfo.objects.filter(user_expense=request.user).filter(expense_name=name)
    record.expense_name=new_name
    record.cost=new_expense_cost
    record.date_added=new_expense_date
    record.update()
    # record.update(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user )
    return HttpResponseRedirect('study') 






def travel_view(request):
    travels_items = TravelsInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        travels_total = TravelsInfo.objects.filter(user_expense=request.user).aggregate(travels=Sum('cost',filter=Q(cost__gt=0), default=0))
        fig,ax=plt.subplots()
        ax.bar(['Podróże'], [abs(travels_total['travels'])],color=['orange'])
        ax.set_title('Twoje całkowite koszty podróży')
        plt.savefig('budget_app/static/budget_app/travel.jpg')
    except TypeError:
        print('No data.')
    context = {'travel_item':travels_items,'travels':travels_total['travels']}
    return render(request,'budget_app/travel.html',context=context)

def add_travel(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    TravelsInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('travel')

def remove_travel(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    record = TravelsInfo.objects.get(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    record.delete()
    return HttpResponseRedirect('travel')

def edit_travel(request):
    name = request.POST['expense_name']
    new_name = request.POST['expense_name']
    new_expense_cost = request.POST['cost']
    new_expense_date = request.POST['expense_date']
    record = TravelsInfo.objects.filter(user_expense=request.user).filter(expense_name=name)
    record.expense_name=new_name
    record.cost=new_expense_cost
    record.date_added=new_expense_date
    record.update()
    # record.update(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user )
    return HttpResponseRedirect('travel') 








def savings_view(request):
    savings_items = SavingsInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        savings_total = SavingsInfo.objects.filter(user_expense=request.user).aggregate(savings=Sum('cost',filter=Q(cost__gt=0), default=0))
        fig,ax=plt.subplots()
        ax.bar(['Oszczędności'], [abs(savings_total['savings'])],color=['yellow'])
        ax.set_title('Twoje całkowite oszczędności')
        plt.savefig('budget_app/static/budget_app/savings.jpg')
    except TypeError:
        print('No data.')
    context = {'savings_item':savings_items,'savings':savings_total['savings']}
    return render(request,'budget_app/savings.html',context=context)


def add_savings(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    SavingsInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('savings')


def remove_savings(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    record = SavingsInfo.objects.get(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    record.delete()
    return HttpResponseRedirect('savings')

def edit_savings(request):
    name = request.POST['expense_name']
    new_name = request.POST['expense_name']
    new_expense_cost = request.POST['cost']
    new_expense_date = request.POST['expense_date']
    record = SavingsInfo.objects.filter(user_expense=request.user).filter(expense_name=name)
    record.expense_name=new_name
    record.cost=new_expense_cost
    record.date_added=new_expense_date
    record.update()
    # record.update(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user )
    return HttpResponseRedirect('savings') 






def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponseRedirect('app')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    else:
        form = UserCreationForm
    return render(request,'budget_app/sign_up.html',{'form':form})
