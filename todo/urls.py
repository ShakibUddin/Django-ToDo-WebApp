from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='todo_home'),
    path('home/', views.home,name='todo_home'),
    path('mytask/', views.mytask,name='todo_mytask'),
    path('addtask/', views.addtask,name='todo_addtask'),
    path('deletetask/<int:todo_id>/', views.deletetask,name='todo_deletetask'),
    path('contact/', views.contact,name='todo_contact'),
    path('about/', views.about,name='todo_about'),
]
