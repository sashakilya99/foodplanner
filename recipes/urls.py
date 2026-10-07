from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path(
        'recipe/<int:recipe_id>/',
        views.recipe_detail,
        name='recipe_detail'
    ),

    path(
        'recipe/create/',
        views.recipe_create,
        name='recipe_create'
    ),

    path(
        'recipe/<int:recipe_id>/edit/',
        views.recipe_update,
        name='recipe_update'
    ),

    path(
        'recipe/<int:recipe_id>/delete/',
        views.recipe_delete,
        name='recipe_delete'
    ),
]