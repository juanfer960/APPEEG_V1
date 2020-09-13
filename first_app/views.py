from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Prediction
from . import forms
from first_app.forms import NewUserForm,FormName,FormSearch
import pickle
from sklearn import svm
from sklearn.metrics import classification_report
from django.core.files.storage import FileSystemStorage


import pandas as pd
import numpy as np

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    form = NewUserForm()
    from_2 = FormSearch()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['name']
            password = form.cleaned_data['password']

            predictions_0 = Prediction.objects.filter(prediction = '0')[:3]
            predictions_1 = Prediction.objects.filter(prediction = '1')[:3]
            predictions_2 = Prediction.objects.filter(prediction = '2')[:3]

            temp = []
            dataRes_1 = []
            dataRes_2 = []
            dataRes_3 = []

            for prediction in predictions_0:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente" + prediction.patiente_age)
                    temp.append("Fecha Análisis" + prediction.analysis_date)

                    dataRes_1.append(temp.copy())
                    temp.clear()
                except:
                    print('error')
             
            for prediction in predictions_1:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente" + prediction.patiente_age)
                    temp.append("Fecha Análisis" + prediction.analysis_date)

                    dataRes_2.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_2:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente" + prediction.patiente_age)
                    temp.append("Fecha Análisis" + prediction.analysis_date)

                    dataRes_3.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            dataRes = {'form':from_2, 'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

            if userValid(user,password):
                return  render(request,'basicapp/workPage.html',context=dataRes)

            else:
                data = {'user': 'null', 'password': 'null'}
                form = NewUserForm(data)
              

                return render(request,'basicapp/pageError.html')

    return render(request,'basicapp/login.html',{'form':form})


def logup(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)
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

    form = FormSearch()

    prediction_result = 3

    predictions_0 = Prediction.objects.filter(prediction = '0')[:prediction_result]
    predictions_1 = Prediction.objects.filter(prediction = '1')[:prediction_result]
    predictions_2 = Prediction.objects.filter(prediction = '2')[:prediction_result]

    temp = []
    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []

    for prediction in predictions_0:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)

            dataRes_1.append(temp.copy())
            temp.clear()
        except:
            print('error')

    for prediction in predictions_1:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)

            dataRes_2.append(temp.copy())
            temp.clear()
        except:
            print('error')

    for prediction in predictions_2:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)

            dataRes_3.append(temp.copy())
            temp.clear()
        except:
            print('error')
       

    dataRes = {'form':form,'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def fileSerch(request,**kwargs):

    user=kwargs['user']
    password=kwargs['password']
    paciente=kwargs['paciente']
    edad=kwargs['edad']

    print(paciente)
    print(edad)

    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        dataRes = {'user': user, 'password': user, 'URL': 'El archivo se cargo correctamente en: ' + url}

    return  render(request,'basicapp/search.html',context=dataRes)
    

def eegSerch(request,**kwargs):

    form = forms.FormSearch()

    dataRes_  = []

    temp = []

    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []

    user=kwargs['user']
    password=kwargs['password']

    if request.method == 'POST':
        form = forms.FormSearch(request.POST)

        if form.is_valid():

            doctor = form.cleaned_data['doctor']
            paciente = form.cleaned_data['paciente']

            prediction_result =  3

           
            predictions_0 = Prediction.objects.filter(prediction = '0', patinte_id = paciente, user_id = doctor)[:prediction_result]
            predictions_1 = Prediction.objects.filter(prediction = '1', patinte_id = paciente, user_id = doctor)[:prediction_result]
            predictions_2 = Prediction.objects.filter(prediction = '2', patinte_id = paciente, user_id = doctor)[:prediction_result]

            for prediction in predictions_0:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)

                    dataRes_1.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_1:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)

                    dataRes_2.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_2:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)

                    dataRes_3.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            dataRes = {'form':form, 'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

        return  render(request,'basicapp/workPage.html',context=dataRes)
         

   

    












