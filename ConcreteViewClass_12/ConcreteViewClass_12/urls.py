"""
URL configuration for ConcreteViewClass_12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/student/',views.StudentList.as_view()),   # GET API
    # path('api/student/',views.StudentCreate.as_view()),     #POST API
    # path('api/student/<int:pk>',views.StudentRetrieve.as_view()),     #GET API
    # path('api/student/<int:pk>',views.StudentUpdate.as_view()),     #PUT APi
    # path('api/student/<int:pk>',views.StudentDestroy.as_view()),     #PUT APi


    path('api/student/',views.StudentListCreate.as_view()),   # GET API
    # path('api/student/<int:pk>',views.StudentRetrieveUpdate.as_view()),     #PUT APi
    # path('api/student/<int:pk>',views.StudentRetrieveDestroy.as_view()),     #PUT APi
    path('api/student/<int:pk>',views.StudentRetrieveUpdateDestroy.as_view()),     #PUT APi
    
]
