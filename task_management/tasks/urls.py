from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks_list),
    path('actions/', task_actions),
    path('actions/login/', login_page, name="login"),
    path('actions/logout/', logout_page, name="logout"),
    path('actions/create/', create_action),
    path('actions/update/<int:id>', update_action),
    path('actions/delete/<int:id>', delete_action),
]
