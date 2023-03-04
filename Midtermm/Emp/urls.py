from django.urls import path
from Emp import views

urlpatterns = [
    path('api/employees',views.todo_lists_handler),
    path('api/employees/<int:pk>',views.todo_list_handler)
]