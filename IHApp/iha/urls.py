from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('iha-ekle', views.create_iha, name='iha_ekle'),
    path('iha-list', views.iha_list, name='iha_list'),
    path('iha-edit/<int:id>', views.iha_edit, name='iha_edit'),
    path('iha-delete/<int:id>', views.iha_delete, name='iha_delete'),
    path('<slug:slug>', views.details, name='iha_details'),
    path('category/<slug:slug>', views.getIhasByCategory, name='ihas_by_category')
]
