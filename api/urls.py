from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
urlpatterns = [

    # login api
    path('login/',LoginView.as_view(),name="login" ),
    
    # board crud api
    path('add-board/',BoardCreateView.as_view(),name="add-board" ),
    path('get-board/<int:id>',BoardCreateView.as_view(),name="get-board" ),
    path('del-board/<int:id>',BoardCreateView.as_view(),name="del-board" ),
    path('edit-board/<int:id>',BoardCreateView.as_view(),name="edit-board" ),
    
    # list crud api
    path('add-list/',ListView.as_view(),name="add-list" ),
    path('get-list/<int:id>',ListView.as_view(),name="get-list" ),
    path('del-list/<int:id>',ListView.as_view(),name="del-list" ),
    path('edit-list/<int:id>',ListView.as_view(),name="edit-list" ),
    
    # card crud  api
    path('add-card/',CardView.as_view(),name="add-card" ),
    path('get-card/',CardView.as_view(),name="get-card" ),
    path('del-card/<int:id>',CardView.as_view(),name="del-card" ),
    path('edit-card/<int:id>',CardView.as_view(),name="edit-card" ),


]
