from django.shortcuts import render
from .models import *
from .forms import *

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "handball_app/home.html")

def about(request):
    return render(request, "handball_app/about.html")


# ___ ************************* USUARIO ****************************************************************

# ___ REGISTRO DE USUARIO

def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(data=request.POST)
        if miForm.is_valid():
            miForm.save()
            return render(request, "handball_app/home.html")
    else:
        miForm = RegistroUsuariosForm()
    return render(request, "handball_app/user_register.html", {"form":miForm})

# ___ LOGGEO DE USUARIO

def loggin_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = 'Ningún avatar encontrado'
                finally:
                    request.session['avatar'] = avatar
                return render(request, "handball_app/home.html")
            else:
                return render(request, "handball_app/user_login.html", {"form":miForm, 'mensaje':f"Usuario y/o contraseña incorrectos."})
        else:
            return render(request, "handball_app/user_login.html", {"form":miForm, 'mensaje':f"Usuario y/o contraseña incorrectos."})

    miForm = AuthenticationForm(request.POST)
    return render(request, "handball_app/user_login.html", {"form":miForm})

# ___ EDICION DE USUARIO
@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            usuario.email = miForm.cleaned_data.get('email')
            usuario.password1 = miForm.cleaned_data.get('password1')
            usuario.password2 = miForm.cleaned_data.get('password2')
            usuario.first_name = miForm.cleaned_data.get('first_name')
            usuario.last_name = miForm.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "handball_app/home.html")
        else:
            return render(request, "handball_app/user_edit.html", {"form":miForm})
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "handball_app/user_edit.html", {"form":miForm})

# ___ EDICION DE AVATAR
@login_required
def editar_avatar(request):
    if request.method == 'POST':
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            # eliminar avatares viejos
            avatar_delete = Avatar.objects.filter(user=usuario)
            if len(avatar_delete) > 0:
                for a in range(len(avatar_delete)):
                    avatar_delete[a].delete()

            # guardar avatar nuevo
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data['imagen'])
            avatar.save()

            # obtiene el url de la imagen y la almacena en session
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, "handball_app/home.html")
    else:
        miForm = AvatarForm()
    return render(request, "handball_app/user_avatar.html", {"form":miForm})

# ___ ************************* ABM ****************************************************************

# ___ ABM JUGADORES

class JugadorList(ListView):
    model = Jugador

class JugadorCreate(LoginRequiredMixin, CreateView):
    model = Jugador
    fields = ['nombre', 'altura', 'fecha_nacimiento', 'nacionalidad', 'club', 'estado_actividad']
    success_url = reverse_lazy('jugadores')

class JugadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jugador
    fields = ['nombre', 'altura', 'fecha_nacimiento', 'nacionalidad', 'club', 'estado_actividad']
    success_url = reverse_lazy('jugadores')

class JugadorDelete(LoginRequiredMixin, DeleteView):
    model = Jugador
    success_url = reverse_lazy('jugadores')

# ___ ABM CLUBES

class ClubesList(ListView):
    model = Club

class ClubesCreate(LoginRequiredMixin, CreateView):
    model = Club
    fields = ['nombre', 'arena', 'liga', 'ciudad', 'pais']
    success_url = reverse_lazy('clubes')

class ClubesUpdate(LoginRequiredMixin, UpdateView):
    model = Club
    fields = ['nombre', 'arena', 'liga', 'ciudad', 'pais']
    success_url = reverse_lazy('clubes')

class ClubesDelete(LoginRequiredMixin, DeleteView):
    model = Club
    success_url = reverse_lazy('clubes')

# ___ ABM LIGAS

class LigasList(ListView):
    model = Liga

class LigasCreate(LoginRequiredMixin, CreateView):
    model = Liga
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('ligas')

class LigasUpdate(LoginRequiredMixin, UpdateView):
    model = Liga
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('ligas')

class LigasDelete(LoginRequiredMixin, DeleteView):
    model = Liga
    success_url = reverse_lazy('ligas')

# ___ ABM ARENAS

class ArenasList(ListView):
    model = Arena

class ArenasCreate(LoginRequiredMixin, CreateView):
    model = Arena
    fields = ['nombre', 'capacidad', 'ciudad', 'pais']
    success_url = reverse_lazy('arenas')

class ArenasUpdate(LoginRequiredMixin, UpdateView):
    model = Arena
    fields = ['nombre', 'capacidad', 'ciudad', 'pais']
    success_url = reverse_lazy('arenas')

class ArenasDelete(LoginRequiredMixin, DeleteView):
    model = Arena
    success_url = reverse_lazy('arenas')


# ___ BUSCADORES

# función que resuelve la busqueda de datos y devuelve los parámetros a pasar a la vista
def buscar(request, modelo, nombe_key):
    if request.GET['buscar']:
        filtro = request.GET['buscar']
        filtrados = modelo.objects.filter(nombre__icontains=filtro)
        if len(filtrados) > 0:
            contexto = {nombe_key: filtrados, 'gotodiv': 'datos', 'filtro_ingresado': f"Filtro ingresado: {filtro}"}
        else:
            contexto = {nombe_key: filtrados, 'gotodiv': 'datos', 'filtro_ingresado':f'Ningún objeto cumple el filtro {filtro}!!!'}
    else:
        contexto = {nombe_key: modelo.objects.all, 'gotodiv': 'datos', 'filtro_ingresado':'Filtro no ingresado!!!'}
    return contexto

# función para cada específica
def jugadores_buscar(request):
    contexto = buscar(request, Jugador, 'jugador_list')
    return render(request, "handball_app/jugador_list.html", contexto)

def clubes_buscar(request):
    contexto = buscar(request, Club, 'club_list')
    return render(request, "handball_app/club_list.html", contexto)

def ligas_buscar(request):
    contexto = buscar(request, Liga, 'liga_list')
    return render(request, "handball_app/liga_list.html", contexto)

def arenas_buscar(request):
    contexto = buscar(request, Arena, 'arena_list')
    return render(request, "handball_app/arena_list.html", contexto)