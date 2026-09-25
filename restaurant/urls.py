# Define URL route for index() view
from django.urls import path, include
from . import views

urlpatterns = [
    # ...,
    path('', views.index, name='index'),
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
]
