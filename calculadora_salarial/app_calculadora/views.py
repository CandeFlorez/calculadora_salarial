from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')
def calculadora(request):
    pensionSalud = 0
    pensionObligatoria = 0
    auxilioTransporte = 0
    pagoNeto = 0
    ingresoTotal = 0
    sueldo = 0
    tiempo = 2

    try:
        if request.method=="POST":
            sueldo = eval(request.POST.get('sueldo'))
            tiempo = eval(request.POST.get('tiempo'))

            pensionSalud = sueldo * 0.04
            pensionObligatoria = sueldo * 0.04
            auxilioTransporte = 117172 if sueldo <= 2000000 else 0
            pagoNeto = sueldo - pensionSalud - pensionObligatoria + auxilioTransporte
            ingresoTotal = sueldo + auxilioTransporte

            if tiempo == 1:
                pensionSalud = pensionSalud * 12
                pensionObligatoria = pensionObligatoria * 12
                auxilioTransporte = auxilioTransporte * 12
                ingresoTotal = ingresoTotal * 12
                pagoNeto = pagoNeto * 12
            
            if tiempo == 3:
                pensionSalud = pensionSalud * 0.5
                pensionObligatoria = pensionObligatoria * 0.5
                auxilioTransporte = auxilioTransporte * 0.5
                ingresoTotal = ingresoTotal * 0.5
                pagoNeto = pagoNeto * 0.5
            
            if tiempo == 4:
                pensionSalud = pensionSalud * 0.25
                pensionObligatoria = pensionObligatoria * 0.25
                auxilioTransporte = auxilioTransporte * 0.25
                ingresoTotal = ingresoTotal * 0.25
                pagoNeto = pagoNeto * 0.25
            
            if tiempo == 5:
                pensionSalud = pensionSalud * 0.03
                pensionObligatoria = pensionObligatoria * 0.03
                auxilioTransporte = auxilioTransporte * 0.03
                ingresoTotal = ingresoTotal * 0.03
                pagoNeto = pagoNeto * 0.03

            if tiempo == 6:
                pensionSalud = pensionSalud * 0.013
                pensionObligatoria = pensionObligatoria * 0.013
                auxilioTransporte = auxilioTransporte * 0.013
                ingresoTotal = ingresoTotal * 0.013
                pagoNeto = pagoNeto * 0.013
    
    except:
        print()

    return render(request, 'pages/calculadora.html',{'sueldo':sueldo,'tiempo':tiempo, 'pensionSalud':pensionSalud, 'pensionObligatoria':pensionObligatoria, 'auxilioTransporte':auxilioTransporte, 'pagoNeto':pagoNeto, 'ingresoTotal':ingresoTotal})