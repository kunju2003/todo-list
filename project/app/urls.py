from django.urls import path
from . import views

urlpatterns=[
    path('',views.todo),
    path('todo_update/<pk>',views.todo_update)
    
]