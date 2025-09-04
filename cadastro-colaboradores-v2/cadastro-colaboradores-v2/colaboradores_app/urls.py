from django.urls import path
from . import views
urlpatterns = [
    path('', views.ColaboradorListView.as_view(), name='colaborador_list'),
    path('novo/', views.ColaboradorCreateView.as_view(), name='colaborador_novo'),
    path('editar/<int:pk>/', views.ColaboradorUpdateView.as_view(), name='colaborador_editar'),
    path('excluir/<int:pk>/', views.ColaboradorDeleteView.as_view(), name='colaborador_excluir'),
]
