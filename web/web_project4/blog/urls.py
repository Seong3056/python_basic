from django.urls import path
from . import views



urlpatterns = [
    path("", views.index),
    path("posts/", views.post_list),
    path("posts/<int:post_id>/", views.post_detail),
    path("posts/add/", views.post_add),
]
