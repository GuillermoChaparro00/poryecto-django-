from re import template
from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns=[


    path("",views.plantilla, name="index"),
    path("alumnos",views.alumnos, name="alumnos"),
    path("profesores",views.profesores, name="profesores"),
    path("cargar_alumno",views.cargar_alumno, name="cargar_alumno"),
    path("buscar_alumno",views.buscar_alumno),
    path("buscar",views.buscar),
    path("cargar_profesores",views.cargar_profesores, name="cargar_profesores"),
    path("cargar_curso",views.cargar_curso, name="cargar_curso"),
    path("cursos",views.cursos, name="cursos"),
    path("eliminar_alumno/<int:id>",views.eliminar_alumno, name="eliminar_alumno"),
    path("editar_alumno/<int:id>",views.editar_alumno, name="editar_alumno"),
    path("editar_alumno",views.editar_alumno, name="editar_alumno"),

    #perfil
    path("perfil",views.perfil, name="perfil"),
    #login
    path("login",views.login_request, name="login"),

    #registro
    path("register",views.register, name="register"),

    #logaut
     path("logout",LogoutView.as_view(template_name="logout.html"), name="logout"),

    #editar perfil
     path("EditarPerfil",views.EditarPerfil, name="EditarPerfil"),
]