from django.urls import path
from student import views

# 127.0.0.1:8000/student

urlpatterns = [

    path('',views.index),

    path('wel/<str:name>',views.greeting), # student/wel/Anihs 

    path('index',views.indexPage), # student/index
    
    path('about/',views.about),    # student/about
]

# student/index