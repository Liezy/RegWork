from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
]