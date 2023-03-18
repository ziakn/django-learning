from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('show/', views.show_emp, name='show-emp'),
    # path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    # path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
]