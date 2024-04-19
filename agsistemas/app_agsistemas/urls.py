from django.urls import path
from .views import (PaginaInicialView, VeiculosView, CriarVeiculoView,
                    EditarVeiculoView, ExcluirVeiculoView, MotoristasView, CriarMotoristaView,
                     ExcluirMotoristaView, EditarMotoristaView, MotoristaDetailView, ControleCreateView, VeiculoDetailView, ControleDeleteView, ControleDetailView, ControleUpdateView, ControleListView)

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='pagina_inicial'),
    path('veiculos/', VeiculosView.as_view(), name='veiculos'),
    path('veiculos/criar/', CriarVeiculoView.as_view(), name='criar_veiculo'),
    path('veiculos/<int:veiculo_id>/editar/', EditarVeiculoView.as_view(), name='editar_veiculo'),
    path('veiculos/<int:veiculo_id>/excluir/', ExcluirVeiculoView.as_view(), name='excluir_veiculo'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo_detail'),
    path('motoristas/', MotoristasView.as_view(), name='motoristas'),
    path('motoristas/criar/', CriarMotoristaView.as_view(), name='criar_motorista'),
    path('motoristas/<int:motorista_id>/excluir/', ExcluirMotoristaView.as_view(), name='excluir_motorista'),
    path('motoristas/<int:motorista_id>/editar/', EditarMotoristaView.as_view(), name='editar_motorista'),
    path('motoristas/<int:pk>/', MotoristaDetailView.as_view(), name='motorista_detail'),
    path('controle/', ControleListView.as_view(), name='controle_list'),
    path('controle/<int:pk>/', ControleDetailView.as_view(), name='controle_detail'),
    path('controle/create/', ControleCreateView.as_view(), name='controle_create'),
    path('controle/<int:pk>/update/', ControleUpdateView.as_view(), name='controle_update'),
    path('controle/<int:pk>/delete/', ControleDeleteView.as_view(), name='controle_delete'),
]
