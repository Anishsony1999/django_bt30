from django.urls import path
from student import views

# 127.0.0.1:8000/student

app_name = 'students'

urlpatterns = [

    path('',views.index,name='welcome'),

    path('wel/<str:name>',views.greeting), # student/wel/Anihs 

    path('index',views.indexPage,name='index'), # student/index
    
    path('student_about/',views.about,name='about'),    # student/student_about

    path('newindex/',views.index2,name='index2'),

    path('find/<int:num>',views.find,name='searchbyid'),

    path('contact',views.show_contact,name='c'),

    path('home/welcome',views.home,name="home"),

    path('projects',views.projects,name="projects"),

    path('products',views.show_products,name='products'),

    path('findbyid/<int:id>',views.findbyid,name='findbyid'),

    path('register',views.register,name='register'),

    path('sregister/',views.student_reg,name='student_reg'),

    path('sendmail/',views.send_my_email,name="send_mail"),

    path('sendimage',views.send_email_with_image_html),
]

# student/index