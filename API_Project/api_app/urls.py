from django.urls import path
from api_app import views

urlpatterns = [
    path('bulk_insert/',views.insert,name='insert'),
    path('',views.products_list,name='products_list'),
]
