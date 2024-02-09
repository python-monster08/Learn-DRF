
from django.contrib import admin
from django.urls import path
from DRF_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:pk>', views.student_details, name='student_info'),
    path('student_info/', views.student_list, name='student_list'),
]
