from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('update/<int:image_id>/', views.update_image, name='update_image'),
] 