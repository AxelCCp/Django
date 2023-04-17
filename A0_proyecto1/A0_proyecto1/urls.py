"""
URL configuration for A0_proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from A0_proyecto1.views import saludo
from A0_proyecto1.views import despedida
from A0_proyecto1.views import dameFecha, calculaEdad, calculaEdad2, saludo2, saludo3, saludo4, saludo5, cursoC, cursoCss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('fecha/', dameFecha),
    path('edades/<int:agno>', calculaEdad),
    path('edades/<int:edad>/<int:agno>', calculaEdad2),
    path('saludo2/', saludo2),
    path('saludo3/', saludo3),
    path('saludo4/', saludo4),
    path('saludo5/', saludo5),
    path('cursoC/', cursoC),
    path('cursoCss/', cursoCss),
]
