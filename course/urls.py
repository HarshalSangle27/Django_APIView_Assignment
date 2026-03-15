from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView

urlpatterns = [
    # GET and POST for the entire list
    path('', CourseListCreateAPIView.as_view(), name='course-list-create'),
    
    # GET, PUT, PATCH, DELETE for a specific course ID
    # The <int:pk> captures the ID from the URL and passes it to your view
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
]