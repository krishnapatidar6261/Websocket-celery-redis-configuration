from django.urls import path
from . import views 


urlpatterns=[

    path("", views.index, name="index"),
    path("celery-task/", views.check_celery_working,name="celery_task")
]