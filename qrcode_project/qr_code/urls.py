# urls.py inside your app folder

from django.urls import path

from . import views
 
urlpatterns = [

    path('', views.index, name='index'),        # main page (QR code generator)

    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

]
 