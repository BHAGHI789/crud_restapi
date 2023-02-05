from django.urls import path
from app import views
urlpatterns=[
    path('',views.list),
    path('add',views.Post_Book),
    path('<int:pk>',views.update_book),
    path('de/<int:pk>/',views.delete_book)
]