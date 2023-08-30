from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),

    path('user_login', loggin_request, name='user_login'),
    path('user_logout', LogoutView.as_view(template_name="handball_app/home.html"), name='user_logout'),
    path('user_register', register, name='user_register'),
    path('user_edit', editar_usuario, name='user_edit'),
    path('user_avatar', editar_avatar, name='user_avatar'),

    path('jugadores/', JugadorList.as_view(), name='jugadores'),
    path('create_jugadores/', JugadorCreate.as_view(), name='create_jugadores'),
    path('update_jugadores/<int:pk>', JugadorUpdate.as_view(), name='update_jugadores'),
    path('delete_jugadores/<int:pk>', JugadorDelete.as_view(), name='delete_jugadores'),

    path('clubes/', ClubesList.as_view(), name='clubes'),
    path('create_clubes/', ClubesCreate.as_view(), name='create_clubes'),
    path('update_clubes/<int:pk>', ClubesUpdate.as_view(), name='update_clubes'),
    path('delete_clubes/<int:pk>', ClubesDelete.as_view(), name='delete_clubes'),
    
    path('ligas/', LigasList.as_view(), name='ligas'),
    path('create_ligas/', LigasCreate.as_view(), name='create_ligas'),
    path('update_ligas/<int:pk>', LigasUpdate.as_view(), name='update_ligas'),
    path('delete_ligas/<int:pk>', LigasDelete.as_view(), name='delete_ligas'),

    path('arenas/', ArenasList.as_view(), name='arenas'),
    path('create_arenas/', ArenasCreate.as_view(), name='create_arenas'),
    path('update_arenas/<int:pk>', ArenasUpdate.as_view(), name='update_arenas'),
    path('delete_arenas/<int:pk>', ArenasDelete.as_view(), name='delete_arenas'),

    path('jugadoresBuscar/', jugadores_buscar, name='jugadoresBuscar'),
    path('clubesBuscar/', clubes_buscar, name='clubesBuscar'),
    path('ligasBuscar/', ligas_buscar, name='ligasBuscar'),
    path('arenasBuscar/', arenas_buscar, name='arenasBuscar'),
]
