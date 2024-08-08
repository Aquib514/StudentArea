
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .import settings
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('resume/',views.resume),
    path('cheatsheet/',views.cheatsheet,name='save'),
    path('login/', views.login),
    path('maths/', views.math),
    path('studentPage/', views.studentpage),
    path('notes/', views.note),
    path('matrix/', views.matrix),
    path('science/', views.science),
    path('matrixs/', views.matrixs,name="matrixs"),
    path('document/', views.document),
    path('datavisu/', views.datavisu),
    path('linear/', views.linear,name="linear"),
    path('linears/', views.linears, name="linears"),
    path('book/', views.book,name="book"),
    path('humrespi/', views.humrespi),
    path('bookread/', views.books, name="bookread"),
    path('bookread2/', views.books2, name="bookread2"),
    path('bookread3/', views.books3, name="bookread3"),
    path('bookread4/', views.books4, name="bookread4"),

    path('templatedesign/', views.tempdesign,name="tempdesign"),
    path('resumeTemplate/', views.resumeTemplate,name="resumeTemplate"),
    # path('cheatsheet/', views.cheatsheet, name='cheatsheet'),
    
    path('cheatsheet/<str:language>/', views.cheatsheet, name='cheatsheet'),
    path('pythonSheet/<str:language>/', views.pythonSheet, name='pythonSheet'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
