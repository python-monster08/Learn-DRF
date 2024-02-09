
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('api/student',views.StudentModelViewSet,basename='student')
# router.register('api/student2',views.StudentModelViewSet2,basename='student2')
# router.register('api/student3',views.StudentModelViewSet3,basename='student3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework'))
    
]
