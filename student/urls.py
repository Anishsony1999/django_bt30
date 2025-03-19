from django.urls import path
from student import views

from django.conf import settings
from django.conf.urls.static import static

# 127.0.0.1:8000/student

app_name = 'students'

urlpatterns = [

    path('',views.index,name='welcome'),

    path('wel/<str:name>',views.greeting), # student/wel/Anihs 

    path('index/',views.indexPage,name='index'), # student/index
    
    path('student_about/',views.about,name='about'),    # student/student_about

    path('newindex/',views.index2,name='index2'),

    path('find/<int:num>',views.find,name='searchbyid'),

    path('contact',views.show_contact,name='c'),

    path('home/welcome',views.home,name="home"),

    path('projects',views.projects,name="projects"),

    path('products',views.show_products,name='products'),

    path('findbyid/<slug:slug>',views.findbyid,name='findbyid'),

    path('register',views.register,name='register'),

    path('sregister/',views.student_reg,name='student_reg'),

    path('sendmail/',views.send_my_email,name="send_mail"),

    path('home2/',views.home2,name='home2'),

    path('country/<int:id>',views.states_by_id,name='states'),

    path('login/',views.login,name='student_login'),

    path('logout',views.user_logout,name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# student/index