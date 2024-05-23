from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", apiOverview),
    path("task-list/", csrf_exempt(taskList), name="task-list"),
    path("task-detail/<str:pk>/", taskDetail, name="task-detail"),
    path("task-create/", taskCreate, name="task-create"),
    path("task-update/<str:pk>/", taskUpdate, name="task-update"),
    path("task-delete/<str:pk>/", taskDelete, name="task-delete"),
]
