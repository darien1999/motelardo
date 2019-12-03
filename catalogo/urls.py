from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('usuario/<int:pk>/', views.usuarioDetailView.as_view(),name='usuario-detail'),
]
urlpatterns +=[
   path('usuario/create/', views.usuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/<int:pk>/update/', views.usuarioUpdate.as_view(), name='usuario-update'),
    path('usuario/<int:pk>/delete/', views.usuarioDelete.as_view(), name='usuario-delete'),
    path('usuarios/', views.usuarioListView.as_view(), name='usuario_list'),
    path ('principal/', views.principal, name='principal'),
    path('registro/', views.registro, name='registro')
]