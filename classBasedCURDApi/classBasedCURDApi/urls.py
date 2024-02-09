
from django.contrib import admin
from django.urls import path
from CRUD_API import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentAPI.as_view()),
]
