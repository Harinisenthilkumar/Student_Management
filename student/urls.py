from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('signup/', views.student_signup, name='student_signup'),
    path('student-list/', views.student_list, name='student_list'),
]
