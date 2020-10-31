from django.urls import path
from .views import (
    TutorListView,
    # AddTutorView,
    UpdateTutorView,
    DeleteTutorView,
)

urlpatterns = [
    # path('MyHome/', views.myHome, name='studenthomepage' ),
    # path('', views.logopage , name='cars'),
    # path('MyMaterial/', views.myMat, name='teacherhomepage'),
    path('', TutorListView.as_view(), name='Tutor'),
    # path('add-tutor/', AddTutorView.as_view(), name='add_Tutor'),
    path('tutor/<int:pk>/update/', UpdateTutorView.as_view(), name='update_Tutor'),
    path('tutor/<int:pk>/delete/', DeleteTutorView.as_view(), name='delete_Tutor'),

]
