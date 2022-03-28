from django.urls import path
from . import views

urlpatterns=[
    path('display',views.Display,name='Display'),
    path('',views.addform,name='addform'),
    path('update/<str:pk>',views.updateworkdetails,name='updateworkdetails'),
    path('details',views.adddetailsform,name='adddetails'),
    path('delete/<str:pk>',views.deletework,name='deletework')
]
