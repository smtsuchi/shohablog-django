from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('post/create/', views.createPost, name='blog-createpost'),
    path('register/', views.register, name='blog-register'),
    path('login/', views.loginPage, name='blog-login'),
    path('logout/', views.logoutUser, name='blog-logout'),
    path('api/', views.testAPI, name='api-test'),
]
