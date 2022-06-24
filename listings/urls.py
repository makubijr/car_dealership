from django.urls import path
from .import views
urlpatterns = [
    path('',views.listings,name='listings'),
    path('create/',views.create,name='create'),
    path('listing/<id>/',views.listing,name='listing'),
]