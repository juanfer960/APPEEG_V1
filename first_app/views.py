from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import forms
from first_app.forms import NewUserForm,FormName
import pickle
from sklearn import svm
from sklearn.metrics import classification_report


import pandas as pd
import numpy as np

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            password = form.cleaned_data['password']

            con = 1
            dataRes_1 = []
            dataRes_2 = []
            dataRes_3 = []
            dataRes_4 = []
            dataRes_5 = []
            dataRes_6 = []

            dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,'dataRes_cuatro':dataRes_4,'dataRes_cinco':dataRes_5,'dataRes_seis':dataRes_6}

            if userValid(user,password):
                return  render(request,'basicapp/workPage.html',context=dataRes)

            else:
                data = {'user': 'null', 'password': 'null'}
                form = NewUserForm(data)
                form.is_valid()

                return render(request,'basicapp/pageError.html')

    return render(request,'basicapp/login.html',{'form':form})


def logup(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'basicapp/successPage.html')
        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/logup.html',{'form':form})


def userValid (user, password):
    try:
        User.objects.get(user = user, password =  password)
        print(User)
    except:
        return False

    return True


def singout(request):
    return render(request,'index.html')


def search(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']
    dataRes = {'user': user, 'password': password}

    return  render(request,'basicapp/search.html',context=dataRes)


def search(request,**kwargs):
    form = forms.FormSearch()

    user = kwargs['user']
    password = kwargs['password']
    dataRes = {'user': user, 'password': password,'form':form}

    return  render(request,'basicapp/search.html',context=dataRes)


def home(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']

    con = 1
    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []
    dataRes_4 = []
    dataRes_5 = []
    dataRes_6 = []

    dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,'dataRes_cuatro':dataRes_4,'dataRes_cinco':dataRes_5,'dataRes_seis':dataRes_6}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def modelItemitem(id_user):
    
    dataRes = []

    try:
        return ItemItem.objects.filter(user_id = id_user)[:10]
    except: 
        return dataRes


def analysis(request,**kwargs):

    user=kwargs['user']
    password=kwargs['password']

    dataRes_Name = []
    dataRes_city = []
    dataRes_adreesss = []
    dataRes_score = []
    
    dataRes = {'user': user, 'password': password,'dataRes_artistName':dataRes_Name,'dataRes_city':dataRes_city,'dataRes_artistId':dataRes_adreesss,'dataRes_prediction':dataRes_score}
    return  render(request,'basicapp/analysis.html',context=dataRes)


def songSerch(request,**kwargs):
    form = forms.FormSearch()
    dataRes_  = []
    user=kwargs['user']
    password=kwargs['password']
    dataRes = {}

    return  render(request,'basicapp/search.html',context=dataRes)









