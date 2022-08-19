from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="base", kwargs={'navbar': 'home'}),
    path("home/", views.home, name="home", kwargs={'navbar': 'home'}),
    path("question/", views.question, name="question"),
    path("show_questions/", views.show_questions, name="show_questions", kwargs={'navbar': 'show_questions'}),
    path("delete/<int:id>", views.delete, name="delete"),
    path("edit/<int:id>", views.edit, name="edit")
]
