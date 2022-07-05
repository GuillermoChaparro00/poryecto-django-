import re
from unittest import loader
import django
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Personas , Profesores , Curso
 
from django.template import loader
from app_coder.forms import Alumnos_formulario,  Curso_formulario , EditarFormUsuario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required










def plantilla(request):
    return render(request, "plantilla.html")

##ALUMNOOS
def alumnos(request):
    los_alumnos=Personas.objects.all()
    diccionario={"alumnos": los_alumnos}
    platilla=loader.get_template("alumnos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)

def cargar_alumno(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            persona= Personas(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            persona.save()
    return render(request, "cargar_alumno.html")


def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"] 
        alumnos=Personas.objects.filter(nombre__icontains =nombre)
        return render(request,"resultado_busqueda.html",{"alumnos":alumnos})
    else:
        return HttpResponse("campo vacio")

@login_required
def eliminar_alumno(request,id):
    alumno=Personas.objects.get(id=id)
    alumno.delete()

    alumno=Personas.objects.all()
    return render(request,"alumnos.html",{"alumnos":alumno})

@login_required
def editar_alumno(request,id):
    alumno=Personas.objects.get(id=id)

    if request.method=="POST":
        mi_fomulario=Alumnos_formulario(request.POST)

        if mi_fomulario.is_valid():
            datos=mi_fomulario.cleaned_data
            alumno.nombre=datos["nombre"]
            alumno.apellido=datos["apellido"]
            alumno.dni=datos["dni"]
            alumno.edad=datos["edad"]
            alumno.nacimiento=datos["nacimiento"]
            alumno.save()
            return HttpResponse("listo")
        else:
            mi_fomulario=Alumnos_formulario(initial={"nombre":alumno.nombre,"apellido":alumno.apellido,"dni":alumno.dni,"edad":alumno.edad,"nacimiento":alumno.nacimiento})

        return render(request, "editar_alumno.html",{"mi_formulario":mi_fomulario, "alumno":alumno})
    
##fin alumnos


##PROFESORES 
@login_required
def cargar_profesores(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            Profe= Profesores(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            Profe.save()
    return render(request, "cargar_profesores.html")

def profesores(request):
    los_profes=Profesores.objects.all()
    diccionario={"profesores": los_profes}
    platilla=loader.get_template("profesores.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)  

##FIN PROFESORES

##CURSOS
@login_required
def cargar_curso(request):
    if request.method=="POST":
        validacionForm= Curso_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            cursos= Curso(nombre= datos["nombre"],camada=datos["camada"],turno=datos["turno"])
            cursos.save()
    return render(request, "cargar_curso.html")

def cursos(request):
    los_cursos=Curso.objects.all()
    diccionario={"cursos": los_cursos}
    platilla=loader.get_template("cursos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)  
##FIN CURSOS



##INICIO LOGIN

def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user=authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                return render(request,"inicio.html", {"mensaje": f"bienvenido {usuario}"})
            else:
                return HttpResponse("usuario incorrecto")
        else:
            return HttpResponse(f"Form incorrecto {form}")

    form=  AuthenticationForm()
    return render (request, "login.html", {"form":form})

##FIN LOGIN


##inicio registro

def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("usuario creado")


    else:
        form=UserCreationForm()
    return render(request, "registro.html", {"form":form})

##fin registro

##editar perfil
@login_required
def EditarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        miFormulario=EditarFormUsuario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.changed_data
            usuario.email=informacion['email']
            password=informacion['password']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")



    else:
        miFormulario=EditarFormUsuario(initial={'emial': usuario.email})
        return render(request, "editar_perfil.html",{"miFormulario":miFormulario, "usuario":usuario})

##fin editar perfil

##perfil
@login_required
def perfil(request):
    return render(request, "inicio.html")