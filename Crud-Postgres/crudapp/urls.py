from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.test, name='test'),
    path("get/id/<int:id>", views.getById),
    path("create/", views.create),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete)
]