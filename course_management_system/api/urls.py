from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListTrainee, AddTrainee, UpdateTrainee, DeleteTrainee, CourseUpdate, CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)  

urlpatterns = [
    path('trainees/', ListTrainee.as_view(), name='list-trainees'),
    path('trainees/add/', AddTrainee.as_view(), name='add-trainee'),
    path('trainees/<int:pk>/', UpdateTrainee.as_view(), name='update-trainee'),
    path('trainees/<int:pk>/delete/', DeleteTrainee.as_view(), name='delete-trainee'),
    path('courses/<int:pk>/', CourseUpdate, name='update-course'),
    path('', include(router.urls)), 
]
