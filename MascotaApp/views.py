from django.shortcuts import render
from MascotaApp import views
from MascotaApp.forms import *
from MascotaApp.models import *
# Create your views here.

def inicio(request):
    #pagina de inicio
    return render(request,"MascotaApp\index.html")

def mascotaFormulario(request):
    # return render(request,"MascotaApp\mascotaFormulario.html")
    if request.method == 'POST':
        miFormulario = MascotaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            mascota = Mascota(nombre=informacion['nombre'], tamaño=informacion['tamaño'], raza = informacion['raza'])
            mascota.save()
            return render(request, "MascotaApp\index.html")
    else:
        miFormulario=MascotaFormulario()

    return render(request, "MascotaApp\mascotaFormulario.html", {"miFormulario":miFormulario})
    
def entrenadorFormulario(request):
    # return render(request,"MascotaApp\entrenadorFormulario.html")
    if request.method == 'POST':
        miFormulario = EntrenadorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entrenador = Entrenador(nombre=informacion['nombre'], edad=informacion['edad'])
            entrenador.save()
            return render(request, "MascotaApp\index.html")
    else:
        miFormulario=EntrenadorFormulario()

    return render(request, "MascotaApp\entrenadorFormulario.html", {"miFormulario":miFormulario})
    
def entrenamientoFormulario(request):
    # return render(request,"MascotaApp\entrenamientoFormulario.html")
    if request.method == 'POST':
        miFormulario = EntrenamientoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entrenamiento = Entrenamiento(curso=informacion['curso'])
            entrenamiento.save()
            return render(request, "MascotaApp\index.html")
    else:
        miFormulario=EntrenamientoFormulario()

    return render(request, "MascotaApp\entrenamientoFormulario.html", {"miFormulario":miFormulario})
    