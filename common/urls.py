from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.do_logout, name="user_logout"),
    path('pendings/', views.pendigs, name="pendings"),
    
    path('exams/', views.exams, name="exams"),
    path('all-cr-of-each-intakes/', views.all_cr, name="all_cr"),
    path('all-assignments/', views.assignments, name="assignments"),
    path('sign-up/', views.register, name="registration"),
    path('fill-up-register-info/', views.last_step_of_register, name="last_step_of_register"),
    path('add-routine/', views.add_routine, name="add_routine"),
    
    path('add-assignments/', views.add_assignments, name="add_assign"),
    path('view-assignments/<str:the_id>', views.view_assignment, name="view_assign"),
    path('calender/', views.calender, name="calender"),
    path('all-announcements/', views.all_announcement, name="all_announcement"),
    path('add-announcement/', views.add_announcement, name="add_announcement"),

    path('temp/', views.test_function, name="temp"),

]