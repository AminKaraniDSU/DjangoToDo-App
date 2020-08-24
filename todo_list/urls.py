from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name= 'home'),
    path('about/',views.about,name= 'about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('Uncrouss/<list_id>',views.Uncrouss,name='Uncrouss'),
    path('Croussoff/<list_id>',views.Croussoff,name='Croussoff'),
    path('edit/<list_id>',views.edit,name='edit'),
]
