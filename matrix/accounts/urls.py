from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("login_index",views.login_index,name='login_index'),
    path("staff_attendance",views.student_attendance,name='staff_attendance'),
    path("staff_register", views.staff_register, name='staff_register'),
    path("student_register", views.student_register, name='student_register'),
    path("delete/<int:id>", views.delete_data, name='delete_data'),
    path("<int:id>/", views.update_data, name='update_data'),
    path("student_attendance", views.student_attendance, name='student_attendance'),
    path("student_exam", views.student_exam, name='student_exam'),
    path("feedback_form", views.feedback_form, name='feedback_form'),
    path("show_feedback", views.showfeedback, name='show_feedback'),
    path("show_data", views.show_data, name='show_data'),
    path("studentdetail", views.studentdetail, name='studentdetail'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout')
]
