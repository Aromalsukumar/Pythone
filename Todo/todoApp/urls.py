from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('view',views.display),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete)
]
