from django.urls import path
from . import views

app_name = 'adminApi'


urlpatterns = [
    path('', views.home),
    path('multi/', views.evalution_admin, name='adminApi'),
    path('test/', views.index, name='adminApi'),
    path('fenetre/', views.evalution_admin),
    path('change-dataset/', views.dataset),
    path('get-dataset/', views.set_dataset),
    path('visual-data/', views.visual_data),
]