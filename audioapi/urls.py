from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('createapi/',views.createapi,name="createapi"),
    path('getapi/<audioFileType>/<audioFileID>',views.getapi,name="getapi"),
    path('getapi/<audioFileType>',views.getapi,name="getapi1"),
    path('deleteapi/<audioFileType>/<audioFileID>',views.deleteapi,name="delete"),
    path('updateapi/<audioFileType>/<audioFileID>',views.updateapi,name="updateapi")

]