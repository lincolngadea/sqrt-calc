from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
    # path('criar/', create, name='criar'),
    # path('modificar/<int:user_id>', refresh, name='modificar'),
    # path('deletar/<int:user_id>', delete, name='deletar')
]